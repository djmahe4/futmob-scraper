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
import seaborn as sns


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
directory_path = f'{id}'
# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
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
e1=gem['header']
extrac=e1["teams"]
tm1=extrac[0]['name']
tm2=extrac[1]['name']
score=[extrac[0]['score'],extrac[1]['score']]
print(score)
#extrac=extrac["lineup"][0]
#print(extrac.keys())
teamnames=[tm1,tm2]
headtohead(id,teamnames,score)
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
        #print(j)
        k=j[0]
        for i in j:
            k=i["key"]
            l=i["stats"]
            print(k,l)
            x = stz.update({k: l})
    json.dump(stz,file)

def dataext(dic):
        for i in dic:
            for x in i:
                if None:
                    continue
                l=[]
                #print(x.keys())
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
                    y.update({i:x['value']})

                l=[position,y]
                #print(fname)
                #dict[fname]=l
                #rec.append(list(dict))
                records.update({fname:l})


b=a["lineup"]
c=b['lineup']
x=c.pop()
y=x['players']
#print(y)
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
new_rec={}
# Create a color palette
colors=sns.color_palette("husl", 12)
for i in records:
    name=i
    pos=records[i][0]
    dic=records[i][1]
    #dic.pop("fantasy_points")
    try:
        rating=dic["rating_title"]
    except KeyError:
        rating=None
    x = dic.copy()
    x.update({"rating" : rating})
    print(x)
    z = []
    y=[]
    print(name)
    ls={}
    for i in dic:
        if type(dic[i])==None:
            x.pop(i)
        elif dic[i]==True or dic[i]==False:
            x.pop(i)
        elif type(dic[i])==str and "(" in dic[i]:
            a=dic[i].split("(")
            b=a[1].split("%")
            x[i]=float(b[0])
            ls.update({i:a[0]})
        elif type(dic[i])==str:
            a=float(dic[i])
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
    real=z.copy()
    zc=z.copy()
    # Normalize data to fit within the range [0, 1]
    for i in z:
        ind = zc.index(i)
        if i==None:
            zc.pop(ind)
            y.pop(ind)
            real.pop(ind)
        elif i<=0.1:
            zc.pop(ind)
            y.pop(ind)
            real.pop(ind)
        elif i<1:
            zc[ind]=i*100
        elif i<10:
            zc[ind]=i*10
    #min_stat = min(z)
    color1, color2, color3 = random.sample(colors, 3)
    max_stat = max(zc)
    normalized_stats = [(stat- 0) / (max_stat-0) for stat in zc]

    # Number of categories
    for i in y:
        ind=y.index(i)
        if i=='FotMob rating':
            y[ind]='rating'
    num_categories = len(y)

    # Step 2: Calculate the angle for each category
    angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
    # Step 3: Close the plot
    normalized_stats += [normalized_stats[0]]
    angles += [angles[0]]
    # Step 4: Create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    #ax.set_ylim(0, 0.8)

    # Plot the data
    #color = random.choice(colors)
    # Create the plot with the new colors
    ax.plot(angles, normalized_stats, 'o-', linewidth=2, color=color1, markersize=8, alpha=0.7)
    ax.fill(angles, normalized_stats, color=color1, alpha=0.3)

    #ax.set_aspect("equal")
    ax.margins(len(y)/30)

    # Set category labels on the plot with clear font
    ax.set_xticks(angles[:-1])
    #colour2=random.choice(colors)
    ax.set_xticklabels(y,fontsize=6,weight='bold',color=color2, rotation_mode="anchor")
    #ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)  # Make xticks invisible


    #textbox
    colour3=random.choice(colors)
    for i  ,(angle,stat,label) in enumerate (zip(angles,real,y)):
        x=angle+np.pi/2 if angle <np.pi else angle - np.pi / 2
        y=normalized_stats[i] +0.355
        # Check if stat is an integer
        if type(stat)==int:
            text = f"{int(stat)}"
        else:
            text = f"{float(stat)}"
        ax.text(angle, y, text, fontsize=8, ha='center', va='center', color=color3,
                bbox=dict(boxstyle='square', facecolor='white'))
    # Set radial gridlines
    #ax.set_yticklabels([])
    #ax.set_rlabel_position(0)



    # Add watermark with Twitter handle
    plt.text(-0.05, -0.05, '@DJMahe04', fontsize=12, ha='center', va='center', alpha=0.2, transform=ax.transAxes)

    # Create a string with the keys and values from 'ls'
    ls_text = "\n".join(f"{k}: {v}" for k, v in ls.items())

    # Add the text box to the plot
    ax.text(1.2, 0.25, ls_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.4))

    # Step 6: Display the plot
    #plt.legend()
    plt.title(f'Player Performance {name} ({pos})', size=16, weight='bold', color='#333333')
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
    #break
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
    #if all(stat_name not in stats or stats[stat_name] == 0 for stats in new_rec.values()):
        #continue
    formatted_data[stat_name] = [stats.get(stat_name, 0) for stats in new_rec.values()]

# Print the formatted data
with open("stats.json","w",encoding='utf-8') as file:
    json.dump(formatted_data,file, ensure_ascii=False)
print(formatted_data)
analyze_player_stats(formatted_data,id)
