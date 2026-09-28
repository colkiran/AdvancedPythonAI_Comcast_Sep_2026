"""
dump - is used to write python serialized object into json formatted data
dumps - dumps is used to encode any python object into json formatted string
"""

import json

players = {
'players':[
        {'id': 'P101', 'Name': 'Sachin Tendulkar', 'Matches': 585, 'runs': 28500, 'age': 38},
        {'id': 'P102', 'Name': 'Sourav Ganguly', 'Matches': 430, 'runs': 19400, 'age': 36},
        {'id': 'P103', 'Name': 'Rahul Dravid', 'Matches': 390, 'runs': 18500, 'age': 35},
        {'id': 'P104', 'Name': 'Virendra Sehwag', 'Matches': 410, 'runs': 23500, 'age': 34},
        {'id': 'P105', 'Name': 'VVS Laxman', 'Matches': 298, 'runs': 15500, 'age': 36},
        {'id': 'P106', 'Name': 'Virar Kholi', 'Matches': 450, 'runs': 23000, 'age': 38},
        {'id': 'P107', 'Name': 'Yuvraj Singh', 'Matches': 520, 'runs': 19400, 'age': 36},
        {'id': 'P108', 'Name': 'MS Dhoni', 'Matches': 460, 'runs': 18500, 'age': 35},
        {'id': 'P109', 'Name': 'Md Kaif', 'Matches': 345, 'runs': 12400, 'age': 34},
        {'id': 'P110', 'Name': 'Suresh Raina', 'Matches': 410, 'runs': 15500, 'age': 36},
    ]
}

JFW = open("players.json", "w")
json.dump(players, JFW, indent=3)
JFW.close()

print("-" * 60)
player = {'name': 'Mike Tyson', 'age': 58, 'city': 'Los Angeles', 'Knockouts' :45}

print(f'player :{player}')
print(type(player))

print("-" * 60)
res = json.dumps(player)
print(res)
print(type(res))

