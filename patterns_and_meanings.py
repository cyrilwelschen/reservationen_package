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
    # pat3 = ([20170416, '19:16:17', '', 'prot_Aufenthalt Nr:777 20170513-20170513:Permbhusri Bambi gelöscht', 'AUFENT_LOESC', 777, 8407, 9, 'RECEPTION', 2], 10*[''])
    pat3 = (['i', 'T', 'T', 'prot_Aufenthalt', 'AUFENT_LOESC', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat2 = ([20170402, '11:55:55', '', 'prot_Aufenthalt geändert Nr:637 ZNr: 7           20170331-20170401', 'AUFENTHALT', 637, 0, 7, 'RECEPTION', 2], 10*[''])
    pat2 = (['i', 'T', 'T', 'prot_Aufenthalt ge', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat4 = ([20170502, '18:22:11', '', 'prot_Aufenthalt neu Nr:846 ZNr: 5    Termin gerade reserviert ... 20170505-20170505', 'RESERVIERUNG', 846, 8463, 5, 'RECEPTION', 2], 10*[''])
    pat4 = (['i', 'T', 'T', 'prot_Aufenthalt neu', 'RESERVIERUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat5 = ([20170806, '21:31:36', '', 'prot_Aufenthalt neu Nr:1616 ZNr: 14  \x98\x05r\x02', '\x93bÊF Termin gerade reserviert ... 20170825-20170825', 'RESERVIERUNG', 1616, 9095, 14, 'RECEPTION', 2], 11*[''])
    pat5 = (['i', 'T', 'T', 'prot_Aufenthalt neu', 'T', 'RESERVIERUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], 11*[''])
    # pat8 = ([20180512, ' 8:08:21', '', '"prot_Aufenthalt neu Nr:3066 ZNr: 2   ', '\x92\x99wã\x17 Termin gerade reserviert ... 20180514-20180514"', 'RESERVIERUNG', 3066, 10047, 2, 'RECEPTION', 2], 11*[''])
    pat8 = (['i', 'T', 'T', '"prot_Aufenthalt neu', 'T', 'RESERVIERUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], 11*[''])
    # pat9 = ([20180415, '11:15:17', '', 'prot_Aufenthalt neu Nr:2880 ZNr: 4   l\x91Xtn. Termin gerade reserviert ... 20190216-20190222', 'ANGEBOT', 2880, 1597, 4, 'RECEPTION', 2], 10*[''])
    pat9 = (['i', 'T', 'T', 'prot_Aufenthalt neu', 'ANGEBOT', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat10 = ([20180307, ' 8:00:07', '', '"prot_Aufenthalt neu Nr:2596 ZNr: 9   l\x91¾s£\r Termin gerade reserviert ... 20180403-20180407"', 'ANGEBOT', 2596, 7262, 9, 'RECEPTION', 2], 10*[''])
    pat10 = (['i', 'T', 'T', '"prot_Aufenthalt neu', 'ANGEBOT', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat11 = ([20180306, '18:34:45', '', '"prot_Aufenthalt neu Nr:2595 ZNr: 11  l\x91¾s£\r Termin gerade reserviert ... 20190223-20190301"', 'RESERVIERUNG', 2595, 8099, 11, 'RECEPTION', 2], 10*[''])
    pat11 = (['i', 'T', 'T', '"prot_Aufenthalt neu', 'RESERVIERUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat1 = ([20161110, '16:59:17', '0.00', 'Termin geändert: Welschen', 308, ' 11.11.2016-13.11.2016', 'AUFENTHALT', 12, 7413, 7, 'RECEPTION', 2], [])
    pat1 = (['i', 'T', 'T', 'Termin ge', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], ['']*12)
    # pat6 = ([20171226, '14:59:58'    # pat11 = (, *['']), '0.00', 'Termin geändert: Walla', 315, ' 23.12.2017-27.12.2017', ' 1 Pax', ' F', 'AUFENTHALT', 1918, 9313, 12, 'RECEPTION', 2], 14*[''])
    pat6 = (['i', 'T', 'T', 'Termin ge', 'i', 'T', 'T', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], 14*[''])
    # pat7 = ([20180507, ' 9:08:34', '', 'prot_Zimmertausch Nr:2482  ZNr: 14', 'AUFENTHALT', 2482, 0, 14, 'RECEPTION', 2], 10*[''])
    pat7 = (['i', 'T', 'T', 'prot_Zimmertausch', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat12 = ([20180510, '13:44:27', '', '"prot_Aufenthalt neu Nr:3057 ZNr: 19  ', '\x92\x99wï\x11 Termin gerade reserviert ... 20190323-20190329"', 'ANGEBOT', 3057, 8048, 19, 'RECEPTION', 2], 11*[''])
    pat12 = (['i', 'T', 'T', '"prot_Aufenthalt neu', 'T', 'ANGEBOT', 'i', 'i', 'i', 'RECEPTION', 'i'], 11*[''])
    # pat13 = ([20180317, ' 9:20:44', '', 'prot_Aufenthalt neu Nr:2678 ZNr: 20   Termin gerade reserviert ... 20190309-20190315', 'BELEGUNG', 2678, 2295, 20, 'RECEPTION', 2], 10*[''])
    pat13 = (['i', 'T', 'T', 'prot_Aufenthalt neu', 'BELEGUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # --------------------
    # pat14 = ([20180122, '17:43:24', '', '"prot_Aufenthalt neu Nr:2334 ZNr: 10  l\x91/uä\n'], 4*[''])
    pat14 = (['i', 'T', 'T', '"prot_Aufenthalt neu'], 4*[''])
    # pat15 = ([20180109, '15:50:02', '', 'prot_Aufenthalt neu Nr:2230 ZNr: 5   ¬ë\x19 Termin gerade reserviert ... 20180217-20180223', '?', 2230, 9514, 5, 'RECEPTION', 2], 10*[''])
    pat15 = (['i', 'T', 'T', 'prot_Aufenthalt neu', 'T', 'i', 'i', 'i', 'RECEPTION', 'i'], 10*[''])
    # pat16 = ([' Termin gerade reserviert ... 20180217-20180223"', 'RESERVIERUNG', 2461, 9652, 5, 'RECEPTION', 2], 7*[''])
    pat16 = (['T', 'RESERVIERUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], 7*[''])
    # pat17 = (['& Termin gerade reserviert ... 20180217-20180223"', 'RESERVIERUNG', 2461, 9652, 5, 'RECEPTION', 2], 7*[''])
    pat17 = (['T', 'ANGEBOT', 'i', 'i', 'i', 'RECEPTION', 'i'], 7*[''])
    # pat18 = ([20170515, '08:23:42', '0.00', '"Termin geändert: Portax', ' s.r.o', 301, ' 13.05.2017-15.05.2017"', 'AUFENTHALT', 631, 8295, 1, 'RECEPTION', 2], 13*[''])
    pat18 = (['i', 'T', 'T', '"Termin geändert', 'T', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], 13*[''])
    # pat19 = ([20170718, '17:58:26', '0.00', 'Termin gelöscht: Kraus Niklas', '  [301]', ' 24.02.2018-03.03.2018', 'AUFENT_LOESC', 568, 3635, 0, 'RECEPTION', 2], 12*[''])
    pat19 = (['i', 'T', 'T', 'Termin gelöscht', 'T', 'T', 'AUFENT_LOESC', 'i', 'i', 'i', 'RECEPTION', 'i'], 12*[''])
    # pat20 = (, *[''])
    # pat21 = (, *[''])
    # pat22 = (, *[''])
    # pat23 = (, *[''])
    # pat24 = (, *[''])

    # ----------------------------------------------------- ignore ----------------------------------------------------
    # Termin
    # ign2 = ([20170129, '18:33:14', '0.00', 'Termineinsicht: Welschen', 309, ' 10.11.2016-11.11.2016', 'AUFENTHALT', 10, 7413, 8, 'RECEPTION', 2])
    ign2 = (['i', 'T', 'T', 'Termineinsicht', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign4 = ([20170210, '09:36:02', '0.00', 'Terminstatus: CheckOut', 310, ' 03.02.2017-10.02.2017', 'AUFENTHALT', 146, 4187, 9, 'RECEPTION', 2], [False])
    ign4 = (['i', 'T', 'T', 'Terminstatus: CheckOut', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign5 = ([20170210, '09:36:21', '0.00', 'Terminstatus: Belegung', 300, ' 10.02.2017-15.02.2017', 'AUFENTHALT', 231, 8076, 15, 'RECEPTION', 2], [False])
    ign5 = (['i', 'T', 'T', 'Terminstatus: Belegung', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign21 = ([20180507, '15:02:59', '0.00', 'Terminstatus: Reservierung', 350, ' 14.08.2018-19.08.2018', 'AUFENTHALT', 3022, 8799, 20, 'RECEPTION', 2], [False])
    ign21 = (['i', 'T', 'T', 'Terminstatus: Reservierung', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign25 = ([20180125, '17:18:14', '0.00', 'Terminstatus: Angebot', 350, ' 01.10.2018-31.10.2018', 'AUFENTHALT', 2354, 6789, 20, 'RECEPTION', 2], [False])
    ign25 = (['i', 'T', 'T', 'Terminstatus: Angebot', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign10 = ([20170318, '17:40:55', '0.00', 'Termin-Info geändert: 1x glutenfreies brot!! -> 1x glutenfreies Brot!!', 'AUFENTHALT', 368, 995, 2, 'RECEPTION', 2], [False])
    ign10 = (['i', 'T', 'T', 'Termin-Info ge', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign15 = ([20180305, '18:21:17', '0.00', '"Termin-Info geändert: möchten 2 EZ', ' letzte Nacht nur... -> möchten 9.3.- 13.3. und 3 EZ +..."', 'AUFENTHALT', 2567, 4406, 3, 'RECEPTION', 2], [False])
    ign15 = (['i', 'T', 'T', '"Termin-Info ge', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign16 = ([20180323, '14:13:55', '0.00', '"Termin-Info geändert:  -> ""non-ref"""', 'AUFENTHALT', 698, 5273, 19, 'RECEPTION', 2], [False])
    ign16 = (['i', 'T', 'T', '"Termin-Info ge', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign22 = ([20180119, '09:15:03', '0.00', '"Termin-Info geändert: Ankunft 11:15', ' abholen!! -> Ankunft 10:15', ' abholen!!"', 'AUFENTHALT', 1863, 9274, 4, 'RECEPTION', 2], [False])
    ign22 = (['i', 'T', 'T', '"Termin-Info ge', 'T', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign34 = ([20180329, '08:04:30', '0.00', '"Termin-Info geändert: Extra-Bett', ' Kind ? -> KK belastet 50%', ' Extra-Bett', ' K..."', 'AUFENTHALT', 2742, 9828, 6, 'RECEPTION', 2], [False])
    ign34 = (['i', 'T', 'T', '"Termin-Info ge', 'T', 'T', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign7 = ([20170216, '21:27:25', '', 'prot_fkt: LeistungNr.: 364 Tourismustaxe 1 Pers. aufgebucht', 'LEISTUNG', 356, 3635, 10, 'RECEPTION', 2], [False])
    ign7 = (['i', 'T', 'T', 'prot_fkt: LeistungNr.:', 'LEISTUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign17 = ([20180511, '21:22:01', '', 'prot_eingecheckt', 'CHECKIN', 0, 0, 0, 'RECEPTION', 2], [False])
    ign17 = (['i', 'T', 'T', 'prot_eingecheckt', 'CHECKIN', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # igo1 = ([20161110, '10:41:45', '', 'prot_Zimmerdaten eingestellt', 'ZIMMERDATEN', 3, 0, 21, '', 0])
    ign1 = (['i', 'T', 'T', 'prot_Zimmerdaten eingestellt', 'ZIMMERDATEN', 'i', 'i', 'i', 'T', 'i'], [False])
    # ign20 = ([20180414, '21:14:36', '0.00', 'Zimmer fixiert: Chanton', 311, ' 17.04.2019-22.04.2019', 'AUFENTHALT', 2861, 8220, 10, 'RECEPTION', 2], [False])
    ign20 = (['i', 'T', 'T', 'Zimmer fixiert:', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])

    # Leistung
    # ign11 = ([20170321, '18:23:24', '70.00', 'Leistung geändert: 5 Speisen', ' 70.00 -> 5 Frühstück', ' 70.00', 'AENDERN_LEIS', 379, 8140, 0, 'RECEPTION', 2] , [False])
    ign11 = (['i', 'T', 'T', 'Leistung ge', 'T', 'T', 'AENDERN_LEIS', 'i', 'i', 'i', 'RECEPTION', 'i'] , [False])
    # ign13 = ([20170710, '22:11:40', '400.00', 'Leistung gebucht: 2 Pers. im DZSüd', ' CHF 400.00', 'LEISTUNG', 1389, 8912, 6, 'RECEPTION', 2], [False])
    ign13 = (['i', 'T', 'T', 'Leistung gebucht:', 'T', 'LEISTUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign14 = ([20170714, '17:45:22', '1020.00', 'Leistung gelöscht: 01  Apartment 2 Pers', " CHF 1'020.00", 'STORNO_LEIST', 981, 8582, 15, 'RECEPTION', 2], [False])
    ign14 = (['i', 'T', 'T', 'Leistung gel', "T", 'STORNO_LEIST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign28 = ([20180415, '19:03:01', '13.50', 'Leistung geändert: 1 Tourismustaxe 1 Pers. 12-16 Jahre', ' 15.00 -> 1 Tourismustaxe 1 Pers. 12-16 Jahre', 'AENDERN_LEIS', 2127, 9443, 0, 'RECEPTION', 2], [False])
    ign28 = (['i', 'T', 'T', 'Leistung ge', 'T', 'AENDERN_LEIS', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign29 = ([20180131, '12:08:14', '5560.00', '"Leistung geändert: 2 Pers. im DZNord', ' 880.00 -> 2 Pauschale ""Ski u. Wellness""', ' 5560.00"', 'AENDERN_LEIS', 2334, 7107, 0, 'RECEPTION', 2], [False])
    ign29 = (['i', 'T', 'T', '"Leistung ge', 'T', 'T', 'AENDERN_LEIS', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign30 = ([20180131, '12:08:42', '1390.00', '"Leistung gelöscht: 02  Pauschale ""Ski u. Wellness""', ' CHF 1\'390.00"', 'STORNO_LEIST', 2334, 7107, 10, 'RECEPTION', 2], [False])
    ign30 = (['i', 'T', 'T', '"Leistung ge', 'T', 'STORNO_LEIST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign23 = ([20180120, '08:31:08', '0.00', 'Fixierung aufgehoben: Zysset Kaufmann', 302, ' 20.01.2018-27.01.2018', 'AUFENTHALT', 344, 7932, 2, 'RECEPTION', 2], [False])
    ign23 = (['i', 'T', 'T', 'Fixierung aufgehoben', 'i', 'T', 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign24 = ([20180127, '10:58:47', '0.00', "RT's sortiert: Prospert", 'AUFENTHALT', 1808, 0, 0, 'RECEPTION', 2], [False])
    ign24 = (['i', 'T', 'T', "RT's sortiert:", 'AUFENTHALT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign32 = ([20170723, '16:10:35', '', 'prot_Saisonszeit eingestellt', 'SAISON', 1515, 9009, 5, 'RECEPTION', 2], [False])
    ign32 = (['i', 'T', 'T', 'prot_Saisonszeit eingestellt', 'SAISON', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])

    # Dokument Rechnung Zahlung
    # ign3 = ([20170204, '18:53:20', '0.00', 'Dokument erstellt: Rechnung (D)', 'DOKUMENT', 143, 1793, 0, 'RECEPTION', 2])
    ign3 = (['i', 'T', 'T', 'Dokument erstellt', 'DOKUMENT', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign19 = ([20180511, '19:00:03', '0.00', 'Dokument gelöscht: Rechnung (D)', 'STORNO_DOKUM', 2978, 9977, 9, 'RECEPTION', 2], [False])
    ign19 = (['i', 'T', 'T', 'Dokument ge', 'STORNO_DOKUM', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign9 = ([20170318, '15:10:18', '1862.00', 'Rechnung erstellt: 237', " CHF 1'862.00", " EC Karte: CHF 1'862.00", '', 'RECHNUNG', 358, 8136, 12, 'RECEPTION', 2], [False])
    ign9 = (['i', 'T', 'T', 'Rechnung erstellt', "T", "T", 'T', 'RECHNUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign18 = ([20180511, '10:19:01', '196.00', 'Rechnung erstellt: 1623', ' CHF 196.00', ' Visa: CHF 6.00', ' Mastercard: CHF 190.00', '', 'RECHNUNG', 3052, 10038, 4, 'RECEPTION', 2], [False])
    ign18 = (['i', 'T', 'T', 'Rechnung erstellt', 'T', 'T', 'T', 'T', 'RECHNUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign33 = ([20170207, '10:33:12', '920.00', '"Rechnung erstellt: 127', ' \x80 920', 0, ' EC Karte: \x80 920', 0, '"', 'RECHNUNG', 188, 8047, 7, 'RECEPTION', 2], [False])
    ign33 = (['i', 'T', 'T', '"Rechnung erstellt', 'T', 'i', 'T', 'i', 'T', 'RECHNUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign26 = ([20180420, '22:13:45', '786.60', 'Zahlungsart geändert: 1587', ' EC Karte: 586.60 -> Bar: 200.00', ' EC Karte: 586.60', 'RECHNUNG_AEN', 2612, 5680, 2, 'RECEPTION', 2], [False])
    ign26 = (['i', 'T', 'T', 'Zahlungsart ge', 'T', 'T', 'RECHNUNG_AEN', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign27 = ([20180507, '09:02:59', '450.00', 'Zahlungsart geändert: 1601', ' Bar: 450.00 -> VISA: 450.00', 'RECHNUNG_AEN', 2986, 9984, 1, 'RECEPTION', 2], [False])
    ign27 = (['i', 'T', 'T', 'Zahlungsart ge', 'T', 'RECHNUNG_AEN', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign31 = ([20180106, '18:36:08', '522.00', 'Zahlungseingang: 1263', ' 522.00', ' Debitor->Visa', 'DEB_ZAHLUNG', 2062, 9404, 0, 'RECEPTION', 0], [False])
    ign31 = (['i', 'T', 'T', 'Zahlungseingang:', 'T', 'T', 'DEB_ZAHLUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])

    # ---------------------
    # ign35 = ([20180109, '16:14:10', '380.00', '"Leistung geändert: 1 Pauschale ""Zermatt zum Kennenlernen""', ' 596.00 -> 1 Pauschale ""Zermatt zum Kennen"', 'AENDERN_LEIS', 2004, 2526, 0, 'RECEPTION', 2], [False])
    ign35 = (['i', 'T', 'T', '"Leistung ge', 'T', 'AENDERN_LEIS', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign36 = ([20180105, '17:41:44', '', 'prot_Extras eingestellt', 'SETUP', 2216, 9504, 3, 'RECEPTION', 2], [False])
    ign36 = (['i', 'T', 'T', 'prot_Extras eingestellt', 'SETUP', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign37 = ([20171231, '14:13:33', '0.00', 'Artikel angelegt: 10018', ' Neue Leistung 10018', 'ARTIKEL', 0, 0, 0, 'RECEPTION', 2], [False])
    ign37 = (['i', 'T', 'T', 'Artikel angelegt', 'T', 'ARTIKEL', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign38 = ([20171231, '14:14:13', '0.00', 'Artikel geändert: 10018', ' TIP', ' Sonstiges', ' 0.00', 'ARTIKEL', 0, 0, 0, 'RECEPTION', 2], [False])
    ign38 = (['i', 'T', 'T', 'Artikel ge', 'T', 'T', 'T', 'ARTIKEL', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign39 = ([20170210, '15:07:39', '42.00', '"Leistung gelöscht: 01  Ortstaxe 2 Pers.', ' \x80 42', '00"', 'STORNO_LEIST', 140, 8017, 2, 'RECEPTION', 2], [False])
    ign39 = (['i', 'T', 'T', '"Leistung gel', 'T', 'T', 'STORNO_LEIST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign51 = ([20170210, '15:07:51', '230.00', '"Leistung geändert: 2 Pers. im DZSüd', 1610, '00 -> 2 Pers. im DZSüd', 230, '00"', 'AENDERN_LEIS', 140, 8017, 0, 'RECEPTION', 2], [False])
    ign51 = (['i', 'T', 'T', '"Leistung ge', 'i', 'T', 'i', 'T', 'AENDERN_LEIS', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign52 = ([20170718, '14:13:31', '0.00', 'Leistung gebucht: ODER', 'LEISTUNG', 918, 8525, 1, 'RECEPTION', 2], [False])
    ign52 = (['i', 'T', 'T', 'Leistung gebucht', 'LEISTUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign53 = ([20170111, '11:09:25', '397.50', '"Rechnung erstellt: 41', ' \x80 397', 50, ' Visa: \x80 297', 50, ' Bar: \x80 100', 0, '"', 'RECHNUNG', 63, 7981, 2, 'RECEPTION', 2], [False])
    ign53 = (['i', 'T', 'T', '"Rechnung erstellt', 'T', 'i', 'T', 'i', 'T', 'i', 'T', 'RECHNUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign54 = ([20180307, '09:49:21', '4366.00', 'Rechnung erstellt: 1456', " CHF 4'366.00", ' Visa: CHF 195.50', " Amex: CHF 4'072.75", ' Mastercard: CHF 97.75', '', 'RECHNUNG', 1111, 8140, 17, 'RECEPTION', 2], [False])
    ign54 = (['i', 'T', 'T', 'Rechnung erstellt', "T", 'T', "T", 'T', 'T', 'RECHNUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign55 = ([20171204, '20:50:24', '0.00', 'Rechnung erstellt: 1201', ' CHF 0.00', '', 'RECHNUNG', 2093, 9422, 2, 'RECEPTION', 2], [False])
    ign55 = (['i', 'T', 'T', 'Rechnung erstellt', 'T', 'T', 'RECHNUNG', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign56 = ([20170916, '10:19:17', '196.00', 'Zahlungsart geändert: 1072', ' AMEX: 6.00', ' MASTER: 190.00 -> AMEX: 6.00', ' MASTER: 190.00', 'RECHNUNG_AEN', 1767, 9205, 11, 'RECEPTION', 2], [False])
    ign56 = (['i', 'T', 'T', 'Zahlungsart geändert', 'T', 'T', 'T', 'RECHNUNG_AEN', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign57 = ( , [False])
    # ign58 = ( , [False])
    # ign59 = ( , [False])[20170708, '
    # ---------------------

    # Gastdaten
    # ign6 = ([20170216, '16:42:59', '0.00', 'Gastdaten geändert: Neuer Gast -> Geschlossen', 'GAST', 0, 8163, 0, 'RECEPTION', 2], [False])
    ign6 = (['i', 'T', 'T', 'Gastdaten geändert: Neuer Gast ->', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign8 = ([20170315, '18:31:41', '0.00', '"Gastdaten geändert: Neuer Gast -> McGrory', ' Gilian"', 'GAST', 0, 8259, 0, 'RECEPTION', 2], [False])
    ign8 = (['i', 'T', 'T', '"Gastdaten ge', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign12 = ([20170709, '13:27:00', '0.00', 'Gast angelegt: Boonsararuxapong', 'GAST', 0, 8899, 0, 'RECEPTION', 2], [False])
    ign12 = (['i', 'T', 'T', 'Gast angelegt', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    # ign40 = ([20170805, '11:41:38', '0.00', '"Gastdaten geändert: Bouvier-Oberson -> Bouvier-Oberson', ' PEILLONNEX', ' 320 Route des Contamines"', 'GAST', 395, 8151, 0, 'RECEPTION', 2], [False])
    ign40 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign41 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign42 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'T','T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign43 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'T', 'T', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign44 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'T', 'T', 'T', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign45 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign46 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign47 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign48 = (['i', 'T', 'T', '"Gastdaten geändert:', 'T', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign49 = (['i', 'T', 'T', '"Gastdaten geändert:', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])
    ign50 = (['i', 'T', 'T', 'Gastdaten geändert:', 'GAST', 'i', 'i', 'i', 'RECEPTION', 'i'], [False])

    # DEMO
    # ign80 = ([20171212, '11:56:00', '0.00', 'Termin geändert: Hotel Geschlossen', 900, ' 10.12.2017-13.12.2017', ' 1 Pax', ' F', 'AUFENTHALT', 2057, 9398, 21, 'DEMO', 1], [False])
    ign80 = (['i', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'i', 'i', 'i', 'DEMO', 'i'], [False])
    ign81 = (['i', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'i', 'i', 'i', 'DEMO', 'i'], [False])
    ign82 = (['i', 'T', 'T', 'T', 'T', 'T', 'T', 'i', 'i', 'i', 'DEMO', 'i'], [False])
    ign83 = (['i', 'T', 'T', 'T', 'T', 'T', 'i', 'i', 'i', 'DEMO', 'i'], [False])
    ign84 = (['i', 'T', 'T', 'T', 'T', 'i', 'i', 'i', 'DEMO', 'i'], [False])

    return [pat1, pat2, pat3, pat4, pat5, pat6, pat7, pat8, pat9, pat10, pat11, pat12, pat13, pat14, pat15, pat16,
            pat17, pat18, pat19,
            ign1, ign2, ign3, ign4, ign5, ign6, ign7, ign8, ign9, ign10, ign11, ign12, ign13, ign14, ign15,
            ign16, ign17, ign18, ign19, ign20, ign21, ign22, ign23, ign24, ign25, ign26, ign27, ign28, ign29,
            ign30, ign31, ign32, ign33, ign34, ign35, ign36, ign37, ign38, ign39, ign40, ign41, ign42, ign43, ign44,
            ign45, ign46, ign47, ign48, ign49, ign50, ign51, ign52, ign53, ign54, ign55, ign56,
            ign80, ign81, ign82, ign83, ign84]


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
