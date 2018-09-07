from crontab import CronTab
import datetime


def write_cron_test():
    with open('/home/cyril/Desktop/dateInfo.txt', 'a') as f:
        f.write('\n' + str(datetime.datetime.now()))


if __name__ == "__main__":
    import os
    os.system("python3 ./test_cronjob_handler.py")
    my_cron = CronTab('cyril')
    test_job = my_cron.new(command="python3 test_cronjob_handler.py ")
    test_job.minute.every(1)
    my_cron.write()
    for job in my_cron:
        print(job)
