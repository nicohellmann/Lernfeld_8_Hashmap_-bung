# Angewendete Hashfunktion
def hashFunction(x,m):
    return x%m
# Hashtabelle in denen die schlüssel gespeichert werden sollen
hashtabelle = []
for i in range(7):
    hashtabelle.append([])

# Die Schlüssel
schlüssel = [2, 12, 5, 15, 19, 43, 53]


for i in range(0,len(schlüssel)):
    # Mithife der Hashfunktion wird der Index ausgerechnet wo der Schlüssel gespeichert werden soll
    index = hashFunction(schlüssel[i],7)
    # Anschließend wird der Schlüssel eingetragen
    hashtabelle[index].append(schlüssel[i])

print(hashtabelle)