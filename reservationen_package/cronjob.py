# local file ###

import os
from reservationen_package import single_run_master


if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "configs.txt")
    single_run_master.do_single_run(config_path)
