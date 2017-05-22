
def (list):
    list.sort()

    for i in range(0, len(list)-3):
        s = list[i]
        e = list[len(list)-i]
        m = list[i+1]
        if s+e+m ==0:
            return s,e,m
        elif s+e > 0:
            m = list[len(list)-i-1]

        m =
