# loacal file ###

import os
from crontab import CronTab
# from reservation_package.configs import Configs
from configs import Configs

if __name__ == "__main__":
    con = Configs("configs.txt")
    my_cron = CronTab(user=True)
    command = "python3 {}".format(os.path.join(con.configs["working_dir"], "cronjob.py"))
    job = my_cron.new(command=command, comment="reservation app cron job")
    job.hour.every(1)
    my_cron.write()
