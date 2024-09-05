#go over to out gmail account and setup 2 factor authentication
#   generate app passwd
#create a function to send email
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'vs142303@gmail.com'
email_password = 'pcms gigf orrj sf'

email_reciver = 'sapevif546@daypey.com'

subject = 'dont forget to keep coding'

body = """
when you watch a video keep writing with it
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,  email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_bytes())

