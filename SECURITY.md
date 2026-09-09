# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this site or its underlying code,
please report it privately to the project owner. **Do not file a public GitHub
issue for security problems.**

- **Email:** security@pretty-stoned.com
- **Response window:** within 7 business days
- **Encrypted reports:** PGP key available on request

## Scope

This repository currently contains a static landing page (HTML, CSS, vanilla
JavaScript) with no backend, no authentication, and no production payment
wiring. Once the production Stripe integration is added, anything that could
expose a Stripe key, customer data, or the live checkout flow falls in scope.

## What to include

When reporting, please include:

1. A clear description of the issue and its impact.
2. Steps to reproduce (URL, browser, request payload, screenshot).
3. Whether the issue is on the static preview (`gsantana212.github.io/smile-gems/`)
   or the production site (`skillhub.shop/toothgem/`).
4. Your name / handle for credit in the fix release notes (optional).

We will acknowledge receipt, triage within 7 days, and coordinate disclosure
timing with you before any public mention.
