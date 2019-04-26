from sys import *
import schedule
import hashlib
import time
import os
import urllib2
import smtplib
import schedule
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
argc = 4

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout = 1)
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
        Please find attached file as log of deleted duplicate files in mac
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

        s.login(mail_from, 'mailsender')

        text = msg.as_string()

        s.sendmail(mail_from, mail_to, text)
        s.quit()

        print('Log file successfully sent')

    except Exception as err:
        print(err)

def DupLog(dup_files):
    srcdir = 'logs'
    if not os.path.isdir(srcdir):
        print('No such a directory ', srcdir)
        print('Creating a directory : %s'%srcdir)

        try:
            os.mkdir(srcdir)
        except Exception as err:
            print('ERROR: ', err)

    if os.path.isdir(srcdir):
        separator = '-' * 80
        log_path = os.path.join(srcdir, 'Duplicate files Log %s.log'%(time.strftime("%a %d-%m-%Y %H-%M-%S")))
        fd = open(log_path, 'w')
        fd.write(separator + '\n')
        fd.write('Duplicate files Log %s' %(time.ctime()) + '\n')
        fd.write(separator + '\n')

    for element in dup_files:
        fd.write(element + '\n')

    return log_path

def Checksum(path, block = 1024):
    hasher = hashlib.md5()
    fd = open(path, 'rb')
    buffer = fd.read(block)

    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = fd.read(block)
    return hasher.hexdigest()

def DuplicateDetector(path):
    if not os.path.isabs(path):
        srcdir = os.path.abspath(path)
    else:
        srcdir = path

    if not os.path.isdir(srcdir):
        print('No such a directory', srcdir)
        exit()
    else:
        duplicate_files = {}

        for dirname,sub_dir_list,files_list in os.walk(srcdir):
            for file in files_list:
                file_path = os.path.join(dirname, file)
                file_checksum = Checksum(file_path)

                if file_checksum in duplicate_files:
                    duplicate_files[file_checksum].append(file_path)
                else:
                    duplicate_files[file_checksum] = [file_path]
        return duplicate_files

def DeleteDuplicate(duplicate_files):
    list_dup_files = []
    print('printing duplicate files %s'%duplicate_files)
    results = list(filter(lambda x : len(x) > 1, duplicate_files.values()))
    if len(results) > 0:
        icnt = 0
        print('Duplicate files Found')
        for duplicate in results:
            for dup in duplicate:
                icnt += 1
                if icnt >= 2:
                    print('\t\t%s' % dup)
                    list_dup_files.append(dup)
                    # os.remove(dup)

            icnt = 0
    else:
        print('No Duplicate files Found')
    return list_dup_files

def ScheduledMethod():
    try:
        duplicate_files = DuplicateDetector(argv[1])
        dup_files_path_list = DeleteDuplicate(duplicate_files)
        logfile = DupLog(dup_files_path_list)
        MailSender(logfile, time.ctime(), argv[3])
    except Exception as e:
        print('Exception: ', e)


def main():

    if not len(argv) == argc:
        print('Arguements length should be 4')
        exit()

    else:
        schedule.every(int(argv[2])).minutes.do(ScheduledMethod)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()