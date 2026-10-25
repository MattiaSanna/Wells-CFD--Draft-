

cord = 72

with open("NACA_0015.txt", "r") as p, open("NACA_0015_72.txt", "w") as d:

    for line in p:
        
        l = line.split()
        
        x = round((float(l[0])*cord - cord/2),4)
        z = round((float(l[1])*cord),5)
        y = float(l[2])
        
        new_line = str(x) + " " + str(y) + " " + str(z) 
        
        d.write(f"{x} {y} {z}\n")
    
    
    
    