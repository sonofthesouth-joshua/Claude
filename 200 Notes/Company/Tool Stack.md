---
distilled: 2026-09-19
via: brain-install starter-kit
---

# Tool Stack

**Confirmed by owner (2026-09-19): nothing below is live — SMM is pre-launch.** Every row is the *target* stack from the source documents, not a connected/configured tool. Re-run this doc as each tool actually gets set up.

| Tool | Role | Live status |
|---|---|---|
| Vendasta | Core partner ecosystem — white-label marketplace + CRM-related services | Not live — pre-launch |
| Seamless.AI, Apollo | Lead sourcing / outbound enrichment | Not live — pre-launch |
| n8n | Automation (primary) | Not live — pre-launch |
| Zapier / Make | Automation (secondary, where appropriate) | Not live — pre-launch |
| ChatGPT workflows | AI content | Not live — pre-launch |
| HeyGen, ElevenLabs | AI avatars / voice | Not live — pre-launch |
| Runway | Creative / video workflows | Not live — pre-launch |
| GA4, Google Tag Manager, Search Console | Analytics | Not live — pre-launch |
| Microsoft Clarity or Hotjar | Behavior analytics (either/or, not both specified) | Not live — pre-launch |
| CallRail (or equivalent) | Call tracking | Not live — pre-launch |
| Next.js, TypeScript, Tailwind, React Hook Form, Zod, Recharts | Web/data architecture — "prior Revenue Audit specification used" this stack | Not live — prior spec, pre-launch |
| Supabase | Audit storage — **source flags "must be verified/configured in production"** | Not live; missing `SUPABASE_URL` / `SUPABASE_SERVICE_ROLE_KEY` per source |
| Resend | Report email — **same flag** | Not live; missing `RESEND_API_KEY`, `REPORT_FROM_EMAIL` per source |
| Stripe | Payments, where applicable | Not live — pre-launch |
| Cloudflare | Security / infrastructure | Not live — pre-launch |

## Known missing production configuration (as documented in source)
Earlier Revenue Leak Audit builds identified these as unconfigured: database (Supabase), CRM webhook, report email (Resend), admin routing. Target env vars named: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `CRM_WEBHOOK_URL`, `RESEND_API_KEY`, `REPORT_FROM_EMAIL`, `ADMIN_EMAILS`. Vendasta routing needs its own Partner CRM/service-account credentials and permissions.

**No credential values exist anywhere in this corpus** — only the names of the env vars that need to be set. Per AGENTS.md §1, any actual key values go only in `200 Notes/Admin/Credentials/api-keys.env`, never in this note.

---
**Sources:** [[Master Business OS]]; live status confirmed by owner, 2026-09-19
**UNVERIFIED:** none on live-status — "nothing is live yet" is owner-confirmed. Still open: which tools Joshua will actually adopt first vs. treat as aspirational/later-stage.
**CONFLICT:** none.
