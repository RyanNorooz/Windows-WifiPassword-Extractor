import yaml
import subprocess


extracted = {}
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
wifis = [i.split(":")[1].strip('\r').strip() for i in data if "All User Profile" in i]

for wifi in wifis:
    data = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("utf-8").split("\n")
    pw = [i.split(":")[1].strip('\r').strip() for i in data if "Key Content" in i]
    pw = pw[0] if pw else None
    extracted[wifi] = pw

with open("Wifi-Passwords.yaml", 'w') as file:
    yaml.dump(extracted, file, sort_keys=True, indent=4, encoding='utf-8')

MAC = subprocess.check_output("ipconfig /all").decode("utf-8").replace("\r", '').replace("\n\n\n", '\n').strip()
with open("MAC-Addresses.txt", "w") as file:
    file.write(MAC)

print('''
wrote 2 files:
    Wifi-Passwords.yaml
    MAC-Addresses.txt
''')
