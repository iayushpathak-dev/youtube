// Same scripted test for every habit-tracker app (SWAI-L001 Round 4):
// add 2 habits, tick today for both, read the streak, reload, check that everything persisted.
// Usage: node production/apptest/habit-test.js <dir-with-chatgpt.html/gemini.html/claude.html>
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const dir = path.resolve(process.argv[2] || '.');

const apps = {
  chatgpt: {
    add: async p => { for (const n of ['Drink water', 'Read 10 pages']) { await p.fill('#habitInput', n); await p.click('.add-btn'); await p.waitForTimeout(400); } },
    tick: async (p, today) => { const sel = `button.check[data-date="${today}"]`; const n = await p.locator(sel).count(); for (let i = 0; i < n; i++) { await p.locator(sel).nth(i).click(); await p.waitForTimeout(300); } },
    read: p => p.$$eval('tbody tr', rs => rs.map(r => r.querySelector('.habit-name').textContent.trim() + ' | ticked:' + r.querySelectorAll('.check.done').length + ' | ' + r.querySelector('.streak').textContent.replace(/\s+/g, ' ').trim())),
  },
  claude: {
    add: async p => { for (const n of ['Drink water', 'Read 10 pages']) { await p.fill('#habitInput', n); await p.click('#addForm button[type=submit]'); await p.waitForTimeout(400); } },
    tick: async (p, today) => { const sel = `button.check[data-day="${today}"]`; const n = await p.locator(sel).count(); for (let i = 0; i < n; i++) { await p.locator(sel).nth(i).click(); await p.waitForTimeout(300); } },
    read: p => p.$$eval('#grid tbody tr', rs => rs.map(r => r.querySelector('.name').textContent.trim() + ' | ticked:' + r.querySelectorAll('.check.done').length + ' | ' + r.querySelector('.streak').textContent.replace(/\s+/g, ' ').trim())),
  },
  gemini: {
    add: async p => { for (const n of ['Drink water', 'Read 10 pages']) { await p.click('#openAddModalBtn'); await p.fill('#habitNameInput', n); await p.click('#saveHabitBtn'); await p.waitForTimeout(400); } },
    tick: async (p, today) => {
      for (const b of await p.$$(`button[data-action="toggle-day"][data-date="${today}"]`)) {
        const label = await b.getAttribute('aria-label');
        if (/Drink water|Read 10 pages/.test(label) && (await b.getAttribute('aria-pressed')) === 'false') { await p.locator(`button[aria-label="${label}"]`).click(); await p.waitForTimeout(300); }
      }
    },
    read: p => p.$$eval('#habitListContainer > div', rs => rs.map(r => r.querySelector('span[title]').textContent.trim() + ' | ticked:' + r.querySelectorAll('button[aria-pressed="true"]').length + ' | ' + (r.querySelector('span[title$="streak"]') || {}).textContent.replace(/\s+/g, ' ').trim())),
  },
};

(async () => {
  const d = new Date();
  const today = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const b = await chromium.launch();
  for (const [name, a] of Object.entries(apps)) {
    const file = path.join(dir, name + '.html');
    if (!fs.existsSync(file)) { console.log(name, 'missing'); continue; }
    const ctx = await b.newContext({ viewport: { width: 1280, height: 720 }, recordVideo: { dir: path.join(dir, 'video-' + name), size: { width: 1280, height: 720 } } });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + file);
    await p.waitForTimeout(1500);
    const before = await a.read(p).catch(e => 'read failed: ' + e.message);
    await a.add(p);
    await a.tick(p, today);
    await p.waitForTimeout(800);
    const afterTick = await a.read(p).catch(e => 'read failed: ' + e.message);
    await p.reload();
    await p.waitForTimeout(1500);
    const afterReload = await a.read(p).catch(e => 'read failed: ' + e.message);
    await p.screenshot({ path: path.join(dir, name + '-after-reload.png') });
    console.log(JSON.stringify({ name, before, afterTick, afterReload, errors: errs }, null, 1));
    await ctx.close();
  }
  await b.close();
})();
