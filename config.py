API_TOKEN: str = '7617694393:AAEVtZJd_dB-O0Aqo-94bStgiWcSwSmwf9w'
STARS_AMOUNT: int = 1

MESSAGES = {
    'payment_success': (
        "🎉 <b>Payment successful!</b>\n"
        "💲 <b>Amount:</b> {amount}⭐️\n"
        "🆔 <b>Transaction ID:</b> <code>{transaction_id}</code>"
    ),
    'refund_success': "✅ <b>Payment has been successfully refunded!</b>",
    'refund_fail': "❌ <b>Failed to refund payment</b>",
    'invalid_command': ("❌ <b>Please use format:</b> /refund '&lt;transaction_id&gt;'\n"
                        "Example: <code>/refund ABC123XYZ</code>")
}
