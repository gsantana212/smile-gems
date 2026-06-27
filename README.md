# SMILE GEMS — DIY Tooth Gem Kits

A 3-SKU e-commerce site for Ali (Pretty Stoned) — pre-portioned tooth gem kits for artists and beginners.

🌐 **Live preview (GitHub Pages):** https://gsantana212.github.io/smile-gems/

## What's here

- **index.html** — full landing page (hero, kits grid, how-it-works, reviews, vendors, math, FAQ, CTA)
- **photos/** — 9 product images (kit1, kit2, kit3 + lifestyle)
- **buyKit() JS** — wired for production Stripe checkout, demo-stubbed here

## The three SKUs

| SKU | Price | Contents |
|---|---|---|
| The Starter | $39 | 10 crystals, cure light, etchant, practice tooth |
| The Pro (featured) | $89 | 50 crystals, pro light, full pro kit |
| The Vault | $149 | 200 premium gems, display case, 1:1 consult |

## Production stack (separate from this preview)

When Ali is ready to take payments:

- **Frontend:** same `index.html` (drop-in replace of this demo)
- **Backend:** `toothgem/api.py` — Python + SQLite, single file
- **Payments:** Stripe Checkout
- **Hosting:** `skillhub.shop/toothgem/` (live now)
- **Domain:** will migrate to `pretty-stoned.com` when ready

## Source / inspiration

- Juliana Lupul — "Materials you need for Tooth Gems | FREE Vendor List" (YouTube, Nov 2024)
- Vendor table in `index.html` credits her blueprint + 8 actual vendor links

## Client context

- **Client:** Ali (boss's friend)
- **Brand:** Pretty Stoned
- **Status:** Live preview at GitHub Pages, backend pending Stripe setup
- **Reusable patterns:** every feature shipped here is documented in the SkillHub agents/skills catalog

---

*Built with 💎 — Ada CEO, 2026-06-27*