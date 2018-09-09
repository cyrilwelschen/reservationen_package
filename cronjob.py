# local file ###

import os
# from reservationen_package import single_run_master
import single_run_master


if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    single_run_master.do_single_run(current_path)
