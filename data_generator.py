# stałe [a.u.]
kx = 0.01
lx = 0.00005
ky = 0.00001
ly = 0.005

time = 0  # czas początku symulacji [a.u.]
tend = 3000  # czas zakończenia symulacji [a.u.]
tstep = 0.1  # długość kroku [a.u.]

# wartości początkowe zmiennych
prey = 1000
predator = 100

# równania różniczkowe
# dxdt = vx - ux
# dydt = vy - uy

f = open('data_storage.txt', "w")

# wypisanie początkowych danych w pierwszej linijce
line = "time" + '\t' + "prey" + '\t' + "predator" + '\n'
f.write(line)
line = format(time, ".4e") + '\t' + format(prey, ".4e") + '\t' + format(predator, ".4e") + '\n'
f.write(line)

# początek symulacji
for i in range(int(tend/tstep)):
    time = time + tstep
    vx = kx * prey
    ux = lx * prey * predator
    prey = prey - (ux * tstep) + (vx * tstep)
    vy = ky * prey * predator
    uy = ly * predator
    predator = predator - (uy * tstep) + (vy * tstep)
    line = format(time, ".4e") + '\t' + format(prey, ".4e") + '\t' + format(predator, ".4e") + "\n"
    f.write(line)



