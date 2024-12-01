l = []
r = []
with open("example-1.txt", "r") as file:
    for line in file:
        line = line.strip().split("   ")

        l.append(int(line[0]))
        r.append(int(line[1]))

print(l)
print(r)


l.sort()
r.sort()

n = []

for i in range(len(l)):
    n.append(abs(l[i] - r[i]))

print(n)

print(sum(n))

n2 = []

for number in l:

    n2.append(r.count(number) * number)

print(sum(n2))
