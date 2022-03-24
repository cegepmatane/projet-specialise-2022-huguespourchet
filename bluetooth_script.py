import bluetooth
# liste les appareils connectés
def search():
    return bluetooth.discover_devices(duration=8, lookup_names=True)

devices = None
print("Recherche d'appareils...")
all_devices = []
while True:
    devices = search()
    if devices != None or devices != []:
        for d in devices:
            if d not in all_devices:
                all_devices.append(d)
        if all_devices == []:
            print("Aucun appareil détecté pour le moment...")
        else:
            print(all_devices)
