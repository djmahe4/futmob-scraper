import requests
from datetime import date
import json

x=date.today()
y=str(x).split('-')
z=''
for i in y:
    z=z+i

cookies = {
    'u:location': '%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%22111.92.78.166%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D',
    '_ga': 'GA1.1.948230614.1700192035',
    '_hjSessionUser_2585474': 'eyJpZCI6IjE5NTIyMWQ3LTVjNjctNTZhMS04M2RmLTlkNTYzYTdhNGE1MCIsImNyZWF0ZWQiOjE3MDAxOTIwMzQxNDAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjIncludedInSessionSample_2585474': '0',
    '_hjSession_2585474': 'eyJpZCI6Ijg4MTZiODk1LWMwOTMtNDcwNS05MTg4LWQ0ZGFhM2U4OTg3YSIsImNyZWF0ZWQiOjE3MDAyMTgwMzI0MjQsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '__gads': 'ID=4a53b611dd8f2f33:T=1700192043:RT=1700218034:S=ALNI_MZ7af194OUe5cYcxUmjBR-_v_HLyw',
    '__gpi': 'UID=00000c8acce475e6:T=1700192043:RT=1700218034:S=ALNI_MZ-Y_BwyFNtH9dxlC_BaZ9_UJKBVg',
    '_ga_G0V1WDW9B2': 'GS1.1.1700217085.2.1.1700218036.56.0.0',
    'FCNEC': '%5B%5B%22AKsRol-61bjGXTm8QMYeD92wJtrXKIcUB3fkuYg_Iw5U2r4-k7roeKq36J3zIgpb8BlduaNRS_IByXzC69EVh7xVDn5zST0JvOgQ6kMhrNhySYQ9muHo6cFGDQAH90BJudlFaMD2f0wweyZXuUSzIbD6imGfcXlmKg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
    'g_state': '{"i_p":1700225255791,"i_l":1}',
}

headers = {
    'authority': 'www.fotmob.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'u:location=%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%22111.92.78.166%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D; _ga=GA1.1.948230614.1700192035; _hjSessionUser_2585474=eyJpZCI6IjE5NTIyMWQ3LTVjNjctNTZhMS04M2RmLTlkNTYzYTdhNGE1MCIsImNyZWF0ZWQiOjE3MDAxOTIwMzQxNDAsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_2585474=0; _hjSession_2585474=eyJpZCI6Ijg4MTZiODk1LWMwOTMtNDcwNS05MTg4LWQ0ZGFhM2U4OTg3YSIsImNyZWF0ZWQiOjE3MDAyMTgwMzI0MjQsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=0; __gads=ID=4a53b611dd8f2f33:T=1700192043:RT=1700218034:S=ALNI_MZ7af194OUe5cYcxUmjBR-_v_HLyw; __gpi=UID=00000c8acce475e6:T=1700192043:RT=1700218034:S=ALNI_MZ-Y_BwyFNtH9dxlC_BaZ9_UJKBVg; _ga_G0V1WDW9B2=GS1.1.1700217085.2.1.1700218036.56.0.0; FCNEC=%5B%5B%22AKsRol-61bjGXTm8QMYeD92wJtrXKIcUB3fkuYg_Iw5U2r4-k7roeKq36J3zIgpb8BlduaNRS_IByXzC69EVh7xVDn5zST0JvOgQ6kMhrNhySYQ9muHo6cFGDQAH90BJudlFaMD2f0wweyZXuUSzIbD6imGfcXlmKg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; g_state={"i_p":1700225255791,"i_l":1}',
    'if-none-match': '"96plnqf6oxvef"',
    'referer': 'https://www.fotmob.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-fm-req': 'eyJib2R5Ijp7ImNvZGUiOjE3MDAyMTgxMjE2NTl9LCJzaWduYXR1cmUiOiJFMkI1QzUwRkRFRDlBNjRCNzhBODI3NDk0QzRCQjRFQiJ9',
}

params = {
    'date': f'{z}',
    'timezone': 'Asia/Calcutta',
    'ccode3': 'IND',
}
response = requests.get('https://www.fotmob.com/api/matches', params=params, cookies=cookies, headers=headers)
yes=response.json()

a=yes["leagues"]
b=[]
for i in a:
    #print(i.keys())
    c=[i['name'],i['matches']]
    leagueid=i['id']
    matches=[]
    for x in i['matches']:
        score=[]
        matchid=x['id']
        d=x['home']
        hname=d['longName']
        score.append(d['score'])
        e=x['away']
        aname=e['longName']
        score.append(e['score'])
        teams=[hname,aname]
        matches.append({matchid:[teams,score]})
    b.append({leagueid:matches})
    with open("leagues.txt",'w') as file:
        json.dump(b, file, indent=2)
file.close()
