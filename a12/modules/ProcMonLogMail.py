from sys import argv
import os
import time
import psutil
import urllib2
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import socket

argc = 3

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout = 2)
        return True
    except Exception as err:
        print(err)
        return False

def MailSender(filename, time, mail_to):
    try:
        mail_from = "pratikbali01@gmail.com"
        msg = MIMEMultipart()

        msg['from'] = mail_from
        msg['to'] = mail_to
        msg['Subject'] = "Process log generated at %s" %time

        body = """
        Hello %s
        Welcome to Hydrogen
        Please find attached file as log of running process in mac
        log file is created at %s

        This is Auto Generated Mail \n\n"""%(mail_to, time)

        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, 'rb')

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename = %s"%filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        s.login(mail_from, '--')

        text = msg.as_string()

        s.sendmail(mail_from, mail_to, text)
        s.quit()

        print('Log file successfully sent')

    except Exception as err:
        print(err)

def ProcessDisplay(path, mail_to):
    listProcess = []
    srcdir = path

    if not os.path.isdir(srcdir):
        print('No such a directory', srcdir)
        try:
            os.mkdir(srcdir)
        except Exception as err:
            print('ERROR: ', err)

    if os.path.isdir(srcdir):
        separator = '-' * 80
        log_path = os.path.join(srcdir, 'ProcessLog %s.log'%(time.strftime("%a %d-%m-%Y %H-%M-%S")))
        fd = open(log_path, 'w')
        fd.write(separator + '\n')
        fd.write('Process Log %s' %(time.ctime()) + '\n')
        fd.write(separator + '\n')

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=["pid", "name", "username"])
                vms = proc.memory_info().vms / (1024 * 1024)
                pinfo['vms'] = vms
                listProcess.append(pinfo)
            except Exception as e:
                print(e)

        for element in listProcess:
            fd.write('%s \n' % element)

        print('Log file generated at %s ' % log_path)

        if is_connected():
            start_time = time.time()
            print(time.ctime())
            MailSender(log_path, time.ctime(), mail_to)
            print(time.ctime())
            end_time = time.time()

            print('Took %s seconds to mail' % (end_time - start_time))
        else:
            print('No internet connection')

def main():
    print('hi')
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    try:
        ProcessDisplay(argv[1], argv[2])
    except Exception as e:
        print('ERROR: Exception occurred : ', e)

if __name__ == '__main__':
    main()
