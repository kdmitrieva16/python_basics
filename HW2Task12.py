s = int(input("s: "))
p = int(input("p: "))

for x in range(1001):
    for y in range(1001):
        if x + y == s and x * y == p and x <= y:
            print(f'x={x},y={y}')
            break