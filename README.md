# COR Waitlist Landing Page

Standalone Vercel project. No framework, no build step — deploys in under 2 minutes.

## Structure

```
/index.html          ← Landing page (all styles + JS inline)
/api/waitlist.js     ← Vercel serverless function (Resend integration)
/vercel.json         ← Routing config
```

## Deploy

### 1. Create repo & push

```bash
git init
git add .
git commit -m "Initial commit"
gh repo create cor-waitlist --private --source=. --push
# or push to your existing GitHub org
```

### 2. Connect to Vercel

1. Go to vercel.com/new
2. Import the `cor-waitlist` repo
3. No build settings needed — Vercel detects static + serverless automatically
4. Click Deploy

### 3. Add environment variables in Vercel

In your project settings → Environment Variables:

| Key | Value |
|-----|-------|
| `RESEND_API_KEY` | Your existing Resend API key |
| `NOTIFY_EMAIL` | e.g. `juanfe@evolve-iq.com` |

> The `from` address is `waitlist@evolve-iq.com` — your `evolve-iq.com` domain is already verified in Resend, so this works out of the box.

### 4. Set custom domain (optional)

In Vercel project → Settings → Domains → add `cor.evolve-iq.com` or your preferred domain.

## Waitlist data

Signups currently flow as email notifications to `NOTIFY_EMAIL`. To also log to a spreadsheet or Airtable, update `api/waitlist.js` to POST to a webhook (Zapier, Make, etc.) alongside the Resend calls.

If you want a persistent list without any extra tools, add a free [Airtable](https://airtable.com) base and POST to their API in the same handler.
