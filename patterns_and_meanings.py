def known_patterns_and_meanings():
    pat1 = (['T', 'T', "prot_Aufen", 'i'], ['', '', '', ''])
    return [pat1]


def make_func(p):
    if p == 'T':
        return lambda x: True
    elif p == 'i':
        return lambda x: isinstance(x, int)
    elif isinstance(p, str) and len(p) > 3:
        return lambda x: x[:len(p)] == p


def test_patterns():
    test1 = ['asdf', 3, 'prot_aufen', 3]
    test2 = ['asdf', 3, 'prot_Aufen', 3]
    test3 = ['asdf', 3, 'prot_Aufen', 3.7]
    test4 = ['asdf', 3, 'prot_Aufenthalt', 3]
    for pat in known_patterns_and_meanings():
        print(process_line(pat, test1))
        print(process_line(pat, test2))
        print(process_line(pat, test3))
        print(process_line(pat, test4))


def process_line(pattern_and_meaning, test_list):
    if match_pattern(pattern_and_meaning[0], test_list):
        meaning = pattern_and_meaning[1]
        return convert_to_meaning(meaning, test_list)
    else:
        return "no match: ", test_list


def convert_to_meaning(meaning, test_list):
    return_list = []
    for m, item in zip(meaning, test_list):
        if m == '':
            return_list.append(item)
    return return_list


def match_pattern(func_list, param_list):
    match = True
    for f, p in zip(func_list, param_list):
        func = make_func(f)
        match = match and func(p)
    return match


if __name__ == "__main__":
    test_patterns()
