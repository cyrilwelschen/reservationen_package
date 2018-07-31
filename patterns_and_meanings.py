def test_known_patterns_and_meanings():
    pat1 = (['T', 'T', "prot_Aufen", 'i'], ['', '', '', ''])
    return [pat1]


def test_patterns():
    test1 = ['asdf', 3, 'prot_aufen', 3]
    test2 = ['asdf', 3, 'prot_Aufen', 3]
    test3 = ['asdf', 3, 'prot_Aufen', 3.7]
    test4 = ['asdf', 3, 'prot_Aufenthalt', 3]
    for pat in test_known_patterns_and_meanings():
        print(process_line(pat, test1))
        print(process_line(pat, test2))
        print(process_line(pat, test3))
        print(process_line(pat, test4))


def known_patterns_and_meanings():
    # pat1 = ([20161110, '16:59:17', '0.00', 'Termin geändert: Welschen', 308, ' 11.11.2016-13.11.2016', 'AUFENTHALT', 12, 7413, 7, 'RECEPTION', 2], [])
    pat1 = (['i', 'T', 'T', 'Termin ge', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], ['']*12)
    # igo1 = ([20161110, '10:41:45', '', 'prot_Zimmerdaten eingestellt', 'ZIMMERDATEN', 3, 0, 21, '', 0])
    ign1 = (['i', 'T', 'T', 'prot_Zimmerdaten eingestellt', 'ZIMMERDATEN', 'i', 'i', 'i', 'T', 'i'], [False])
    # ign2 = ([20170129, '18:33:14', '0.00', 'Termineinsicht: Welschen', 309, ' 10.11.2016-11.11.2016', 'AUFENTHALT', 10, 7413, 8, 'RECEPTION', 2])
    ign2 = (['i', 'T', 'T', 'Termineinsicht', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign3 = ([20170204, '18:53:20', '0.00', 'Dokument erstellt: Rechnung (D)', 'DOKUMENT', 143, 1793, 0, 'RECEPTION', 2])
    ign3 = (['i', 'T', 'T', 'Dokument erstellt', 'DOKUMENT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign4 = ([20170210, '09:36:02', '0.00', 'Terminstatus: CheckOut', 310, ' 03.02.2017-10.02.2017', 'AUFENTHALT', 146, 4187, 9, 'RECEPTION', 2], [False])
    ign4 = (['i', 'T', 'T', 'Terminstatus: CheckOut', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign5 = ([20170210, '09:36:21', '0.00', 'Terminstatus: Belegung', 300, ' 10.02.2017-15.02.2017', 'AUFENTHALT', 231, 8076, 15, 'RECEPTION', 2], [False])
    ign5 = (['i', 'T', 'T', 'Terminstatus: Belegung', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign6 = (, [False])
    return [pat1, ign1, ign2, ign3, ign4, ign5]


def make_func(p):
    if p == 'T':
        return lambda x: True
    elif p == 'i':
        return lambda x: isinstance(x, int)
    elif isinstance(p, str) and len(p) > 3:
        return lambda x: x[:len(p)] == p


def perform_matching(item_list):
    found, li = False, []
    for pat in known_patterns_and_meanings():
        if len(pat[0]) == len(item_list):
            f, l = process_line(pat, item_list)
            if f == True:
                found = True
                li = l
    return found, li


def process_line(pattern_and_meaning, item_list):
    if match_pattern_one_by_one(pattern_and_meaning[0], item_list):
        meaning = pattern_and_meaning[1]
        if meaning:
            return True, convert_to_meaning(meaning, item_list)
        else:
            return True, []
    else:
        # todo: send mail with no-match
        # return "no match: ", item_list
        return False, []


def convert_to_meaning(meaning, item_list):
    return_list = []
    for m, item in zip(meaning, item_list):
        if m == '':
            return_list.append(item)
    return return_list


def match_pattern_one_by_one(func_list, param_list):
    match = True
    for f, p in zip(func_list, param_list):
        func = make_func(f)
        match = match and func(p)
    return match


if __name__ == "__main__":
    test_patterns()
