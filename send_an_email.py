import smtplib, ssl

port = 465 # for SSL
sender_email = '' # email
sender_password = '' # password

def send_reminder(receiver_email, subject, body):
    message =  "Subject: " + subject + "\n\n" + body
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

send_reminder(sender_email, "Reminder", "This is a reminder email.")

# This method is not very secure, so don't use main email account