from sys import *
import time
import smtplib
import urllib2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout = 1)
        return True
    except urllib2.URLError as err:
        return False
    except Exception as e:
        return False

def MailSender(username, password):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()

        server.login(username, password)

        to = 'cnpratik@gmail.com'
        text = """Hello from Prince Hydrogen"""

        message = MIMEMultipart("alternative")
        message["Subject"] = "send mail test"
        message["From"] = username
        message["To"] = to

        part1 = MIMEText(text, "plain")

        message.attach(part1)

        server.sendmail(username, to, message.as_string())

    except Exception as e:
        print('ERROR:', e)

    else:
        print('mail sent')

def getEncryptedPassword():
    return ''

def main():
    print('in main')

    try:
        if is_connected():
            username = 'pratikbali01@gmail.com'
            password = getEncryptedPassword()
            MailSender(username, password)
        else:
            print('No internet connection')
    except Exception as e:
        print('EXCEPTION:', e)

if __name__ == '__main__':
    main()
