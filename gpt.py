import requests
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from openai import analyze_player_stats,headtohead, subdataext
import json
import random


mainstats={}
records={}
rec=[]
view=[]
id=input("Enter id:")

headers = {
    #'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    #'Referer': 'https://www.fotmob.com/matches/east-bengal-fc-vs-kerala-blasters-fc/3j39c35b',
    #'x-fm-req': 'eyJib2R5Ijp7ImNvZGUiOjE2OTk3NTY2OTQ5NTJ9LCJzaWduYXR1cmUiOiIwQzdDMzRGQTczNjk2ODAwMzE0MjUwODI2QjBGRDY4QyJ9',
    #'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    #'sec-ch-ua-platform': '"Windows"',
}

params = {
    'matchId': f'{id}',
}

response = requests.get('https://www.fotmob.com/api/matchDetails', params=params, headers=headers)
gem=response.json()
#for i in gem:
    #print(i)
a=gem["content"]
lin=a['lineup']
ben=lin['bench']
arr=ben['benchArr']
sub=arr[0]
for i in sub:
    if i["timeSubbedOn"]!=None and i["timeSubbedOn"]<90:
        subdataext(i,records)
#def substitute(dict):

#for i in a:
    #print(a[i],end="\n\n")
e1=a['liveticker']
extrac=e1["teams"]
#extrac=extrac["lineup"][0]
#print(extrac.keys())
teamnames=extrac
#extrac=extrac["lineup"][1]
#teamnames.append(extrac["teamName"])
print(teamnames)
b=a['stats']
c=b['Periods']
d=c['All']
e=d["stats"]
f=e[0]
#substitute(f)
g=f['stats']
for i in range(len(e)):
    f=e[i]
    g = f['stats']
    mainstats.update({f['key']:f['stats']})
stz = {}
with open("impstats.json", 'w') as file:
    ax=list(mainstats.keys())
    for i in range(len(mainstats)):
        j = mainstats[ax[i]]
        k=j[0]
        #print(j)
        for i in j:
            k=i["key"]
            l=i["stats"]
            print(k,l)
            x = stz.update({k: l})
    json.dump(stz,file)

def dataext(dict):
        for i in dict:
            for x in i:
                if None:
                    continue
                l=[]
                print(x.keys())
                position=x['positionStringShort']
                #fpos=x['role']
                name=x['name']
                fname=name['fullName']
                if 'stats'not in x.keys():
                    break
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
print(y)
#lineup=y['lineup'][0]
#ben1=lineup['bench']
dataext(y)
#dataext(ben1)
d=c[0]
e=d['players']
#ben2=lineup['bench']
#print(ben1)
dataext(e)
#dataext(ben2)

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
new_rec={}
for i in records:
    name=i
    pos=records[i][0]
    dict=records[i][1]
    rating=dict["rating_title"]
    x = dict.copy()
    x.update({"rating_title" : rating})
    print(x)
    z = []
    y=[]
    print(name)
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
            a=a
            x[i]=a
    #insights = prompt(name, pos, dict)
    #print(insights)
    new_rec[name] = x
    y=y+list(x.keys())
    z=z+list(x.values())
    #print(z)
    #print(len(z), len(y))
    #continue

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
    ax.set_xticklabels(y, fontsize=10, weight='bold')

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
        ax.text(angle_rad, normalized_stats[i] + random.uniform(0.30,0.50), f'{z[i]:.2f}', fontsize=8, ha='center', va='center')

    # Step 6: Display the plot
    #plt.legend()
    plt.title(f'Player Performance {name}', size=16, weight='bold', color='#333333')
    directory_path = f'{id}'
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    new_jpg_path = os.path.join(directory_path, f'{name}.jpg')

    # Export the radar chart as a JPEG image
    plt.savefig(f'{name}.jpg', dpi=300, bbox_inches='tight')
    # Replace 'sample_image.jpg' with the actual path to your existing JPG file
    shutil.copy(f'{name}.jpg', new_jpg_path)
    file_to_delete = f'{name}.jpg'
    # Check if the file exists before attempting to delete
    if os.path.exists(file_to_delete):
        # Delete the file
        os.remove(file_to_delete)
print(new_rec)
# Extracting keys (players) and values (player stats) from the given data
players = list(new_rec.keys())
#player_stats = list(new_rec.values())

# Creating the desired format
formatted_data = {
    "Player": players,
}
# Extract all unique stat names across all players
all_stats = set(stat for stats in new_rec.values() for stat in stats)

# Iterate through stats and add them to formatted_data
for stat_name in all_stats:
    if all(stat_name not in stats or stats[stat_name] == 0 for stats in new_rec.values()):
        continue
    formatted_data[stat_name] = [stats.get(stat_name, 0) for stats in new_rec.values()]

# Print the formatted data
print(formatted_data)
analyze_player_stats(formatted_data,id)
headtohead(id,teamnames)
