from email.message import EmailMessage
import ssl
import smtplib

def send_email(email_sender, email_password, email_receiver, subject, body):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_bytes())

# Your credentials and email details
email_sender = 'vs142303@gmail.com'
email_password = 'bcgy prbo ljpb wvkq'  # Use the app-specific password here
email_receiver = 'sapevif546@daypey.com'

subject = 'Don’t forget to keep coding'
body = """
When you watch a video, keep writing with it.
"""

# Send the email
send_email(email_sender, email_password, email_receiver, subject, body)
