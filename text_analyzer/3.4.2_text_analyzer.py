with open('text.txt','r') as x:
    s = x.read()\
        .replace('-', ' ').replace('«', ' ').replace('»', ' ').replace('|', ' ').replace('–', ' ').replace("'", ' ').replace('*', ' ').replace(':', ' ').replace(';', ' ').replace('(', ' ').replace(')', ' ').replace('—', ' ').replace('"', ' ').replace('?', ' ').replace('…', ' ').replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace('!', ' ')\
        .split()
    s.sort()
    #print(s)

    text = {}
    for i in s:
        if i in text:
            text[i] += 1
        else:
            text[i] = 1
    #print(text)

    numbers = []
    words = []
    for i in text.keys():
        words.append(i)
        numbers.append(text[i])

# find most popular word
    t = 0
    n = 0
    for i in range(len(numbers)):               
        if t < numbers[i]:
            t = numbers[i]
            n = i
    print(words[n], numbers[n], sep = ' ')      # print most popular word and number of repeats

with open('file_1.txt','w') as y:
    for i in range(len(words)):
        y.write(str(words[i]) + (' ' * (14 - len(words[i]))) + str(numbers[i]) + '\n')  # print in file all words with len of l and repeats more than m
        #print(words[i], '\t', numbers[i], sep = '')            # print all words with len of l and repeats more than m


# find all words with len of l and repeats more than m
    l = 0                                               # len of word
    m = 500                                             # repeats of word
    words_l = []
    numbers_l = []
    for i in range(len(words)):
        le = len(words[i])
        if "'" in words[i]:
            le -= 1
        if (l < le):
            if "'" in words[i]:
                continue
            words_l.append(words[i])
            numbers_l.append(numbers[i])
            
    #print(words, '\n\n\n', numbers, sep = '')
        
with open('file_2.txt','w') as y:
    for i in range(len(words_l)):
        if numbers_l[i] <= m:
            continue
        y.write(str(words_l[i]) + (' ' * (14 - len(words_l[i]))) + str(numbers_l[i]) + '\n')  # print in file all words with len of l and repeats more than m
        #print(words_l[i], '\t', numbers_l[i], sep = '')            # print all words with len of l and repeats more than m

