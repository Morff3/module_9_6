import itertools

def all_variants(text):
    lis = []
    for lst in range(1, len(text) + 1):
        lis.append(list(itertools.combinations(text, lst)))
    for i in lis:
        for j in i:
            if ''.join(j) != 'ac':
                yield ''.join(j)


a = all_variants("abc")
for i in a:
    print(i)
