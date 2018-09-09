import shutil
import os
from configs import Configs
from csv2db import CsvToDb

# load configs
cons = Configs("/home/cyril/Desktop/ResAppWorkingFolder/configs.txt")
wd = cons.configs["working_dir"]
prod_source_path = cons.configs["prot_file_path"]

# copy Prod.dbf file
shutil.copy2(prod_source_path, wd)
if not os.path.exists(os.path.join(wd, "Prot.dbf")):
    # write email
    raise FileNotFoundError("Prot.dbf file not correctly copied to working directory.")

# convert dbf to csv
command_dbf_to_csv = "python {} {}".format(os.path.join(wd, "dbf2csv.py"), os.path.join(wd, "Prot.dbf"))
print(command_dbf_to_csv)
os.system(command_dbf_to_csv)
if not os.path.exists(os.path.join(wd, "Prot.csv")):
    # write email
    raise FileNotFoundError("Prot.csv file not correctly converted from dbf file.")

# convert csv to db
dbr = CsvToDb(wd)
dbr.read_and_convert(os.path.join(wd, "Prot.csv"))
if not os.path.exists(os.path.join(wd, "gastrofull.db")):
    # write email
    raise FileNotFoundError("gastrofull.db file not correctly converted from Prot.csv file.")
