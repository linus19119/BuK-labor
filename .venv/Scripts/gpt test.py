import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # Nur pyplot von matplotlib importieren

# Excel-Datei einlesen (richtiges Sheet mit den Zeitstempel auswählen)
try:
    # Die 'published'-Spalte in das Datetime-Format konvertieren, während die Datei gelesen wird
    posts = pd.read_excel("C:/Users/linus/Downloads/Datensatz_Uhl.xlsx", sheet_name="Daten",
                          parse_dates=['published'], date_parser=lambda x: pd.to_datetime(x, format="%d.%m.%y %H:%M", errors='coerce'))
except Exception as e:
    print(f"Fehler beim Einlesen der Datei: {e}")

# Überprüfen, ob die Umwandlung erfolgreich war
if posts['published'].isnull().any():
    print("Warnung: Einige Zeitstempel konnten nicht konvertiert werden.")

# Ereignisse definieren mit datetime-Objekten für 2024
ereignisse = {
    pd.to_datetime("30.05.2024", format="%d.%m.%Y"): "30.5 Beginn der intensiven Regenfälle",
    pd.to_datetime("31.05.2024", format="%d.%m.%Y"): "31.5 Starke Niederschläge setzen sich fort, Überflutungen in einigen Regionen.",
    pd.to_datetime("01.06.2024", format="%d.%m.%Y"): "1.6 Höchste Niederschläge mit über 200 mm in 24 Stunden. Rekordabflüsse werden gemessen.",
    pd.to_datetime("02.06.2024", format="%d.%m.%Y"): "2.6 Situation verschärft sich; viele Flüsse treten über die Ufer.",
    pd.to_datetime("03.06.2024", format="%d.%m.%Y"): "3.6 Niederschläge lassen nach, aber die Auswirkungen sind verheerend."
}

# Daten nach der 'published'-Spalte gruppieren mit täglicher Häufigkeit
grouped_data = posts.groupby(pd.Grouper(key="published", freq="D"))

# Anzahl der Einträge pro Tag zählen
daily_counts = grouped_data["published"].count()
print(daily_counts)

# Plotten der täglichen Veröffentlichungen
plt.figure(figsize=(12, 6))
daily_counts.plot(kind='bar', color='skyblue')
plt.title('Anzahl der veröffentlichten Beiträge pro Tag')
plt.xlabel('Datum')
plt.ylabel('Anzahl der Beiträge')
plt.xticks(rotation=90)
plt.grid(axis='y')

# Vertikale Linien für die Ereignisse hinzufügen
for datum, beschreibung in ereignisse.items():
    plt.axvline(datum, color='red', linestyle='--', label=beschreibung)

plt.legend()
plt.tight_layout()
plt.show()

# Daten nach dem 'published'-Datum gruppieren mit stündlicher Frequenz
grouped_data = posts.groupby(pd.Grouper(key="published", freq="h"))

# Anzahl der Einträge pro Stunde zählen
hourly_counts = grouped_data["published"].count()

# Liniendiagramm der stündlichen Veröffentlichungen plotten
plt.figure(figsize=(12, 6))
hourly_counts.plot(kind='line', color='skyblue', marker=',')
plt.title('Anzahl der veröffentlichten Beiträge pro Stunde')
plt.xlabel('Datum und Uhrzeit')
plt.ylabel('Anzahl der Beiträge')
plt.xticks(rotation=45)
plt.grid()

# Vertikale Linien für die Ereignisse hinzufügen
for datum, beschreibung in ereignisse.items():
    plt.axvline(datum, color='red', linestyle='--', label=beschreibung)

plt.legend()
plt.tight_layout()
plt.show()
