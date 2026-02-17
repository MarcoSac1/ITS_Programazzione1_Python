nPari = 0
n = 0
somma= 0
max = min = -1
val = None

while val != -1:
    val = int(input())
    if n ==0:
        massimo = minimo = val
    else:
        if val > massimo:
            massimo = val
            if val < minimo:
                minimo = val
                somma += val
                n += 1
                if val % 2 == 0:
                    nPari