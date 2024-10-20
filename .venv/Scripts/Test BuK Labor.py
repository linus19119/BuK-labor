import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Excell datei in verzeichniss der python datei reinkopieren (einlesen der DAten)
posts = pd.read_excel("C:/Users/linus/Downloads/Datensatz_Uhl.xlsx")
print(posts)

grouped_data = posts.groupby(pd.Grouper(key="published",freq="D"))
print(grouped_data["published"].count())

#plt.hist(grouped_data)
plt.stairs(grouped_data["published"].count())
plt.xticks(ticks=range(len(grouped_data["published"].count())),labels=grouped_data["publishes"].count().index.date,rotation=90)
#ticks =anzahl balken labels=beschriftung der balken
plt.title("beiträge pro tag")
plt.xlable("Datum")
plt.ylable("Anzahl der Beiträge")
plt.grid(True)
plt.savefig("post_per_day.png")#bbox_inches"tight"#zum speichern
plt.show()#um in pycharm das Diagramm überhaubt zu zeigen. Achtung Diagramm im Plot wird dann zurückgesetzt =>plt.show()erst nach savefig()


