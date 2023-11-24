import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

def analyze_player_stats(stats,id):
    file=open(f"{id}/stats.txt","w")
    for i in stats["Player"]:
        analysis = f"{i}:\n"
        x=stats["Player"].index(i)
        isgoalie=False

        # Positive aspects
        analysis += "\nPositive Aspects:\n"
        if 'expected_goals_on_target_faced' in stats and stats['expected_goals_on_target_faced'][x] < 0.5 and stats['expected_goals_on_target_faced'][x] != 0:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to face few on-target shots ({stats['expected_goals_on_target_faced'][x]} xGOTF).\n"
            isgoalie=True
        if stats['rating_title'][x] > 7.0:
            analysis += "- Impressive overall performance.\n"
        if stats['chances_created'][x] > 0:
            analysis += f"- Created {stats['chances_created'][x]} chances.\n"
        if 'expected_goals'in stats  and stats['expected_goals'][x] > 0.5:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to score goals ({stats['expected_goals'][x]} xG).\n"
        if 'expected_goals_on_target_variant' in stats and stats['expected_goals_on_target_variant'][x] > 0.3:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to have on-target shots ({stats['expected_goals_on_target_variant'][x]} xGOT).\n"
        if stats['passes_into_final_third'][x] >= 6:  # Adjust this threshold based on your criteria
            analysis += f"- Successfully passed into the final third ({stats['passes_into_final_third'][x]} passes into final third).\n"
        if 'expected_goals_non_penalty' in stats and stats["expected_goals_non_penalty"] > 0.2:  # Adjust this threshold based on your criteria
            analysis += f"- Was Dangerous infront of goal ({stats['expected_goals_non_penalty'][x]} xGNP).\n"
        if 'expected_assists' in stats and stats['expected_assists'][x] > 0.2:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to provide assists ({stats['expected_assists'][x]} xA).\n"
        # ... add more positive aspects based on specific stats
        if stats['accurate_crosses'][x] > 30:  # Adjust this threshold based on your criteria
            analysis += f"- Successfully delivered accurate crosses ({stats['accurate_crosses'][x]}).\n"
        if stats['duel_won'][x] >= 5:  # Adjust this threshold based on your criteria
            analysis += f"- Duels Won {stats['duel_won'][x]}.\n"
        if stats['recoveries'][x] >= 4:  # Adjust this threshold based on your criteria
            analysis += f"- Made {stats['recoveries'][x]} recoveries.\n"
        if stats['dribbles_succeeded'][x] > 50:  # Adjust this threshold based on your criteria
            analysis += f"- Successfully completed {stats['dribbles_succeeded'][x]}% of dribbles attempted.\n"
        if stats['was_fouled'][x] >= 4:  # Adjust this threshold based on your criteria
            analysis += f"- Was fouled {stats['was_fouled'][x]} times, drawing fouls.\n"
        if 'goals_prevented' in stats and stats['goals_prevented'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Prevented {stats['goals_prevented'][x]} goals.\n"
        if 'blocked_shots' in stats and stats['blocked_shots'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Blocked {stats['blocked_shots'][x]} shots.\n"
        if stats['tackles_succeeded'][x] >50 :
            analysis += f"- Tackles success rate: {stats['tackles_succeeded'][x]}%.\n"
        if stats['touches'][x] > 48:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['touches'][x]} touches, indicating active involvement in the game.\n"
        if stats['clearances'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Made {stats['clearances'][x]} clearances.\n"
        if stats['accurate_passes'][x] > 70:
            analysis += f"- Had Good accuracy in passing ({stats['accurate_passes'][x]}% accuracy).\n"
        if stats['defensive_actions'][x]> 0:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['defensive_actions'][x]} defensive action(s) during the game.\n"
        if stats['duel_lost'][x] == 0:  # Adjust this threshold based on your criteria
            analysis += f"- Lost {stats['duel_lost'][x]} duels.\n"
        if stats['ground_duels_won'][x] > 50:  # Adjust this threshold based on your criteria
            analysis += f"- Won {stats['ground_duels_won'][x]}% ground duels.\n"
        if stats['saves'][x] >= 50:
            analysis += f"- Good Save percentage: {stats['saves'][x]}%\n"
        if stats['shot_accuracy'][x] > 0:
            analysis += f"- Shot accuracy: {stats['shot_accuracy'][x]}%\n"
        if stats['touches_opp_box'][x] >= 5:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['touches_opp_box'][x]} touches in the opponent's box.\n"
        if stats['interceptions'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Made {stats['interceptions'][x]} interceptions.\n"
        if stats['aerials_won'][x] > 50:  # Adjust this threshold based on your criteria
            analysis += f"- Aeriels won {stats['aerials_won'][x]}%.\n"
        if stats['long_balls_accurate'][x] > 60 and stats['long_balls_accurate'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- Succesfull in playing accurate long balls ({stats['long_balls_accurate'][x]}% accuracy).\n"

        # Negative aspects
        analysis += "\nNegative Aspects:\n"
        if 'expected_goals_on_target_faced' in stats and stats['expected_goals_on_target_faced'][x] < 2.0 and  stats['expected_goals_on_target_faced'][x]!= 0:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to face high on-target shots ({stats['expected_goals_on_target_faced'][x]} xGOTF).\n"
            isgoalie=True
        if stats['rating_title'][x] < 6.0:
            analysis += "- Poor performance.\n"
        if stats['minutes_played'][x] <= 45:
            analysis += f"- Had Less game time ({stats['minutes_played'][x]} minutes played).\n"
        if stats['accurate_passes'][x] < 40:
            analysis += f"- Low accuracy in passing ({stats['accurate_passes'][x]}% accuracy).\n"
        # ... add more negative aspects based on specific stats
        if 'expected_goals' in stats and stats['expected_goals'][x] < 0.1 and stats['expected_goals'][x]!= 0:  # Adjust this threshold based on your criteria
            analysis += f"- Failed to generate significant goal-scoring opportunities ({stats['expected_goals'][x]} xG).\n"
        if stats['accurate_crosses'][x] < 30 and stats['accurate_crosses'][x] != 0: # Adjust this threshold based on your criteria
            analysis += f"- Crosses were not accurate enough ({stats['accurate_crosses'][x]}).\n"
        if stats['long_balls_accurate'][x] < 30 and stats['long_balls_accurate'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- Ineffective in playing accurate long balls ({stats['long_balls_accurate'][x]}% accuracy).\n"
        if stats['recoveries'][x] < 4:  # Adjust this threshold based on your criteria
            analysis += f"- Made insufficient ball recoveries ({stats['recoveries'][x]} recoveries).\n"
        if stats['dribbles_succeeded'][x] < 50 and stats['dribbles_succeeded'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- completed a low percentage of dribbles attempted ({stats['dribbles_succeeded'][x]}%).\n"
        if 'goals_prevented' in stats and stats['goals_prevented'][x] < 0:  # Adjust this threshold based on your criteria
            analysis += f"- Prevented {stats['goals_prevented'][x]} goals.\n"
        if stats['touches'][x] < 30:  # Adjust this threshold based on your criteria
            analysis += f"- Had {stats['touches'][x]} touches, indicating less involvement in buildups.\n"
        if stats['dispossessed'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Was Dispossessed {stats['dispossessed'][x]} times.\n"
        if isgoalie==False and stats['defensive_actions'][x] == 0:  # Adjust this threshold based on your criteria
            analysis += f"- Was not active in any defensive action during the game.\n"
        if stats['duel_lost'][x] > 5:  # Adjust this threshold based on your criteria
            analysis += f"- Lost {stats['duel_lost'][x]} duels.\n"
        if isgoalie==False and stats['ground_duels_won'][x] < 50:  # Adjust this threshold based on your criteria
            analysis += f"- Won only {stats['ground_duels_won'][x]}% ground duels.\n"
        if 'big_chance_missed_title' in stats and stats['big_chance_missed_title'][x] > 0:
            analysis += f"- Missed {stats['big_chance_missed_title'][x]} big chances.\n"
        if 'Offsides' in stats and stats['Offsides'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Caught offside {stats['Offsides'][x]} times.\n"
        if stats['dribbled_past'][x] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Was Dribbled past {stats['dribbled_past'][x]} times.\n"
        if stats['aerials_won'][x] < 50 and stats['aerials_won'][x] !=0:  # Adjust this threshold based on your criteria
            analysis += f"- Aeriels won is only {stats['aerials_won'][x]}%.\n"
        if stats['saves'][x] < 50 and stats['saves'][x]:
            analysis += f"- Save percentage: {stats['saves'][x]}%\n"


        # ... add more negative aspects based on specific stats

        # Overall Influence
            # Overall Influence
        analysis += "\nOverall Influence:\n"
        if (stats['rating_title'][x] > 7.0 and
                (stats['chances_created'][x] > 2 or
                #stats['expected_goals'][x] > 0.5 or
                #stats['expected_goals_on_target_variant'][x] > 0.3 or
                stats['passes_into_final_third'][x] > 10 or
                #stats['expected_goals_non_penalty'][x] > 0.2 or
                #stats['expected_assists'][x] > 0.2 or
                stats['accurate_crosses'][x] > 50 or
                (stats['duel_won'][x] >= 5 and stats['duel_lost'][x] < 5 ) or
                stats['dribbles_succeeded'][x] >= 75 or
                stats['long_balls_accurate'][x] > 75 or
                stats['touches_opp_box'][x] > 5 or
                stats['recoveries'][x] > 10)):
            analysis += "- Overall, a highly influential performance on the pitch.\n\n"
        elif stats['rating_title'][x] < 6.0:
            analysis += "- Needs improvement.\n\n"
        else:
            analysis += "- A performance with both positive and negative aspects.\n\n"

        file.write(analysis)
    file.close()

def headtohead(id,teams):
    file=open("impstats.json",'r')
    x=json.load(file)
    t1=[]
    t2=[]
    keys=list(x.keys())
    for i in x:
        t1.append(x[i][0])
        t2.append(x[i][1])
    #print(t1)
    for i in t1:
        if i==None:
            c = t1.index(i)
            t1[c]=0
        #elif i==True or i==False:
            #t1.pop(t1.index(i))
        elif type(i)==str and "(" in i:
            a=i.split("(")
            b=a[0].split('%')
            c=t1.index(i)
            t1[c]=float(b[0])
        elif type(i)==str:
            a=float(i)
            b=t1.index(i)
            t1[b]=a
    for i in t2:
        if i==None:
            c=t2.index(i)
            t2[c]=0
        #elif i==True or i==False:
            #t2.pop(t2.index(i))
        elif type(i)==str and "(" in i:
            a=i.split("(")
            b=a[0].split('%')
            c=t2.index(i)
            t2[c]=float(b[0])
        elif type(i)==str:
            a=float(i)
            b=t2.index(i)
            t2[b]=a
    #print(t1)
    #print(t2)
    for i in teams:
        teamname=i
        if teams.index(i)==0:
            z=t1
        else:
            z=t2
        # Normalize data to fit within the range [0, 1]
        max_stat = max(z)
        normalized_stats = [stat / max_stat for stat in z]

        # Number of categories
        num_categories = len(keys)

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
        ax.set_xticklabels(keys, fontsize=5, weight='bold')

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
            ax.text(angle_rad, normalized_stats[i] + random.uniform(0.30,0.50), f'{z[i]:.2f}', fontsize=6, ha='center', va='center')

        plt.title(f'Team stats {teamname}', size=16, weight='bold', color='#333333')
        plt.savefig(f'{id}/{teamname}.jpg', dpi=300, bbox_inches='tight')
    file.close()