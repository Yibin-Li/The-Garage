ow = input('enter file name:')
file = open(ow)
words_lst = []
for x in file:
        x = x.strip('\n')
        x = x.strip('')
        words = x.split(' ')
        for word in words:
                words_lst.append(word)
count = {}
for x in words_lst:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
"""An alternative
for x in words_lst:
    count[x] = count.get(x,0) + 1
"""
o = []
for (x,words_lst) in count.items():
    o.append((words_lst,x))
o.sort(reverse = True)
print (o[:10])

