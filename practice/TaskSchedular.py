import schedule
import time
import datetime

def minutes():
    print('minute', datetime.datetime.now())

def sunday():
    print('sunday', datetime.datetime.now())

def day():
    print('day', datetime.datetime.now())

def main():
    print('main', datetime.datetime.now())

    schedule.every(1).minutes.do(minutes)
    schedule.every().hour.do(minutes)
    schedule.every().day.at('16:16:56').do(day)
    schedule.every().sunday.at('16:15').do(sunday)
    schedule.every().saturday.do(minutes)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()