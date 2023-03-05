def interleave(*iterables ):
    #l=[]
    for i in range(len(iterables[0])):
        for j in iterables:
            yield j[i]




l=[]
for i in interleave('abc', [1, 2, 3,4], ('!', '@', '#')):
    l.append(i)
print(l)