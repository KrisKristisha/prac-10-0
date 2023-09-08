with open("med_research.txt", 'r') as fin:
    with open("output.txt", 'w') as fout:
        s = fin.readlines()
        #print(s)
        a = []
        for i in range(len(s)):
            b = s[i]
            if s[i] != s[len(s)-1]:
                s[i] = b[:-1]
            a.append(s[i].split(' '))
        #print(a)
        for i in range(len(a[0])):
            for j in range(len(a)):
                c = a[j]
                print(c[i], end = ' ', file = fout)
                #print(c[i], end = ' ')
            print(file = fout)
            #print()
