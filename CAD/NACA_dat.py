cord = 72

with open("NACA_0015.txt", "r") as p, \
     open("NACA_0015_72.dat", "w") as d:

    for line in p:
        l = line.split()

        if len(l) < 2:
            continue

        x = round(float(l[0]) * cord, 4)
        z = round(float(l[1]) * cord, 5)

        d.write(f"{x} {z}\n")