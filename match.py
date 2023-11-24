import requests
import matplotlib.pyplot as plt
import numpy as np
import re
mainstats={}
records={}
rec=[]
view=[]
file=open("impstats.txt",'w')

headers = {
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Referer': 'https://www.fotmob.com/matches/east-bengal-fc-vs-kerala-blasters-fc/3j39c35b',
    'x-fm-req': 'eyJib2R5Ijp7ImNvZGUiOjE2OTk3NTY2OTQ5NTJ9LCJzaWduYXR1cmUiOiIwQzdDMzRGQTczNjk2ODAwMzE0MjUwODI2QjBGRDY4QyJ9',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'matchId': '4322831',
}

response = requests.get('https://www.fotmob.com/api/matchDetails', params=params, headers=headers)
gem=response.json()
#for i in gem:
    #print(i)
a=gem["content"]
b=a['stats']
c=b['Periods']
d=c['All']
e=d["stats"]
f=e[0]
g=f['stats']
for i in g:
    mainstats.update({i['key']:i['stats']})
    #print(a.keys())
    #b=a["teams"]
    #print(b)
#print(mainstats)
#print(e[2])
h=e[2]
i=h['stats']
for x in i:
    #print(x)
    mainstats.update({x['title']:x['stats']})
h=e[3]
i=h['stats']
for x in i:
    #print(x)
    mainstats.update({x['title']:x['stats']})
h=e[4]
i=h['stats']
for x in i:
    #print(x)
    mainstats.update({x['title']:x['stats']})
h=e[5]
i=h['stats']
for x in i:
    #print(x)
    mainstats.update({x['title']:x['stats']})
h=e[6]
i=h['stats']
for x in i:
    #print(x)
    mainstats.update({x['title']:x['stats']})
for i in mainstats:
    file.write(f'{i}:{mainstats[i]}\n')
file.close()
def dataext(dict):
        for i in dict:
            for x in i:
                if None:
                    continue
                l=[]
                #print(x)
                position=x['positionStringShort']
                #fpos=x['role']
                name=x['name']
                fname=name['fullName']
                stats=x['stats']
                stats0=stats[:]
                rstats={}
                for i in range(len(stats0)):
                    stats00=stats0[i]
                    x=stats00['stats']
                    rstats.update(x)
                #rstats.update(lstats)
                y = {}
                for i in rstats:
                    x=rstats[i]
                    y.update({x['key']:x['value']})
                l=[position,y]
                #print(fname)
                #dict[fname]=l
                #rec.append(list(dict))
                records.update({fname:l})


b=a["lineup"]
c=b['lineup']
x=c.pop()
y=x['players']
dataext(y)
d=c[0]
e=d['players']
#print(c)
dataext(e)

#['FotMob rating']
    #print(j)
        #k={i['key']:i['value']}
    #print(k)
    #r=[position,k]
    #records.update({fname:r})
    #print(records)
#for x in j:
    #print(x)
    #records.update({x['title']:x['stats']})
print(records)
print(len(records))
#print(rec)
for i in records:
    name=i
    pos=records[i][0]
    dict=records[i][1]
    rating=dict["rating_title"]
    x = dict.copy()
    x.update({"rating_title" : rating * 10})
    print(x)
    z = []
    y=[]
    for i in dict:
        if type(dict[i])==None:
            x.pop(i)
        elif dict[i]==True or dict[i]==False:
            x.pop(i)
        elif type(dict[i])==str and "(" in dict[i]:
            a=dict[i].split("(")
            b=a[1].split("%")
            x[i]=float(b[0])
        elif type(dict[i])==str:
            a=float(dict[i])
            a=a*100
            x[i]=a
    y=y+list(x.keys())
    z=z+list(x.values())
    #print(z)
    #print(len(z), len(y))

    # Normalize data to fit within the range [0, 1]
    max_stat = max(z)
    normalized_stats = [stat / max_stat for stat in z]

    # Number of categories
    num_categories = len(y)

    # Step 2: Calculate the angle for each category
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
    # Step 3: Close the plot
    normalized_stats += [normalized_stats[0]]
    angles += [angles[0]]
    # Step 4: Create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    # Plot the data
    ax.plot(angles, normalized_stats, 'o-', linewidth=2, color='#007acc', markersize=8, alpha=0.7)
    ax.fill(angles, normalized_stats, color='#007acc', alpha=0.3)

    # Set category labels on the plot with clear font
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(y, fontsize=12, weight='bold')

    # Add lines connecting data points to the center
    for i in range(num_categories):
        ax.plot([angles[i], angles[i]], [0, normalized_stats[i]], color='gray', linestyle='dashed', linewidth=1)

    # Set radial gridlines
    ax.set_yticklabels([])
    ax.set_rlabel_position(0)

    # Add labels to data points with a bit of offset
    label_offset = 0.1
    for i in range(num_categories):
        angle_rad = angles[i]
        x = angle_rad + np.pi / 2 if angle_rad < np.pi else angle_rad - np.pi / 2
        y = normalized_stats[i] + label_offset
        ax.text(angle_rad, normalized_stats[i] + 0.40, f'{z[i]:.2f}', fontsize=10, ha='center', va='center')

    # Step 6: Display the plot
    #plt.legend()
    plt.title(f'Player Performance {name}', size=16, weight='bold', color='#333333')

    # Export the radar chart as a JPEG image
    plt.savefig(f'{name}.jpg', dpi=300, bbox_inches='tight')
    plt.show()
    break