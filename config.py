API_TOKEN: str = '6232208431:AAF9pxZtLQRrWHnnMsTO-GMHOormmEXZVLA'
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
