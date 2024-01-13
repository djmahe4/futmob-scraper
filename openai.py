import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import csv
import seaborn as sns

def subdataext(dict,records):
    l=[]
    x=dict
    print(x)
    position=x['role']
                #fpos=x['role']
    name=x['name']
    fname=name['fullName']
    stats=x['stats']

    stats0=stats[:]
    #print(stats0)
    rstats={}
    for i in range(len(stats0)):
        stats00=stats0[i]
        x=stats00['stats']
        #print(x)
        #if x['minutes_played']<=0:
            #break
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

def analyze_player_stats(stats,id):
    file=open(f"{id}/stats.txt","w")
    for i in stats["Player"]:
        analysis = f"{i}:\n"
        x=stats["Player"].index(i)
        isgoalie=False

        # Positive aspects
        analysis += "\n+ves:\n"
        if 'xGOT faced' in stats and stats['xGOT faced'][x] < 0.5 and stats['xGOT faced'][x] != 0:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to face few on-target shots ({stats['xGOT faced'][x]} xGOTF)\n"
            isgoalie=True
        #if stats['rating_title'][x] > 7.0:
            #analysis += "- Impressive overall performance.\n"
        if stats['Chances created'][x] in stats and stats['Chances created'][x] > 0:
            analysis += f"- Created {stats['Chances created'][x]} chances\n"
        if 'Expected goals (xG)' in stats  and stats['Expected goals (xG)'][x] > 0.5:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to score goals ({stats['Expected goals (xG)'][x]} xG)\n"
        if 'goals' in stats and stats['goals'][x] > 0:
            analysis += f"- {stats['goals'][x]} goals\n"
        if 'assists' in stats and stats['assists'][x] > 0:
            analysis += f"- {stats['assists'][x]} assists\n"
        if 'Expected goals on target (xGOT)' in stats and stats['Expected goals on target (xGOT)'][x] > 0.3:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to score on-target shots ({stats['Expected goals on target (xGOT)'][x]} xGOT)\n"
        if stats['Passes into final third'][x] >= 6:  # Adjust this threshold based on your criteria
            analysis += f"- Successfully passed into the final third ({stats['Passes into final third'][x]} times)\n"
        if 'xG Non-penalty' in stats and stats["xG Non-penalty"][x] > 0.2:  # Adjust this threshold based on your criteria
            analysis += f"- Was Dangerous infront of goal ({stats['xG Non-penalty'][x]} xGNP)\n"
        if 'Expected assists (xA)' in stats and stats['Expected assists (xA)'][x] > 0.2:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to provide assists ({stats['Expected assists (xA)'][x]} xA)\n"
        # ... add more positive aspects based on specific stats
        if stats['Accurate crosses'][x] > 30:  # Adjust this threshold based on your criteria
            analysis += f"- Successfully delivered accurate crosses ({stats['Accurate crosses'][x]})\n"
        if stats['Duels won'][x] >= 5:  # Adjust this threshold based on your criteria
            analysis += f"- Duels Won {stats['Duels won'][x]}\n"
        if stats['Recoveries'][x] >= 4:  # Adjust this threshold based on your criteria
            analysis += f"- Made {stats['Recoveries'][x]} recoveries\n"
        if stats['Successful dribbles'][x] > 50:  # Adjust this threshold based on your criteria
            analysis += f"- Successfully completed {stats['Successful dribbles'][x]}% of dribbles attempted\n"
        if stats['Was fouled'][x] in stats and stats['Was fouled'][x] >= 4:  # Adjust this threshold based on your criteria
            analysis += f"- Was fouled {stats['Was fouled'][x]} times, drawing fouls\n"
        if 'Goals prevented' in stats and stats['Goals prevented'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Prevented {stats['Goals prevented'][x]} goals\n"
        if 'Blocks' in stats and stats['Blocks'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Blocked {stats['Blocks'][x]} shots\n"
        if stats['Tackles won'][x] >50 :
            analysis += f"- Tackles success rate: {stats['Tackles won'][x]}%\n"
        if stats['Touches'][x] > 48:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['Touches'][x]} touches, indicating active involvement in the game\n"
        if stats['Clearances'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Made {stats['Clearances'][x]} clearances\n"
        if stats['Accurate passes'][x] > 70:
            analysis += f"- Had Good accuracy in passing ({stats['Accurate passes'][x]}% accuracy)\n"
        if stats['Defensive actions'][x]> 0:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['Defensive actions'][x]} defensive action(s) during the game\n"
        if stats['Duels lost'][x] == 0:  # Adjust this threshold based on your criteria
            analysis += f"- Lost {stats['Duels lost'][x]} duels\n"
        if stats['Ground duels won'][x] > 50:  # Adjust this threshold based on your criteria
            analysis += f"- Won {stats['Ground duels won'][x]}% ground duels\n"
        if stats['Saves'][x] >= 50:
            analysis += f"- Good Save percentage: {stats['Saves'][x]}%\n"
        if stats['Shot accuracy'][x] > 0:
            analysis += f"- Shot accuracy: {stats['Shot accuracy'][x]}%\n"
        if stats['Touches in opposition box'][x] >= 5:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['Touches in opposition box'][x]} touches in the opponent's box\n"
        if stats['Interceptions'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Made {stats['Interceptions'][x]} interceptions\n"
        if stats['Aerial duels won'][x] > 50:  # Adjust this threshold based on your criteria
            analysis += f"- Aeriels won {stats['Aerial duels won'][x]}%\n"
        if stats['Accurate long balls'][x] > 60 and stats['Accurate long balls'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- Succesfull in playing accurate long balls ({stats['Accurate long balls'][x]}% accuracy)\n"

        # Negative aspects
        analysis += "\n-ves:\n"
        if 'xGOT faced' in stats and stats['xGOT faced'][x] > 0.5 and  stats['xGOT faced'][x]!= 0:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to face high on-target shots ({stats['xGOT faced'][x]} xGOTF)\n"
            isgoalie=True
        if stats['FotMob rating'][x] < 6.0:
            analysis += "- Poor performance.\n"
        if stats['Minutes played'][x] <= 45:
            analysis += f"- Had Less game time ({stats['Minutes played'][x]} minutes played)\n"
        if stats['Accurate passes'][x] < 40:
            analysis += f"- Low accuracy in passing ({stats['Accurate passes'][x]}% accuracy)\n"
        # ... add more negative aspects based on specific stats
        if 'Expected goals (xG)' in stats and stats['Expected goals (xG)'][x] < 0.1 and stats['Expected goals (xG)'][x]!= 0:  # Adjust this threshold based on your criteria
            analysis += f"- Failed to generate significant goal-scoring opportunities ({stats['Expected goals (xG)'][x]} xG)\n"
        if stats['Accurate crosses'][x] < 40 and stats['Accurate crosses'][x] != 0: # Adjust this threshold based on your criteria
            analysis += f"- Crosses were not accurate enough ({stats['Accurate crosses'][x]})\n"
        if stats['Accurate long balls'][x] < 40 and stats['Accurate long balls'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- Ineffective in playing accurate long balls ({stats['Accurate long balls'][x]}% accuracy)\n"
        if stats['Recoveries'][x] < 4:  # Adjust this threshold based on your criteria
            analysis += f"- Made insufficient ball recoveries ({stats['Recoveries'][x]} recoveries)\n"
        if stats['Successful dribbles'][x] < 50 and stats['Successful dribbles'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- completed a low percentage of dribbles attempted ({stats['Successful dribbles'][x]}%)\n"
        if 'Goals prevented' in stats and stats['Goals prevented'][x] < 0:  # Adjust this threshold based on your criteria
            analysis += f"- Prevented {stats['Goals prevented'][x]} goals\n"
        if stats['Touches'][x] < 25:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['Touches'][x]} touches, indicating less involvement in buildups\n"
        if stats['Dispossessed'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Was Dispossessed {stats['Dispossessed'][x]} times\n"
        if isgoalie==False and stats['Defensive actions'][x] == 0:  # Adjust this threshold based on your criteria
            analysis += f"- Was not active in any defensive action during the game\n"
        if stats['Duels lost'][x] > 4:  # Adjust this threshold based on your criteria
            analysis += f"- Lost {stats['Duels lost'][x]} duels\n"
        if isgoalie==False and stats['Ground duels won'][x] < 50:  # Adjust this threshold based on your criteria
            analysis += f"- Won only {stats['Ground duels won'][x]}% ground duels\n"
        if 'big_chance_missed_title' in stats and stats['big_chance_missed_title'][x] > 0:
            analysis += f"- Missed {stats['big_chance_missed_title'][x]} big chances\n"
        if 'Offsides' in stats and stats['Offsides'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Caught offside {stats['Offsides'][x]} times\n"
        if stats['Dribbled past'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Was Dribbled past {stats['Dribbled past'][x]} times\n"
        if stats['Aerial duels won'][x] < 50 and stats['Aerial duels won'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- Aeriels won is only {stats['Aerial duels won'][x]}%\n"
        if stats['Saves'][x] < 50 and stats['Saves'][x]:
            analysis += f"- Save percentage: {stats['Saves'][x]}%\n"
        if stats['Goals conceded'][x]>0 :
            analysis += f"- Conceeded {stats['Goals conceded'][x]} goals\n"


        # ... add more negative aspects based on specific stats

        # Overall Influence
            # Overall Influence
        analysis += "\nOverall Influence:\n"
        if (stats['FotMob rating'][x] > 7.0 and
                (#stats['chances_created'][x] > 2 or
                #stats['expected_goals'][x] > 0.5 or
                #stats['expected_goals_on_target_variant'][x] > 0.3 or
                stats['Passes into final third'][x] > 10 or
                #stats['expected_goals_non_penalty'][x] > 0.2 or
                #stats['expected_assists'][x] > 0.2 or
                stats['Accurate crosses'][x] > 50 or
                (stats['Duels won'][x] >= 5 and stats['Duels lost'][x] < 5 ) or
                stats['Successful dribbles'][x] >= 75 or
                stats['Accurate long balls'][x] > 75 or
                stats['Touches in opposition box'][x] > 5 or
                stats['Recoveries'][x] > 10)):
            analysis += "- Overall, a highly influential performance on the pitch\n\n"
        elif stats['FotMob rating'][x] < 6.0:
            analysis += "- Needs improvement\n\n"
        else:
            analysis += "- A performance with both positive and negative aspects\n\n"

        file.write(analysis)
    file.close()

def headtohead(id,teams,score):
    file=open("impstats.json",'r')
    x=json.load(file)
    t1=[]
    t2=[]
    rem=[]
    keys=list(x.keys())
    #for i in keys:
        #ind=keys.index(i)
        #y=i.split('_')
        #if len(x)==1:
            #keys[ind]=i
            #continue
        #elif "expected" in y:
            #a=y[1:]
            #b=""
            #for i in a:
                #b=b+i[0].upper()
            #keys[ind]=f'x{b}'
    for i in x:
        if x[i][0]==x[i][1]==0 or x[i][0]==x[i][1]==None:
            rem.append(i)
            continue
        t1.append(x[i][0])
        t2.append(x[i][1])
    for i in rem:
        keys.remove(i)
    #print(t1)
    ls1={}
    ls2={}
    for i in t1:
        c = t1.index(i)
        if i==None:
            t1[c]=0
        #elif i==True or i==False:
            #t1.pop(t1.index(i))
        elif type(i)==str and "(" in i:
            a=i.split("(")
            b=a[1].split('%')
            #c=t1.index(i)
            t1[c]=float(a[0])
            t1[c]=round(t1[c], 2)
            ls1.update({keys[c]: f"{b[0]}%"})
        elif type(i)==str:
            a=float(i)
            b=t1.index(i)
            t1[b]=round(a, 2)
    for i in t2:
        c = t2.index(i)
        if i == None:
            t2[c] = 0
        # elif i==True or i==False:
        # t1.pop(t1.index(i))
        elif type(i) == str and "(" in i:
            a = i.split("(")
            b = a[1].split('%')
            #c = t2.index(i)
            t2[c] = float(a[0])
            t2[c] = round(t2[c], 2)
            ls2.update({keys[c]: f"{b[0]}%"})
        elif type(i) == str:
            a = float(i)
            b = t2.index(i)
            t2[b] = round(a, 2)
    print(keys)
    val1=t1.copy()
    val2=t2.copy()
    val2 = [-abs(x) for x in val2]
    t2 = [-abs(x) for x in t2]
    #print(t1)
    #print(t2)

    # Create a figure and a set of subplots with increased size
    fig, ax = plt.subplots(figsize=(15, 15))  # Adjust as needed
    plt.style.use('ggplot')  # Use the 'ggplot' style
    # Set the y positions
    y_pos = np.arange(len(keys))

    # Create a color palette
    colors=sns.color_palette("bright")
    # Randomly select two distinct colors
    color1, color2 = random.sample(colors, 2)
    # Create the horizontal bars with the new colors
    bar1 = ax.barh(y_pos, t1, color=color1, label=f'{teams[0]}')
    bar2 = ax.barh(y_pos, t2, color=color2, label=f'{teams[1]}')

    # ... your existing code ...
    # Set the y-axis limits to make smaller bars appear larger
    #ax.set_xlim([-max(max(t1), max(t2)) * 1.2, max(max(t1), max(t2)) * 1.2])

    # Add the category names as y-tick labels with increased font size
    ax.set_yticks(y_pos)
    ax.set_yticklabels(keys, fontsize=12)  # Adjust as needed
    # Add gridlines
    ax.grid(True, linestyle='--', alpha=0.6)

    # Sort bars
    t1, t2, keys = zip(*sorted(zip(t1, t2, keys)))

        # Hide the y-axis values
    ax.yaxis.set_tick_params(length=0)

        # Add the stat values beside the bars
    for i, v in enumerate(val1):
        ax.text(v + 1, i, str(v), color='black', va='center')
    for i, v in enumerate(val2):
        ax.text(v - 1, i, str(abs(v)), color='black', va='center', ha='right')

        # Add watermark with Twitter handle
    plt.text(0.5, 0.5, '@DJMahe04', fontsize=14, ha='center', va='center', alpha=0.5, transform=ax.transAxes)
    # Create a string with the keys and values from 'ls'
    ls_text = "\n".join(f"{k}: {v}" for k, v in ls1.items())

    # Add the text box to the plot
    ax.text(0.8, -0.05, ls_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor=color1, alpha=0.5))
    # Create a string with the keys and values from 'ls'
    ls_text = "\n".join(f"{k}: {v}" for k, v in ls2.items())

    # Add the text box to the plot
    ax.text(0.1, -0.05, ls_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor=color2, alpha=0.5))
    ax.legend(loc='upper right')
    plt.title(f'[{score[1]}] {teams[1]} vs {teams[0]} [{score[0]}]', size=16, weight='bold', color='#333333')
    plt.savefig(f'{id}/team_comparison.jpg', dpi=100, bbox_inches='tight')
    file.close()
#id=int(input("enter id:"))
#teams=['team1','team2']
#headtohead(id,teams)
