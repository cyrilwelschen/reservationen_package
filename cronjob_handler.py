import os
from configs import Configs
from crontab import CronTab


if __name__ == "__main__":
    con = Configs("/home/cyril/Desktop/ResAppWorkingFolder/configs.txt")
    my_cron = CronTab(user=True)
    command = "python3 {}".format(os.path.join(con.configs["working_dir"], "test_cron_non_package.py"))
    print(command)
    test_job = my_cron.new(command=command, comment="reservation cron job")
    # test_job.minute.every(2)
    my_cron.write()
    for job in my_cron:
        print(job.is_enabled(), job)
