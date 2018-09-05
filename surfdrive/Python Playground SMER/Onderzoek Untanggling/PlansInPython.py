
#MAX PLAN
values = [3,8,12,-4]

max  = 0
for i in values:
    if i > max:
        max = i

print( "max is:", max )

#MAX PLAN, asking user for 5 input values
nr_values_to_ask = 5
max  = 0

for i in range(nr_values_to_ask):
    value = int(input("Enter a value "))
    if value > max:
        max = value

print( "max is:", max )

#MIN PLAN
values = [3,8,12,-4]

min  = values[0]
for i in values:
    if i < min:
        min = i

print( "min is:", min )
