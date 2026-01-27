# EmailJS Setup Guide for Quote Request Forms

This guide will help you set up EmailJS to send quote request emails directly from the forms without opening the user's email client.

## Step 1: Create EmailJS Account

1. Go to [https://www.emailjs.com/](https://www.emailjs.com/)
2. Click "Sign Up" and create a free account
3. Verify your email address

## Step 2: Create an Email Service

1. In your EmailJS dashboard, go to **Email Services**
2. Click **Add New Service**
3. Choose your email provider (Gmail, Outlook, etc.)
4. Follow the connection instructions for your provider
5. Once connected, note your **Service ID** (you'll need this later)

## Step 3: Create an Email Template

1. Go to **Email Templates** in your EmailJS dashboard
2. Click **Create New Template**
3. Use the following template structure:

**Template Name:** Quote Request Template

**Subject:**
```
{{subject}}
```

**Content (HTML):**
```html
<p><strong>From:</strong> {{from_name}} ({{from_email}})</p>
<p><strong>Reply To:</strong> {{reply_to}}</p>
<hr>
{{message}}
```

**Template Variables to Add:**
- `to_email` - Recipient email address
- `to_name` - Recipient name
- `from_name` - Sender name
- `from_email` - Sender email
- `subject` - Email subject
- `message` - Email body (HTML formatted)
- `reply_to` - Reply-to email address

4. Save the template and note your **Template ID**

## Step 4: Get Your Public Key

1. Go to **Account** > **General**
2. Find your **Public Key** (also called API Key)
3. Copy this key

## Step 5: Update the Forms

Open both `domestic-quote-request.html` and `international-quote-request.html` and find the `EMAILJS_CONFIG` section (around line 1230-1235).

Replace the following values:

```javascript
const EMAILJS_CONFIG = {
    publicKey: "YOUR_PUBLIC_KEY",        // Paste your Public Key here
    serviceId: "YOUR_SERVICE_ID",        // Paste your Service ID here
    templateId: "YOUR_TEMPLATE_ID",     // Paste your Template ID here
    enabled: true                        // Change to true to enable EmailJS
};
```

### Example:
```javascript
const EMAILJS_CONFIG = {
    publicKey: "abc123xyz789",
    serviceId: "service_gmail",
    templateId: "template_quote123",
    enabled: true
};
```

## Step 6: Test the Forms

1. Fill out a test quote request form
2. Submit the form
3. Check the email inbox for `eissales@dbaco.com`
4. Verify all fields are included and formatted correctly

## Troubleshooting

### Emails not sending
- Check browser console for errors (F12 > Console)
- Verify all three IDs are correct (Public Key, Service ID, Template ID)
- Ensure `enabled: true` is set
- Check that your EmailJS service is properly connected

### Email format issues
- Verify your template includes `{{message}}` variable
- Check that HTML is enabled in your template settings

### Fallback to mailto
- If EmailJS fails, the form will automatically fallback to opening the user's email client
- This ensures users can always submit their request

## EmailJS Free Tier Limits

- 200 emails per month
- Perfect for most small to medium businesses
- Upgrade available if needed

## Support
For EmailJS-specific issues, visit: [https://www.emailjs.com/docs/](https://www.emailjs.com/docs/)

For form issues, check the browser console for error messages.







