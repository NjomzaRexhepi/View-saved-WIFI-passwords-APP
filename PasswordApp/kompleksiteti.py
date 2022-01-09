import subprocess
import re
import pprint
import json
import numpy as np
import matplotlib.pyplot as plt

output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode()
profiles = [i.strip() for i in re.findall('(?<=:).*', output)[1:]]

tofile = []

pair = {}

for profile in profiles:
    try:
        o = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode()
        keya = re.findall('Key Content.*', o)
        key = re.findall('(?<=:).*', keya[0])[0]
        pair[profile] = key.strip()
    except Exception as e:
        pass

wifinames1 = []
wifinames2 = []
wifinames3 = []

for p in pair:
    try:
        re.findall('^[0-9]*$',  pair[p])[0]
        wifinames1.append(p)

    except Exception as e:
        pass

for p in pair:
    try:
        re.findall('^[a-z]*$',  pair[p])[0]
        wifinames1.append(p)

    except Exception as e:
        pass

for p in pair:
    try:
        re.findall('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',  pair[p])[0]
        wifinames2.append(p)

    except Exception as e:
        pass

for p in pair:
    try:
        re.findall('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',  pair[p])[0]
        wifinames3.append(p)

    except Exception as e:
        pass

wifinames1 = tuple(wifinames1)
wifinames2 = tuple(wifinames2)
wifinames3 = tuple(wifinames3)

y_pos = np.arange(len(wifinames1 + wifinames2 + wifinames3))

performance1 = [1 for i in range(len(wifinames1))]
performance2 = [2 for i in range(len(wifinames2))]
performance3 = [3 for i in range(len(wifinames3))]

p1 = plt.barh(y_pos, tuple(performance1 + performance2 + performance3), align='center', alpha=0.5)
plt.yticks(y_pos, wifinames1 + wifinames2 + wifinames3 )

plt.show()