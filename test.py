from datetime import datetime
from sharppy.sharptab import profile
import json

pres = []
height = []
temp = []
dew = []
wind = []
hdg = []

with open('sounding-test.csv', 'r') as csvfile:
    lines = csvfile.readlines()[1:]

    for line in lines:
        [p, h, t, d, w, hd] = [ part.strip() for part in line.split(',')]

        pres.append(p)
        height.append(h)
        temp.append(t)
        dew.append(d)
        wind.append(w)
        hdg.append(hd)

pres.reverse()
height.reverse()
temp.reverse()
dew.reverse()
wind.reverse()
hdg.reverse()

timestamp = datetime.fromisoformat('2023-09-16T18:00:00')

p = profile.create_profile(
    profile='convective',
    pres=pres,
    hght=height,
    tmpc=temp,
    dwpc=dew,
    wdir=hdg,
    wspd=wind,
    location='KDNR',
    date=timestamp
)


stuff = {
    'dwpc': p.dwpc.tolist(),
    'wetbulb': p.wetbulb.tolist(),
    'tmpc': p.tmpc.tolist(),
    'pres': p.pres.tolist(),
    'mlpcl': {
        'ttrace': p.mlpcl.ttrace.tolist(),
        'ptrace': p.mlpcl.ptrace.tolist()
    }
}

print(stuff)