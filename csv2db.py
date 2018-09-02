# python3

from patterns_and_meanings import perform_matching
from db_util import DbUtil


CREATE_RES_TABLE = '''CREATE TABLE "reservations" ('res_id' TEXT UNIQUE, 'room_number' TEXT, 'check_in' TEXT,
                                'check_out' TEXT, 'guest_name' TEXT, 'guest_id' TEXT)'''
CREATE_GUEST_TABLE = '''CREATE TABLE "guests" ('guest_id' TEXT UNIQUE, 'guest_name' TEXT)'''
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

    def try_get_guest_name(self, guest_id):
        self.db_guest.c.execute("SELECT guest_name FROM guests WHERE guest_id=?", (guest_id,))
        try:
            return self.db_guest.c.fetchone()[0]
        except TypeError:
            print("guest not found in db --> mail. guest_id: {}".format(guest_id))
            return "not_found"

    def handle_create(self, dic_mean):
        execution_string = "INSERT OR REPLACE INTO reservations VALUES ("
        execution_string += "'" + str(dic_mean["res_id"]) + "', "
        execution_string += "'" + self.room_index_to_nr(dic_mean["room_index"]) + "', "
        execution_string += "'" + self.reformat_date(dic_mean["check_in"]) + "', "
        execution_string += "'" + self.reformat_date(dic_mean["check_out"]) + "', "
        execution_string += "'" + self.try_get_guest_name(dic_mean["guest_id"]) + "', "
        execution_string += "'" + str(dic_mean["guest_id"]) + "')"
        self.db.execute_on_db(execution_string)

    def handle_delete(self, dic_mean):
        execution_string = "DELETE FROM reservations WHERE res_id=?"
        self.db.c.execute(execution_string, (dic_mean["res_id"],))

    @staticmethod
    def safe_name(name):
        return name.replace("'", '"')

    def handle_guest(self, dic_mean):
        execution_string = "INSERT OR REPLACE INTO guests VALUES ("
        execution_string += "'" + str(dic_mean["guest_id"]) + "', "
        execution_string += "'" + self.safe_name(dic_mean["g_name"]) + "')"
        self.db_guest.c.execute(execution_string)
        # self.db_guest.conn.commit()

    def handle_meaning(self, dic_meaning):
        # print(dic_meaning)
        stat = dic_meaning["status"]
        if stat == "create":
            self.handle_create(dic_meaning)
        elif stat == "update":
            self.handle_create(dic_meaning)
        elif stat == "delete":
            self.handle_delete(dic_meaning)
        elif stat == "guest":
            self.handle_guest(dic_meaning)
        else:
            # todo: implement mail
            # raise KeyError("unknown status {}".format(stat))
            pass

    @staticmethod
    def room_index_to_nr(index):
        # room_list = [" 300", " 301", " 302", " 303", " 304", " 304", " 305", " 306", " 307", " 308", " 309", " 310",
        #              " 311", " 312", " 314", " 315", " 316", " 317", " 320", " 330", " 340", " 350"]
        room_list2 = ["301", "302", "303", "304", "305", "307", "308", "309", "310",
                      "311", "314", "315", "316", "317", "300", "326", "320", "330", "340", "350", "900", "901"]
        try:
            return room_list2[index - 1]
        except IndexError:
            print("Index Error --> mail {}".format(index))
            return "99"

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
        c, u, g, d, unf = 0, 0, 0, 0, 0
        room_ids = []
        res_ids = []
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
                if isinstance(dic_mean, dict):
                    self.handle_meaning(dic_mean)
                    try:
                        room_ids.append(dic_mean["room_index"])
                        if dic_mean["room_index"] in [16]:
                            print(dic_mean["original_list"])
                    except KeyError:
                        continue
                    try:
                        res_ids.append(dic_mean["res_id"])
                    except KeyError:
                        continue
                    stat = dic_mean["status"]
                    if stat == "update":
                        u += 1
                    elif stat == "create":
                        c += 1
                    elif stat == "guest":
                        g += 1
                    elif stat == "delete":
                        d += 1
                    else:
                        unf += 1
            else:
                # todo: send mail (with print statement) when pattern not found
                print("Couldn't find pattern corresponding to {}".format(clean_row))
        print(c, u, g, d, unf)
        print(set(room_ids))
        print(len(set(res_ids)))
        self.db.conn.commit()
        self.db_guest.conn.commit()
        self.db.close_db()
        self.db_guest.close_db()
        print("finished")


if __name__ == "__main__":
    dbr = CsvToDb()
    dbr.read_and_convert()

