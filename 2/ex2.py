

def max(v):
    m = v[0] #(1)
    for i in range(1, len(v)): #(2)
        if v[i] > m: #(3)
            m = v[i] #(4)
    return m #(5)