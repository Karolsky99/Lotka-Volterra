from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv('data_storage.txt', delimiter='\t')

# dane na osi X
val_x = df.time.to_list()
# dane na osi Y
val_y1 = df.prey.to_list()
val_y2 = df.predator.to_list()

# generowanie serii danych wykresu
plt.plot(val_x, val_y1, 'g-', label='Ofiara')
plt.plot(val_x, val_y2, 'r-', label='Drapieżnik')

# tytuł wykresu
plt.title('Model Lotki-Volterry - Zmiana liczebności populacji w czasie')

# legenda
plt.legend(loc="upper center",)

# etykiety osi
plt.xlabel('Czas [a.u]')
plt.ylabel('Liczebność')

# zapisywanie wykresu
plt.savefig('plot.png')

# wyswietlanie wykresu
plt.show()

