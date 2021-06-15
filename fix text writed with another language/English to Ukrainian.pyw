import clipboard


def change_layout(dic):
    text = clipboard.paste()
    result = ''
    for ts in text:
        if ts in dic.keys():
            result += dic[ts]
        else:
            result += ts
    clipboard.copy(result)
    print(result)
    exit()


dict_from_English_to_Ukrainian = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ї', 'a': 'ф', 's': 'і', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'є', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', '-': '-', '=': '=', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', '*': '*', '(': '(', ')': ')', '_': '_', '+': '+', 'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ї', 'A': 'Ф', 'S': 'І', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж', '"': 'Є', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', '?': ',', 'й': 'й', 'ц': 'ц', 'у': 'у', 'к': 'к', 'е': 'е', 'н': 'н', 'г': 'г', 'ш': 'ш', 'щ': 'щ', 'з': 'з', 'х': 'х', 'ї': 'ї', 'ф': 'ф', 'і': 'і', 'в': 'в', 'а': 'а', 'п': 'п', 'р': 'р', 'о': 'о', 'л': 'л', 'д': 'д', 'ж': 'ж', 'є': 'є', 'я': 'я', 'ч': 'ч', 'с': 'с', 'м': 'м', 'и': 'и', 'т': 'т', 'ь': 'ь', 'б': 'б', 'ю': 'ю', 'Й': 'Й', 'Ц': 'Ц', 'У': 'У', 'К': 'К', 'Е': 'Е', 'Н': 'Н', 'Г': 'Г', 'Ш': 'Ш', 'Щ': 'Щ', 'З': 'З', 'Х': 'Х', 'Ї': 'Ї', 'Ф': 'Ф', 'І': 'І', 'В': 'В', 'А': 'А', 'П': 'П', 'Р': 'Р', 'О': 'О', 'Л': 'Л', 'Д': 'Д', 'Ж': 'Ж', 'Є': 'Є', 'Я': 'Я', 'Ч': 'Ч', 'С': 'С', 'М': 'М', 'И': 'И', 'Т': 'Т', 'Ь': 'Ь', 'Б': 'Б', 'Ю': 'Ю'}
change_layout(dict_from_English_to_Ukrainian)