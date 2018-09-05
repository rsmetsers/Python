getallen = [3,8,12,-4]

max  = 0
for getal in getallen:
    if getal > max:
        max = getal

print( "max is:", max )



min  = getallen[0]
for getal in getallen:
    if getal < min:
        min = getal

print( "min is:", min )
