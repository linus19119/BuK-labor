import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt


# Excel-Datei einlesen (richtiges Sheet mit den Zeitstempel auswählen)
posts = pd.read_excel("C:/Users/linus/Downloads/Datensatz_Uhl.xlsx",sheet_name="Daten")

# Die 'published'-Spalte in das Datetime-Format konvertieren
posts['published'] = pd.to_datetime(posts['published'], format="%d.%m.%y %H:%M")

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
plt.tight_layout()
plt.show()