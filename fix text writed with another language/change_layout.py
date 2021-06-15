import clipboard


def change_layout(dic):
    text = clipboard.paste()
    result = ''
    for ts in text:
        if ts == ' ':
            result += ' '
        if ts in dic.keys():
            result += dic[ts]
    clipboard.copy(result)
    print(result)
    exit()
