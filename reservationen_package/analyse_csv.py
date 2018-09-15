# python3

from patterns_and_meanings import perform_matching


def an_format(anab_str):
    return anab_str[:11]


def ab_format(anab_str):
    return anab_str[12:22]


def name(string):
    return string.split(": ")[1]


# read csv
db_list_of_lists = []
res_id_deleted = []

##
row_list = []
with open("/home/cyril/Desktop/GastroDat2/Prot.csv", "rb") as fi:
    for line in fi:
        row_list.append(line.decode("iso-8859-1"))

list_of_row_lists = []
for row in row_list:
    list_of_row_lists.append(row.split(","))
##

# process data
uniq_ana = []
uniq_ana_f = []
count = 0
matched = 0
no_match = 0

res_ids = []
guest_ids = []

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

    found, ret_dic = perform_matching(clean_row)
    if found:
        matched += 1
        if isinstance(ret_dic, dict):
            try:
                res_ids.append(ret_dic["res_id"])
            except KeyError:
                try:
                    guest_ids.append(ret_dic["guest_id"])
                except KeyError:
                    print(ret_dic)
        if count < 300:
            if isinstance(ret_dic, dict):
                # print(found, list)
                continue
        count += 1
    else:
        no_match += 1
        print(len(clean_row), clean_row)
        count += 1

print("matches: ", matched)
print("no matches: ", no_match)

print(min(guest_ids), max(guest_ids), min(res_ids), max(res_ids))


def room_index_to_nr(index):
    room_list2 = ["301", "302", "303", "304", "305", "307", "308", "309", "310",
                  "311", "314", "315", "316", "317", "300", "326", "320", "330", "340", "350", "900", "901"]
    try:
        return room_list2[index - 1]
    except IndexError:
        print("Index Error --> mail {}".format(index))
        return "99"


for i in set(uniq_ana):
    for j, ele in enumerate(uniq_ana):
        if ele == i:
            print(uniq_ana_f[j])
            break


def minimal_safe_string(st):
    return_st = st
    if return_st[0] == " ":
        return_st = return_st[1:]
    return return_st.replace("'", " ")


def safe_string(st):
    safe_st = minimal_safe_string(st)
    return safe_st
