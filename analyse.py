# python3

import os
import sqlite3
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
# [id, zimmer, ankunft, abreise, name, erstellungsdatum]

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

    found, list = perform_matching(clean_row)
    if found:
        matched += 1
        if count < 300:
            if isinstance(list, dict):
                # print(found, list)
                continue
        count += 1
    else:
        no_match += 1
        print(len(clean_row), clean_row)
        count += 1

print("matches: ", matched)
print("no matches: ", no_match)


def room_index_to_nr(index):
    room_list = [" 300", " 301", " 302", " 303", " 304", " 304", " 305", " 306", " 307", " 308", " 309", " 310",
                 " 311", " 312", " 314", " 315", " 316", " 317", " 320", " 330", " 340", " 350"]
    room_list2 = ["300", "301", "302", "303", "304", "304", "305", "306", "307", "308", "309", "310",
                  "311", "312", "314", "315", "316", "317", "320", "330", "340", "350"]
    return room_list2[index]


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
    print(r)
"""

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
