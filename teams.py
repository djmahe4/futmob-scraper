import requests
dict=[]

headers = {
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Referer': 'https://www.fotmob.com/matches/east-bengal-fc-vs-kerala-blasters-fc/3j39c35b',
    'x-fm-req': 'eyJib2R5Ijp7ImNvZGUiOjE2OTk3NTY2ODI4OTB9LCJzaWduYXR1cmUiOiJCODJGQTU1QzEyQzY3NzhGQzI4OEI5NThFQjVGMTRFMiJ9',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'leagueId': '9478',
    'teams': '[165184,578654]',
}

response = requests.get('https://www.fotmob.com/api/tltable', params=params, headers=headers)
table=response.json()
for i in table:
    x=(i["data"])
    z=(x["table"])
    u=z['all']
    for i in u:
        w = {'name': i['name'], 'id': i['id'],'url':f"https://www.fotmob.com{i['pageUrl']}"}
        dict.append(w)
    #v=u[0]
    #print(v)
    #w={'name':v['name'], 'id':v['id']}
print(dict)
