import sys
import requests
import json

api_key = sys.argv[1]
api_url = 'https://api.openai.com/v1/chat/completions'
prompt = sys.argv[2]

# Set up the headers with the API key
headers = {
    'Authorization': 'Bearer '+api_key,
    'Content-Type': 'application/json'
}

# Define the messages for the conversation
data = {
    "model": "gpt-4",  # Specify model (gpt-3.5-turbo or gpt-4)
    "messages": [
        {"role": "system", "content": '''Relevanz bewerten nach den folgenden Kriterien:

"Relevanz	0	nicht relevant	Der betrachtete Post beinhaltet keine Hinweise auf psychosoziale Bedarfe oder Ressourcen gem. der hier aufgeführten Definition.
	1	relevant	Der betrachtete Post beinhaltet relevante Hinweise zu psychosozialen Bedarfen und/oder Ressourcen, ist relevant für die Lage "Hochwasser" und lässt sich in mind. eine der folgenden Kategorie einordnen.
	2	relevant, keine der aufgeführten Kategorien	Der betrachtete Post beinhaltet relevante Hinweise zu psychosozialen Bedarfen und/oder Ressourcen, lässt sich jedoch in keine weitere Kategorie einordnen.
Personenbezogene, biografische oder situative Informationen, die nicht anderweitig klassifiziert werden können, können hier eingeordnet werden. Dazu zählen etwa Merkmale der Lage (Art und Ausmaß der Lage, zeitlicher Verlauf) sowie Merkmale der Person (Alter, Geschlecht, Bildungsgrad, sofern diese bekannt/erkennbar sind..'''},
        {"role": "user", "content": '''Bewerte
den
Socialmediapost
am
Ende
nach
folgenden
Kriterien:
0
nicht
relevant
Der
betrachtete
Post
beinhaltet
keine
Hinweise
auf
psychosoziale
Bedarfe
oder
Ressourcen
gem.
der
hier
aufgeführten
Definition.
1
relevant
Der
betrachtete
Post
beinhaltet
relevante
Hinweise
zu
psychosozialen
Bedarfen
und/oder
Ressourcen,
ist
relevant
für
die
Lage
"Hochwasser"
und
lässt
sich
in
mind.
eine
der
folgenden
Kategorie
einordnen.
2
relevant,
keine
der
aufgeführten
Kategorien
Der
betrachtete
Post
beinhaltet
relevante
Hinweise
zu
psychosozialen
Bedarfen
und/oder
Ressourcen,
lässt
sich
jedoch
in
keine
weitere
Kategorie
einordnen.
Personenbezogene,
biografische
oder
situative
Informationen,
die
nicht
anderweitig
klassifiziert
werden
können,
können
hier
eingeordnet
werden.
Dazu
zählen
etwa
Merkmale
der
Lage
(Art
und
Ausmaß
der
Lage,
zeitlicher
Verlauf)
sowie
Merkmale
der
Person
(Alter,
Geschlecht,
Bildungsgrad,
sofern
diese
bekannt/erkennbar
sind.
Der
Post
lautet
:"Schwerin. Hacker haben in Mecklenburg-Vorpommern erneut eine Attacke gestartet. Und sie ist noch nicht zu Ende. Der Angriff ist nicht der Erste dieser Art. Der Hackerangriff auf die Webseiten der Landesregierung und der Polizei von Mecklenburg-Vorpo..."'''}
    ],
    "temperature": 0.7
}

# Make the request to the API
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Check for a successful response
if response.status_code == 200:
    # Parse the response content
    result = response.json()
    print("The entire result:")
    print(result)
    # Extract and print the assistant's reply
    print(result['choices'][0]['message']['content'])
else:
    print("Error: "+str(response.status_code))
    print(response.text)
