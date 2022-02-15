import bluetooth
# liste les appareils connectés
def search():
    return bluetooth.discover_devices(duration=8, lookup_names=True)

devices = None
print("Recherche d'appareils...")
while True:
    devices = search()
    if devices != None or devices != []:
        print(devices)