---
distilled: 2026-09-19
via: brain-install starter-kit
---

# Tool Stack

**Important:** the source explicitly instructs to "treat all integration status as verify before migration, not automatically live." Everything below is *known/preferred*, not confirmed production-live, unless noted.

| Tool | Role | Owner | Live status |
|---|---|---|---|
| Vendasta | Core partner ecosystem — white-label marketplace + CRM-related services | `UNVERIFIED` | `UNVERIFIED` |
| Seamless.AI, Apollo | Lead sourcing / outbound enrichment | `UNVERIFIED` | `UNVERIFIED` |
| n8n | Automation (primary) | `UNVERIFIED` | `UNVERIFIED` |
| Zapier / Make | Automation (secondary, where appropriate) | `UNVERIFIED` | `UNVERIFIED` |
| ChatGPT workflows | AI content | `UNVERIFIED` | `UNVERIFIED` |
| HeyGen, ElevenLabs | AI avatars / voice | `UNVERIFIED` | `UNVERIFIED` |
| Runway | Creative / video workflows | `UNVERIFIED` | `UNVERIFIED` |
| GA4, Google Tag Manager, Search Console | Analytics | `UNVERIFIED` | `UNVERIFIED` |
| Microsoft Clarity or Hotjar | Behavior analytics | `UNVERIFIED` (either/or, not both confirmed) | `UNVERIFIED` |
| CallRail (or equivalent) | Call tracking | `UNVERIFIED` | `UNVERIFIED` |
| Next.js, TypeScript, Tailwind, React Hook Form, Zod, Recharts | Web/data architecture — "prior Revenue Audit specification used" this stack | `UNVERIFIED` | Prior spec, not confirmed current |
| Supabase | Audit storage — **source flags "must be verified/configured in production"** | `UNVERIFIED` | Not confirmed live; missing `SUPABASE_URL` / `SUPABASE_SERVICE_ROLE_KEY` per source |
| Resend | Report email — **same flag** | `UNVERIFIED` | Not confirmed live; missing `RESEND_API_KEY`, `REPORT_FROM_EMAIL` per source |
| Stripe | Payments, where applicable | `UNVERIFIED` | `UNVERIFIED` |
| Cloudflare | Security / infrastructure | `UNVERIFIED` | `UNVERIFIED` |

## Known missing production configuration (as documented in source)
Earlier Revenue Leak Audit builds identified these as unconfigured: database (Supabase), CRM webhook, report email (Resend), admin routing. Target env vars named: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `CRM_WEBHOOK_URL`, `RESEND_API_KEY`, `REPORT_FROM_EMAIL`, `ADMIN_EMAILS`. Vendasta routing needs its own Partner CRM/service-account credentials and permissions.

**No credential values exist anywhere in this corpus** — only the names of the env vars that need to be set. Per AGENTS.md §1, any actual key values go only in `200 Notes/Admin/Credentials/api-keys.env`, never in this note.

---
**Sources:** [[Master Business OS]]
**UNVERIFIED:** which tools are actually live in production today vs. planned/aspirational — source explicitly lists "which integrations are live today versus planned" as pending CEO confirmation.
**CONFLICT:** none.
