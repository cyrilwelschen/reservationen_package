import shutil
import os
import time
from configs import Configs
from csv2db import CsvToDb
from push_to_dropbox import upload


def do_single_run(config_file_path):
    # load configs
    cons = Configs(config_file_path)
    wd = cons.configs["working_dir"]
    prod_source_path = cons.configs["prot_file_path"]
    d_access = cons.configs["dropbox_access_token"]

    # copy Prod.dbf file
    shutil.copy2(prod_source_path, wd)
    if not os.path.exists(os.path.join(wd, "Prot.dbf")):
        # todo: write mail
        raise FileNotFoundError("Prot.dbf file not correctly copied to working directory.")

    # convert dbf to csv
    command_dbf_to_csv = "python {} {}".format(os.path.join(wd, "dbf2csv.py"), os.path.join(wd, "Prot.dbf"))
    os.system(command_dbf_to_csv)
    if not os.path.exists(os.path.join(wd, "Prot.csv")):
        # todo: write mail
        raise FileNotFoundError("Prot.csv file not correctly converted from dbf file.")

    # convert csv to db
    dbr = CsvToDb(wd)
    dbr.read_and_convert(os.path.join(wd, "Prot.csv"))
    if os.path.exists(os.path.join(wd, "gastrofull.db")):
        upload(os.path.join(wd, "gastrofull.db"), d_access)
    else:
        # todo: write mail
        raise FileNotFoundError("gastrofull.db file not correctly converted from Prot.csv file.")

    # make stamp and version files
    with open(os.path.join(wd, "upload_stamp.txt"), "w") as f:
        f.write(time.strftime("%X %d.%m.%y"))
    with open(os.path.join(wd, "version.info"), "w") as f:
        f.write("1")

    # upload files
    if os.path.exists(os.path.join(wd, "upload_stamp.txt")):
        upload(os.path.join(wd, "upload_stamp.txt"), d_access)
        upload(os.path.join(wd, "version.info"), d_access)
