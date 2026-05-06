// api/waitlist.js
// Vercel serverless function — receives waitlist signups and sends via Resend

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, source } = req.body;

  if (!email || !email.includes('@')) {
    return res.status(400).json({ error: 'Valid email required' });
  }

  const RESEND_API_KEY = process.env.RESEND_API_KEY;
  const NOTIFY_EMAIL = process.env.NOTIFY_EMAIL; // e.g. juanfe@evolve-iq.com

  if (!RESEND_API_KEY) {
    console.error('RESEND_API_KEY not set');
    return res.status(500).json({ error: 'Server configuration error' });
  }

  try {
    // 1. Send notification to the team
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'COR Waitlist <waitlist@evolve-iq.com>',
        to: [NOTIFY_EMAIL || 'juanfe@evolve-iq.com'],
        subject: `New waitlist signup: ${email}`,
        html: `
          <p><strong>New COR waitlist signup</strong></p>
          <p>Email: <strong>${email}</strong></p>
          <p>Source: ${source || 'unknown'}</p>
          <p>Time: ${new Date().toISOString()}</p>
        `,
      }),
    });

    // 2. Send confirmation to the user
    await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: 'COR <waitlist@evolve-iq.com>',
        to: [email],
        subject: "You're on the COR waitlist",
        html: `
          <div style="font-family: 'DM Sans', sans-serif; max-width: 480px; margin: 0 auto; padding: 40px 24px; background: #0B0C0F; color: #F0EEE8;">
            <h1 style="font-size: 28px; font-weight: 400; margin-bottom: 16px; color: #C8F060;">You're on the list.</h1>
            <p style="color: #9EA2AE; line-height: 1.7; margin-bottom: 24px;">
              Thanks for joining the COR waitlist. We're in private beta and will reach out when we have a spot for you.
            </p>
            <p style="color: #9EA2AE; line-height: 1.7; margin-bottom: 24px;">
              COR is the GTM Marketing OS for solo marketers at Seed and Series A B2B SaaS — connecting calls, LinkedIn signals, and AI search visibility into one system.
            </p>
            <p style="color: #6B6E7A; font-size: 13px;">— The COR team at evolve-iq.com</p>
          </div>
        `,
      }),
    });

    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Resend error:', err);
    return res.status(500).json({ error: 'Failed to send email' });
  }
}
