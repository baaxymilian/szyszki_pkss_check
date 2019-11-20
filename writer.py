from flask import json

data = {}
data['site'] = []
data['site'].append({
    'address': "https://anoldlogcabinforsale.szyszki.de/building"
})
data['site'].append({
    'address': "https://webuiltthiscity.szyszki.de/api/T_ref"
})
data['site'].append({
    'address': "https://layanotherlogonthefire/szyszki.de"
})
data['site'].append({
    'address': "https://ivegotthepower.szyszki.de/mpec/data"
})
data['site'].append({
    'address': "https://selfcontrol.szyszki.de"
})
data['site'].append({
    'address': "https://imagine.szyszki.de"
})
data['site'].append({
    'address': "https://hotstuff.szyszki.de"
})
data['site'].append({
    'address': "https://closingtime.szyszki.de/api/time"
})
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)