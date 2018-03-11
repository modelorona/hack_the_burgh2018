import requests
import math
from enums import *

HOST = "http://localhost:6001/api/"

def get_all_player():
    players = requests.get(HOST+"players").json()    
    my = None
    others = []
    for player in players:
        if player['isConsolePlayer']:
            my = player
            continue
        
        others.append(player)
    return my,others

def get_my_player():
    return requests.get(HOST+"player").json()

def move(action,amount=10):
    requests.post(HOST+"player/actions",json={"type":action,"amount":amount})
def get_player_details(id):
    return requests.get(HOST+"players/"+str(id)).json()

def rad2deg(rad):
    return math.degrees(rad)


def get_closest_enemy(my,others):
    distances = []
    for other in others:
        distances.append(get_distance(my['position'],other['position']))
    
    return others[distances.index(sorted(distances)[0])]

def get_distance(my,other):
    return math.hypot(other['x'] - my['x'], other['y'] - my['y'])

def turn_to_point(my_player,other_player, isPlayer = True):    
    MY_POS , POS  = my_player['position'], other_player['position']
    rad_angle = math.atan2(MY_POS['y']-POS['y'],MY_POS['x']-POS['x'])
    deg_angle = rad2deg(rad_angle)
    norm_angle = deg_angle if deg_angle > 0 else deg_angle + 360
    remain = my_player['angle'] - norm_angle
    remain = remain if remain >=0 else remain + 360

    distance = get_distance(my_player['position'],other_player['position'])    
    print(distance)

    if remain < 185 and remain > 175 and distance < 200 and isPlayer:
        shoot()
        return

    

    if distance > 400:
        if remain > 180:
            move(Moves.RIGHT,Amount.FAST)
        else:
            move(Moves.LEFT,Amount.FAST)
    elif distance > 200:
        if remain > 180:
            move(Moves.RIGHT,Amount.MEDIUM)
        else:
            move(Moves.LEFT,Amount.MEDIUM)
    else:
        if remain > 180:
            move(Moves.RIGHT,Amount.WEEBIT)
        else:
            move(Moves.LEFT,Amount.WEEBIT)
    
def run_straight(amount):
    move(Moves.FORWARD,amount)

def run_backwards(amount):
    move(Moves.BACKWARD,amount)

def update_players(my_player,other_player):
    my_player = get_player_details(my_player['id'])
    other_player = get_player_details(other_player['id'])
    return my_player,other_player

def decide_where_to_move(distance):
    if distance > 500:
        run_straight(Amount.SAVAGE)        
    elif distance > 300:
        run_straight(Amount.MEDIUM)        
    elif distance > 200:
        run_straight(Amount.SLOW)
    else:
        run_backwards(Amount.SLOW)
        

def move_to_enemy(my_player,other_player):
    distance = get_distance(my_player['position'],other_player['position'])
    while distance > 100 and not is_enemy_dead(other_player):
        turn_to_point(my_player,other_player)
        decide_where_to_move(distance)
        my_player,other_player = update_players(my_player,other_player)        
        distance = get_distance(my_player['position'],other_player['position'])

def is_enemy_dead(player):
    player = requests.get(HOST+"players/"+str(player['id'])).json()
    if player['health'] <= 0:
        return True
    return False

def shoot():
    requests.post(HOST+"player/actions",json={"type":Moves.SHOOT,"amount":Amount.WEEBIT})    

def go_grab_object(my_player,obj):
    distance = get_distance(my_player['position'],obj['position'])
    while distance > 30:
        turn_to_point(my_player,obj,isPlayer=False)
        run_straight(Amount.SAVAGE)
        my_player = get_my_player()
        distance = get_distance(my_player['position'],obj['position'])
    
    if my_player['weapons'][obj['type']]:
        return True
    else:
        return False

def square_up(my_player):
    objects = requests.get(HOST+"world/objects").json()
    possible_pickups = []
    for obj in objects:
        if obj['type'] == GunType.SHOTGUN:
            possible_pickups.append(obj)

    closest_obj = sorted(possible_pickups,key=lambda x: x['distance'])[0]
    return go_grab_object(my_player,closest_obj)

