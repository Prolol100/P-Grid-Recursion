n = 2

cells = n ** n

x = n

for i in range(cells):
    print(x)
    tower = x
    for a in range(x-1):
        tower = x ** tower
    x = tower