#[(x**2 + y**2)**0.5 for x in range(1,26) for y in range(1,26) if ((x**2 + y**2)**00.5) in range(1,26)]
py_trip = [(x, y, (int((x**2 + y**2)**0.5))) for x in range(1,26) for y in range(1,26) if x <= y if y <= (x**2 + y**2)**0.5 if (x**2 + y**2)**0.5 in range(1,26)]
'''py_trip = []
for x in range(1,26):
    for y in range(1,26):
        if x <= y:
            if y <= (x**2 + y**2)**0.5:
                z = (x**2 + y**2)**0.5
                if z in range(1,26):
                    z = int(z)
                    print(z)
                    py_trip.append((x,y,z))'''