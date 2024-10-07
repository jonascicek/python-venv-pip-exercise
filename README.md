# Projekt: Datenvisualisierung mit Matplotlib
In diesem Beispiel werden wir ein Python-Skript erstellen, das eine Liste von Zahlen verarbeitet und daraus ein Diagramm erstellt. Wir verwenden die Bibliothek Matplotlib, um ein einfaches Liniendiagramm zu zeichnen.
## Schritt 1: Virtuelle Umgebung einrichten
1. Erstelle ein neues Projektverzeichnis
```bash
mkdir daten_visualization
cd daten_visualization
```
2. Erstelle eine virtuelle Umgebung
```bash
python -m venv venv
```
3. Aktiviere die virtuelle Umgebung
- Für MacOS und Linux:
```bash
source venv/bin/activate
```
- Für Windows:
```bash
venv\Scripts\activate
```
## Schritt 2: Bibliotheken installieren
Für dieses Projekt verwenden wir die Bibliothek matplotlib, um die Daten zu visualisieren. Installiere die Bibliothek mit Pip:
```bash
pip install matplotlib
```
## Schritt 3: Erstelle die requirements.txt
Um die Abhängigkeiten zu dokumentieren, erstellen wir eine requirements.txt Datei:
```bash
pip freeze > requirements.txt
```
Diese Datei stellt sicher, dass andere Benutzer (oder du selbst auf einem anderen Rechner) die gleichen Bibliotheken installieren können.
## Schritt 4: Erstelle das Python-Skript
Erstelle eine Python-Datei namens daten_visualisierung.py im Projektverzeichnis. Diese Datei verarbeitet eine Liste von Zahlen und visualisiert sie als Liniendiagramm.
```python
import matplotlib.pyplot as plt

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x]  # Quadratzahlen

# Liniendiagramm erstellen
plt.plot(x, y, label='Quadratzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadratzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Quadrat')

# Legende anzeigen
plt.legend()

# Diagramm anzeigen
plt.show()
```
Erläuterung:
- Wir erstellen zwei Listen: x enthält die Zahlen von 0 bis 9 und y enthält deren Quadrate (z.B. 0², 1², 2², ... 9²).
- Mit plt.plot() wird ein Liniendiagramm erzeugt, das die Quadrate der Zahlen darstellt.
- Titel und Achsenbeschriftungen werden hinzugefügt, um das Diagramm verständlicher zu machen.
- plt.show() zeigt das Diagramm auf dem Bildschirm an.
## Schritt 5: Skript ausführen
Führe das Python-Skript aus, um das Liniendiagramm anzuzeigen:
```bash
python daten_visualisierung.py
```
Das Diagramm sollte nun angezeigt werden, das die Quadratzahlen von 0 bis 9 darstellt.
## Schritt 6: .gitignore erstellen
Wenn du das Projekt versionieren willst, solltest du eine .gitignore Datei erstellen, um die virtuelle Umgebung und andere nicht benötigte Dateien aus dem Git-Repository auszuschließen.
```bash
echo "venv/" > .gitignore
```
## Schritt 7: Projekt auf GitHub veröffentlichen
1. Initialisiere ein neues Git-Repository
```bash
git init
```
2. Füge die Dateien zum Repository hinzu
```bash
git add .
```
3. Erstelle den ersten Commit
```bash
git commit -m "first datavisualisation example"
```
4. Erstelle ein neues Repository auf GitHub
5. Verlinke das lokale Repository mit dem GitHub-Repository
```bash
git remote add origin <repository-url>
```
6. Pushe die Änderungen auf GitHub
```bash
git push -u origin master
```
Jetzt sollte dein Projekt auf GitHub veröffentlicht sein und andere Benutzer können es herunterladen und ausführen.
