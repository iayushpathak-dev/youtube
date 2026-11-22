# SWAI-L001 test data: answer key (do not show to the AIs)

File: `test-data-sales.csv`. A synthetic dataset made by Claude for this test (seed 42), so every number is checkable.
1840 rows · 2026-07-01 → 2026-09-30 · 4 regions × 5 products · prices in INR.

## Planted insights (what a good AI should find)
1. **Weekend effect:** the average units per row are 17.0 on weekends vs 10.3 on weekdays (**66% higher**).
2. **East region is declining:** East revenue by month: 2026-07: ₹967,389, 2026-08: ₹726,915, 2026-09: ₹464,881 (**52% drop Jul→Sep**). Other regions are flat.
3. **Headphones have a returns problem:** return rate Notebook 2.8%, Backpack 2.1%, Water Bottle 3.4%, Desk Lamp 3.2%, Headphones 22.8%.

## Totals
Total revenue ₹11,883,861. By region: East ₹2,159,185, North ₹3,251,509, South ₹3,260,502, West ₹3,212,665

## Scoring for task 3
- 1 point per planted insight found (max 3). −1 for any invented number that doesn't match this key.
- A bonus note if it makes a correct chart.
