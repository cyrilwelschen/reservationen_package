import dropbox
import subprocess
from dropbox.files import WriteMode
import time
import sqlite3
import os
import smtplib

TIME_STAMP_FILE = "upload_stamp.txt"
PROT_FILE = "Prot.dbf"
GASTRO_PROT_DIR = "GastroData/"


def main():
    convert_to_csv(GASTRO_PROT_DIR + PROT_FILE)
    convert_to_db()
    make_stamp()
    upload("", "gastrofull.db")
    upload("", TIME_STAMP_FILE)


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))


def upload(local_dir, filename):
    access_token = 'dropbox_token'
    transfer_data = TransferData(access_token)

    file_from = local_dir + filename
    file_to = '/' + filename  # The full path to upload the file to, including the file name

    # API v2
    transfer_data.upload_file(file_from, file_to)


def make_stamp():
    with open(TIME_STAMP_FILE, "w") as f:
        f.write(time.strftime("%X %d.%m.%y"))


def send_mail(message):
    from_address = "example@gmail.com"
    to_address = "example@gmail.com"
    usr = "example.user"
    pwd = "PASSWORD"
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(usr, pwd)
    server.sendmail(from_address, to_address, message)
    server.quit()


def an_format(anab_str):
    return anab_str[:11]


def ab_format(anab_str):
    return anab_str[12:22]


def name(string):
    return string.split(": ")[1]


def convert_to_csv(filename):
    # call python2
    python3_command = "python dbf2csv.py {}".format(filename)  # launch your python2 script using bash
    print(python3_command)

    process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()  # receive output from the python2 script
    process.communicate()  # receive output from the python2 script
    os.system("mv {} {}".format(filename[:-4] + ".csv", PROT_FILE[:-4] + ".csv"))


def convert_to_db():
    # prepare db
    try:
        os.remove('gastrofull.db')
        print("removing existing db file")
    except OSError as e:
        print(e)
        print("Db file doesn't exist, creating it...")
    conn = sqlite3.connect('gastrofull.db')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE "reservations" ('res_id' TEXT UNIQUE, 'room_number' TEXT, 'check_in' TEXT, 'check_out' TEXT, 
        'guest_name' TEXT, 'creation_date' TEXT)''')

    # read csv

    db_list_of_lists = []
    res_id_deleted = []
    # [id, zimmer, ankunft, abreise, name, erstellungsdatum]

    ##
    row_list = []
    with open("Prot.csv", "rb") as fi:
        for line in fi:
            row_list.append(line.decode("iso-8859-1"))
        # row_list.append(f.readline().decode("iso-8859-1"))

    list_of_row_lists = []
    for row in row_list:
        list_of_row_lists.append(row.split(","))
    ##

    # process data
    for row in list_of_row_lists:
        r = []
        for i in row:
            if ";" in i:
                r += i.split(";")
            else:
                r.append(i)
        # check 1: column 5 is in 300, 301, ...
        if r[3][:len("prot_Aufen")] == "prot_Aufen":
            if r[3][-len("scht"):] == "scht":
                split_one = r[3].split(":")[1]
                split_two = split_one.split(" ")
                res_id_deleted.append(int(split_two[0]))
        try:
            if r[4] in [" 300", " 301", " 302", " 303", " 304", " 304", " 305", " 306", " 307", " 308", " 309", " 310",
                        " 311", " 312", " 314", " 315", " 316", " 317", " 320", " 330", " 340", " 350"]:
                # check 2: column 4 starts with Terminxx...
                if r[3][:len("Termin")] == "Termin":
                    # check 3: if column 7 is "AUFENTHALT" then 8 is ID 
                    if r[6] == "AUFENTHALT":
                        db_list_of_lists.append(
                            [r[7], r[4], an_format(r[5]), ab_format(r[5]), name(r[3]), r[0] + " " + r[1]])
                    # check 3.2 else column 9 is "AUFENTHALT" then 10 is ID
                    elif r[8] == "AUFENTHALT":
                        db_list_of_lists.append(
                            [r[9], r[4], an_format(r[5]), ab_format(r[5]), name(r[3]), r[0] + " " + r[1]])
        except IndexError:
            print(r)

    def minimal_safe_string(st):
        return_st = st
        if return_st[0] == " ":
            return_st = return_st[1:]
        return return_st.replace("'", " ")

    def safe_string(st):
        safe_st = minimal_safe_string(st)
        return safe_st

    for row in db_list_of_lists:
        execution_string = "INSERT OR REPLACE INTO reservations VALUES ("
        execution_string += "'" + safe_string(row[0]) + "', "
        execution_string += "'" + safe_string(row[1]) + "', "
        execution_string += "'" + safe_string(row[2]) + "', "
        execution_string += "'" + safe_string(row[3]) + "', "
        execution_string += "'" + safe_string(row[4]) + "', "
        execution_string += "'" + safe_string(row[5]) + "')"
        try:
            if int(row[0]) in res_id_deleted:
                continue
            else:
                exec_st = execution_string.encode("utf-8")
                if row[4][:2] == "Sw":
                    print(exec_st)
                c.execute(exec_st.decode("utf-8"))
        except sqlite3.OperationalError as e:
            print(execution_string)
            raise e

    conn.commit()
    c.execute("Select * from reservations")
    print(c.fetchone())
    conn.close()


if __name__ == '__main__':
    main()
