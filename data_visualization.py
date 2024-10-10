import matplotlib.pyplot as plt
import pandas as pd

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x]  # Quadratzahlen

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Kubik
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**3 for i in x]  # Kubikzahlen

# Liniendiagramm erstellen
plt.plot(x, y, label='Kubikzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Kubikzahlen')

# Legende anzeigen
plt.legend()

# PNG speichern
plt.savefig('diagramm.png')

# Diagramm anzeigen
plt.show()

# Pandas Dataframe
nums = pd.DataFrame(y)

# Pandas to CSV
nums.to_csv('zahlen.csv', sep='\t', encoding='UTF-8', index=False, header=True)
