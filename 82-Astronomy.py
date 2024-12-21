import ephem

jupiter = ephem.Jupiter()
jupiter.compute("1230/1/1")
distAu = jupiter.sun_distance
distKm = distAu * 149597870.691
print(distKm)
