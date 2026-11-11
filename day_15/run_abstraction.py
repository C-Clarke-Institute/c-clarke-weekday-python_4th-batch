from day_15.abstraction import SMSNotifier, EmailNotifier, Notifier, WhatsappNotifier


def send_message(message: str, notifier: Notifier):
    notifier.send(message)



sms_notifier = SMSNotifier()
email_notifier = EmailNotifier()
message_input = input("Enter your message to send")
send_message(message_input, sms_notifier)
send_message(message_input, email_notifier)

whatsapp_notifier = WhatsappNotifier()

send_message(message_input, whatsapp_notifier)