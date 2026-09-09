# AGENTS.md — gsantana212/smile-gems

> Operating contract for any AI agent opening this repo. Read first.

## What this repo is

A **3-SKU e-commerce preview** for Ali (Pretty Stoned) — pre-portioned DIY tooth gem kits.
This is the **design preview**, not the production checkout. Production lives separately
at `https://skillhub.shop/toothgem/`.

Per `README.md`:

> A 3-SKU e-commerce site for Ali (Pretty Stoned) — pre-portioned tooth gem kits for
> artists and beginners.

Repo state: **single-commit preview**, untouched since 2026-06-27. The badge says
`preview--demo`; that is the truth.

## Repo layout (verified 2026-08-31)

| File / dir | Role | Notes |
|---|---|---|
| `index.html` | Full landing page | hero, kits grid, how-it-works, reviews, vendors, math, FAQ, CTA |
| `photos/` | Product imagery | 9 images: `hero.jpg`, `kit1.jpg`–`kit6.jpg`, plus lifestyle shots |
| `LICENSE`, `SECURITY.md`, `README.md` | Standard repo glue | — |

## The three SKUs (from README)

| SKU | Price | Contents |
|---|---|---|
| The Starter | $39 | 10 crystals, cure light, etchant, practice tooth |
| The Pro (featured) | $89 | 50 crystals, pro light, full pro kit |
| The Vault | $149 | 200 premium gems, display case, 1:1 consult |

## What an agent here can do safely

- **Edit copy in `index.html`** — hero text, kit descriptions, FAQ answers, testimonials.
- **Replace photos in `photos/`** — keep the filenames (`hero.jpg`, `kit1.jpg`–`kit6.jpg`)
  so existing `<img>` references don't break.
- **Update `README.md` status block** when the project transitions out of preview.
- **Add `SECURITY.md` disclosures** if a vulnerability is found.

## What an agent must NOT do here

- **Do not wire real payments here.** The `buyKit()` JS is **demo-stubbed** for a reason.
  Real Stripe checkout lives in the separate production repo at `skillhub.shop/toothgem/`.
- **Do not commit Ali's Stripe API key** — it goes in `/root/.hermes/secrets/`,
  never in this repo.
- **Do not change the photo filenames** — external references in the production
  checkout depend on the current naming.

## Conventions

- Currency: USD; prices are whole dollars (Stripe handles the cents).
- Image dimensions: keep photos roughly 800×800 for `kit*.jpg`; hero is wider
  (currently 267 KB → aim for < 400 KB to keep Pages snappy).
- Copy tone: friendly, beginner-reassuring, "I can do this" — not clinical.

## Build / serve

```bash
# No build step. Serve the directory:
python3 -m http.server 8000
# Production: https://skillhub.shop/toothgem/ (separate repo)
```

## Status snapshot (2026-08-31)

- Repo state: preview/demo, untouched since 2026-06-27
- Live preview: `gsantana212.github.io/smile-gems/`
- Production: `skillhub.shop/toothgem/` (separate, private)
- Backend: pending — Stripe API key still needs delivery from Ali

## Provenance

Generated 2026-08-31 by Hermes subagent during Week-1 consolidation
(`/root/.hermes/research/synthesis-2026-08-31.md` §2 action #2). Cited content is from
on-disk `README.md` and `ls photos/` at that time.