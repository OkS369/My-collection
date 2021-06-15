'''
This code compare 2 xml files (u with old strings but with necessary language, t with all strings include new but with different language) and write new files with all strings, new (not translated) with tabulation. At the end program provide number of strings (traslated and new) and list of new strings.
'''
try:
    u = open('old_file_with_correct_lng.xml', 'r', encoding='utf-8')
    t = open('file_with_other_lng.xml', 'r', encoding='utf-8')
    nt = open('new_file_with_all_strings.xml', 'w', encoding='utf-8')
    dict_of_strings = {}
    not_translated = 0
    already_translated = 0
    while True:
        f = 'already_translated_strings'
        t_line = t.readline()
        if t_line == '':
            print(555)
            break
        if 'name' not in t_line:
            nt.write(t_line)
            continue
        index01 = t_line.find('"')
        index02 = t_line.find('"', index01 + 1)
        index03 = t_line.find('>', index02 + 1)
        index04 = t_line.find('</string>', index03 + 1)
        while index04 == -1:
            t_line += t.readline()
            index04 = t_line.find('<', index03 + 1)
        name = t_line[index01:index02 + 1]
        text = t_line[index03 + 1:index04]

        while True:
            u_line = u.readline()
            index1 = u_line.find(name)
            if index1 > 0:
                u.seek(0, 0)
                break
            if u_line == '':
                u.seek(0, 0)
                break
        if u_line == '':
            f = 'new_strings'
            u_line = t_line
        index2 = u_line.find(name, index1 + 1)
        index3 = u_line.find('>', index2 + 1)
        index4 = u_line.find('</string>', index3 + 1)
        text = u_line[index3 + 1:index4]
        if f == 'already_translated_strings':
            r = ''+text
            n = ''
            if 'Theme_chat' in name:
                n = '\t\t'
                already_translated -= 1
                not_translated += 1
            already_translated += 1
        elif f == 'new_strings':
            r = text
            n = '    '
            not_translated += 1
        t_line = n + t_line[:index03 + 1] + r + t_line[index04:]
        dict_of_strings[name] = t_line
    print('already_translated = ', already_translated)
    print('not_translated = ', not_translated)
    for i in sorted(dict_of_strings.keys()):
        nt.write(dict_of_strings[i])

finally:

    print('THE END')
    u.close()
    t.close()
    nt.close()
