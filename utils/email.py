import smtplib
from email.mime.multipart import MIMEMultipart  # pip install email-to
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from time import sleep
from email.message import EmailMessage
import config

def format_message_to_html(message):
    message_html = f"""
    <!DOCTYPE html>
    <html>
    <body>

    <p>{message}</p>

    </body>
    </html>
    """
    return message_html


def sendmail(email_to, message, title):
    me = config.import_config('DEFAULT', 'my_email')
    password = config.import_config('DEFAULT', 'password')
    try:
        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = title
        msg['From'] = me
        msg['To'] = email_to

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        sleep(3)
        server.login(me, password)
        sleep(3)
        response = server.send_message(msg)
        server.quit()
        return response
    except Exception as err:
        return str(err)



def sendmail_with_attachments(email_to, title, message, attachment):
    me = config.import_config('DEFAULT', 'my_email')
    password = config.import_config('DEFAULT', 'password')

    message_html = format_message_to_html(message)

    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = me
        msg['To'] = email_to
        message_html_2 = MIMEText(message_html, 'html')
        msg.attach(message_html_2)

        # open the file in bynary
        binary_pdf = open(attachment, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=attachment)
        payload.set_payload((binary_pdf).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=attachment)
        msg.attach(payload)

        #mail = smtplib.SMTP('smtp.gmail.com', 465)
        mail = smtplib.SMTP_SSL('smtp.gmail.com')
        sleep(3)

        #mail.ehlo()

        #mail.starttls()

        mail.login(me, password)
        sleep(3)
        response = mail.sendmail(me, email_to, msg.as_string())
        mail.quit()
        return response
    except Exception as err:
        return str(err)
