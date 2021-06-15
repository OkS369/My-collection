with open('draft of dictionary.txt', 'r', encoding='UTF-8') as dod:
    dict_from_English_to_Ukrainian = {}
    dict_from_Ukrainian_to_English = {}
    dict_mixed_EU = {}
    dict_mixed_UE = {}
    for line in dod.readlines():
        f, t = line.strip().split(' ')
        dict_from_English_to_Ukrainian[f] = t
        dict_from_Ukrainian_to_English[t] = f
        dict_mixed_EU[f] = f
        dict_mixed_UE[t] = t
print(dict_from_English_to_Ukrainian, dict_from_Ukrainian_to_English, dict_mixed_EU, dict_mixed_UE, sep='\n')
