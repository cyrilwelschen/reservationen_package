# python3

from patterns_and_meanings import perform_matching
from db_util import DbUtil


CREATE_RES_TABLE = '''CREATE TABLE "reservations" ('res_id' TEXT UNIQUE, 'room_number' TEXT, 'check_in' TEXT,
                                'check_out' TEXT, 'guest_name' TEXT, 'creation_date' TEXT, 'guest_id' TEXT)'''
CREATE_GUEST_TABLE = '''CREATE TABLE "guests" ('res_id' TEXT UNIQUE, 'room_number' TEXT, 'check_in' TEXT,
                                'check_out' TEXT, 'guest_name' TEXT, 'creation_date' TEXT)'''
RES_DB = 'gastrofull.db'
GUEST_DB = 'guest.db'


class CsvToDb:
    def __init__(self):
        self.db = DbUtil(RES_DB)
        self.db.create_table(CREATE_RES_TABLE)
        self.db_guest = DbUtil(GUEST_DB)
        self.db_guest.create_table(CREATE_GUEST_TABLE)

    @staticmethod
    def reformat_date(date):
        return date[-2:]+"."+date[-4:-2]+"."+date[:4]

    def handle_create(self, dic_mean):
        execution_string = "INSERT OR REPLACE INTO reservations VALUES ("
        execution_string += "'" + dic_mean["res_id"] + "', "
        execution_string += "'" + self.room_index_to_nr(dic_mean["room_index"]) + "', "
        execution_string += "'" + self.reformat_date(dic_mean["check_in"]) + "', "
        execution_string += "'" + self.reformat_date(dic_mean["check_out"]) + "', "
        execution_string += "'" + dic_mean["guest_id"] + "', "
        execution_string += "'" + "tbd" + "')"
        self.db.execute_on_db(execution_string)

    def handle_update(self, dic_mean):
        pass

    def handle_delete(self, dic_mean):
        pass

    def handle_meaning(self, dic_meaning):
        print(dic_meaning)
        stat = dic_meaning["status"]
        if stat == "create":
            self.handle_create(dic_meaning)
        elif stat == "update":
            self.handle_update(dic_meaning)
        elif stat == "delete":
            self.handle_delete(dic_meaning)
        else:
            pass

    @staticmethod
    def room_index_to_nr(index):
        # room_list = [" 300", " 301", " 302", " 303", " 304", " 304", " 305", " 306", " 307", " 308", " 309", " 310",
        #              " 311", " 312", " 314", " 315", " 316", " 317", " 320", " 330", " 340", " 350"]
        room_list2 = ["300", "301", "302", "303", "304", "304", "305", "306", "307", "308", "309", "310",
                      "311", "312", "314", "315", "316", "317", "320", "330", "340", "350"]
        return room_list2[index]

    def read_and_convert(self):
        li = self.read()
        self.convert(li)

    @staticmethod
    def read():
        row_list = []
        with open("/home/cyril/Desktop/GastroDat2/Prot.csv", "rb") as fi:
            for line in fi:
                row_list.append(line.decode("iso-8859-1"))
        list_of_row_lists = []
        for row in row_list:
            list_of_row_lists.append(row.split(","))
        return list_of_row_lists

    def convert(self, list_of_row_lists):
        count = 0
        for row in list_of_row_lists:
            r = []
            for i in row:
                if ";" in i:
                    r += i.split(";")
                else:
                    r.append(i)
            clean_row = []
            for i in r:
                try:
                    clean_row.append(int(i))
                except ValueError:
                    clean_row.append(i)
            found, dic_mean = perform_matching(clean_row)
            if found:
                if count < 300:
                    if isinstance(dic_mean, dict):
                        self.handle_meaning(dic_mean)
                count += 1
            else:
                # todo: send mail (with print statement) when pattern not found
                print("Couldn't find pattern corresponding to {}".format(clean_row))
        self.db.close_db()


if __name__ == "__main__":
    dbc = CsvToDb()
    dbc.read_and_convert()

"""
# remember which reservaiton IDs were deleted
if r[3][:len("prot_Aufen")] == "prot_Aufen":
    if r[3][-len("scht"):] == "scht":
        split_one = r[3].split(":")[1]
        split_two = split_one.split(" ")
        res_id_deleted.append(int(split_two[0]))
# check 1: column 5 is in 300, 301, ...
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
    else:
        uniq_ana.append(r[3][:10])
        uniq_ana_f.append(r[3])
except IndexError:
"""

