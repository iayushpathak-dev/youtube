# Creator voice clone (Shorts narration)

Decision: DEC-008 + DEC-013 (b). The creator asked on 2026-11-21: "so lets set up a ai voice tool jo meri voice use krega".

## Setup
| Item | Value |
|---|---|
| Provider | **ElevenLabs**: Instant Voice Cloning, API, commercial licence |
| Plan | Starter (≈ US$6/month, ~30k credits, cloning + commercial rights per third-party guides, Nov 2026). **Verify the price at elevenlabs.io/pricing before paying.** |
| API host | `api.elevenlabs.io`, header `xi-api-key` |
| Key storage | Environment network secret (saved via the secure form). **Never in this repo.** |
| Voice name | `AI Made Usable - Creator` (voice_id recorded below once created) |
| Model | Multilingual v2 (handles the Indian-English accent of the sample). Re-evaluate after the first listening test. |
| voice_id | _not created yet_ |

## Rules
- Clone **only the creator's own voice**, with the creator's consent (given 2026-11-21).
- **YouTube disclosure:** a cloned own voice counts as altered/synthetic content, so tick **"Altered content = Yes"** at upload for every Short narrated by the clone. Per YouTube, this doesn't limit reach or monetization. [YouTube Help](https://support.google.com/youtube/answer/14328491)
- Long-form stays in the creator's real voice (DEC-003).
- Every clone-narrated Short must carry original insight or a real demo (inauthentic-content policy, Jul 2026).
- The creator listens to every generated voiceover before it is published.

## Recording the sample (creator)
- 1.5–3 minutes total. Quiet room (soft furnishings, no fan/AC noise), phone 20–30 cm from the mouth, the same distance throughout.
- Speak naturally, at your normal Shorts energy. Don't "perform". Pauses are fine.
- Export as the original voice memo file (m4a/wav/mp3). Don't apply filters.
- Read the script below in one take (re-read a line if you stumble, Claude trims it).

### Sample script (≈2 minutes)
> Hi, I'm the voice behind AI Made Usable. Every week I test AI tools on real work, so you can see what actually helps and what doesn't.
>
> Today's question is simple: which AI should you use for which job? ChatGPT, Claude, Gemini. They all sound confident. But confidence isn't the same as being right, so I built a test they can't bluff.
>
> Here's the idea. I made a spreadsheet for a small shop and hid three problems inside it. Weekend sales are sixty-six percent higher. One region dropped by half. And one product keeps coming back as returns. A good AI should find all three. A bad one will invent numbers.
>
> Quick tip before we start. If your AI emails sound robotic, give it four things: who's reading, what you want, the facts, and the tone. Reader, goal, facts, tone. That's it.
>
> Now, agents. A chatbot answers you. An agent does the work. It plans the steps, uses tools, checks the result, and repeats until the job is done. Sounds amazing, right? It is, until it makes a mistake, which is why the best agents ask before doing anything important.
>
> And one more thing. Never trust a link just because an AI gave it to you. Open it. Find the exact claim. Check the date. Five seconds, every time.
>
> Okay, that's enough from me. Is this exciting? Honestly, yes. Is it perfect? Not even close. Let's find out what actually works. Discover, build, automate, ship. See you on Tuesday.

## Log
- 2026-11-21 · Setup started. Waiting for the creator's ElevenLabs account + API key + voice sample.
