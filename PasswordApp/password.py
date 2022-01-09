import subprocess
import json
import re
import pprint

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
    
password = []

for p in pair:
    try:       
        password.append({p: pair[p]})
    except Exception as e:
        pass

open('final1.txt','w').write("Wi-Fi and Password:"+ "\n\n")
open('final1.txt','a').write( "\n".join([ json.dumps(d) for d in password ]) )

weak = []
medium = []
strong = []

for p in pair:
    try:
        find2 = re.findall("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",pair[p])[0]
        medium.append({p: pair[p]})
    except Exception as e:
        pass
for p in pair:
    try:
        find2 = re.findall("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",  pair[p])[0]
        strong.append({p: pair[p]})
    except Exception as e:
        pass

for p in pair:
    try:
        ugjet = re.findall('^[a-z]*$',  pair[p])[0]
        weak.append({p: pair[p]})
    except Exception as e:
        pass

for p in pair:
    try:
        ugjet = re.findall('^[0-9]*$',  pair[p])[0]
        weak.append({p: pair[p]})
    except Exception as e:
        pass



open('final.txt','w').write("Weak:"+ "\n")
open('final.txt','a').write( "\n".join([ json.dumps(d) for d in weak ]) )
                                    #ketu
open('final.txt','a').write("\n\nMedium: " + "\n")               #ketu
open('final.txt','a').write( "\n".join([ json.dumps(d) for d in medium ]) )
                                    #ketu
open('final.txt','a').write("\n\nStrong: " + "\n")               #ketu
open('final.txt','a').write( "\n".join([ json.dumps(d) for d in strong ]) )
