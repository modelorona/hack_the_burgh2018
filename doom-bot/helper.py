import requests
import math
from enums import *
import random

HOST = "http://localhost:6001/api/"

def is_enemy_dead(player):
    player = requests.get(HOST+"players/"+str(player['id'])).json()
    if player['health'] <= 0:
        return True
    return False

def get_all_player():
    players = requests.get(HOST+"players").json()    
    my = None
    others = []
    for player in players:
        if player['isConsolePlayer']:
            my = player
            continue
        
        if is_enemy_dead(player):
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

def turn_to_point(my_player,other_player,is_visible,isPlayer = True):    
    MY_POS , POS  = my_player['position'], other_player['position']
    if not is_visible:    
        rad_angle = math.atan2(MY_POS['y']-(POS['y']-650 if POS['y'] < 0 else POS['y'] + 650),MY_POS['x']-(POS['x']-650 if POS['x']<0 else POS['x']+650))        
    else:    
        rad_angle = math.atan2(MY_POS['y']-POS['y'],MY_POS['x']-POS['x'])
    deg_angle = rad2deg(rad_angle)
    norm_angle = deg_angle if deg_angle > 0 else deg_angle + 360
    remain = my_player['angle'] - norm_angle
    remain = remain if remain >=0 else remain + 360

    distance = get_distance(my_player['position'],other_player['position'])    

    if is_visible and distance < 200:
        shoot()

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
    # my_player = get_player_details(my_player['id'])
    # other_player = get_player_details(other_player['id'])
    my_player,other_players = get_all_player()
    other_player = get_closest_enemy(my_player,other_players)
    
    return my_player,other_player

CALLED = 0
DISTANCE = []
def is_still(distance):
    global CALLED,DISTANCE
    DISTANCE.append(distance)
    CALLED+=1
    if CALLED > 10:
        average = sum(DISTANCE)/len(DISTANCE)
        if abs(average - DISTANCE[0]) < 15:
            CALLED, DISTANCE = 0,[]            
            return True         
        CALLED, DISTANCE = 0,[]
        return False
    else:
        CALLED+=1
        return False

def decide_where_to_move(distance, is_visible = False):
    # if not is_visible and is_still(distance):
    #     move(Moves.BACKWARD,Amount.SAVAGE)
    #     return

    if distance > 400:
        run_straight(Amount.SAVAGE)        
    elif distance > 300:
        run_straight(Amount.MEDIUM)        
    elif distance > 200:
        run_straight(Amount.SLOW)
    else:
        run_backwards(Amount.SLOW)

def line_of_sight(my_player,other_player):
    try:
        is_visible = requests.get(HOST+"world/los/"+str(my_player['id'])+"/"+str(other_player['id'])).json()['los']
        return is_visible         
    except:
        return False

def move_to_enemy(my_player,other_player):
    distance = get_distance(my_player['position'],other_player['position'])
    while distance > 100 and not is_enemy_dead(other_player):
        is_visible = line_of_sight(my_player,other_player)        
        turn_to_point(my_player,other_player,is_visible= is_visible)
        decide_where_to_move(distance,is_visible=is_visible)
        my_player,other_player = update_players(my_player,other_player)        
        distance = get_distance(my_player['position'],other_player['position'])


def shoot():
    requests.post(HOST+"player/actions",json={"type":Moves.SHOOT,"amount":Amount.WEEBIT})    

def go_grab_object(my_player,obj,picking_weapon=True):
    distance = get_distance(my_player['position'],obj['position'])
    while distance > 30:
        is_visible = line_of_sight(my_player,obj)
        turn_to_point(my_player,obj,isPlayer=False,is_visible=is_visible)
        run_straight(Amount.SAVAGE)
        my_player = get_my_player()
        distance = get_distance(my_player['position'],obj['position'])
    
    if picking_weapon and my_player['weapons'][obj['type']]:
        return True
    else:
        return False

    if not picking_weapon and my_player['ammo']['Shells']>10:
        return True
    else:
        get_shells(my_player)
        return False
        

def square_up(my_player):
    objects = requests.get(HOST+"world/objects").json()
    possible_pickups = []
    for obj in objects:
        if obj['type'] == GunType.SHOTGUN:
            possible_pickups.append(obj)

    closest_obj = sorted(possible_pickups,key=lambda x: x['distance'])[0]
    return go_grab_object(my_player,closest_obj)

def get_shells(my_player):
    objects = requests.get(HOST+"world/objects").json()
    possible_pickups = []
    for obj in objects:
        if obj['type']==AmmoType.SHOTGUN:
            possible_pickups.append(obj)
    
    closest_obj = sorted(possible_pickups,key=lambda x: x['distance'])[0]
    return go_grab_object(my_player,closest_obj,picking_weapon=False)

def reload_ammo(my_player):
    if my_player['ammo']['Shells']< 5:
        get_shells(my_player)


def pick_up_health(my_player):
    objects = requests.get(HOST+"world/objects").json()
    possible_pickups = []
    for obj in objects:
        if obj['type']==Health.POTION:
            possible_pickups.append(obj)
    
    closest_obj = sorted(possible_pickups,key=lambda x: x['distance'])[0]
    return go_grab_object(my_player,closest_obj,picking_weapon=False)


def health_is_up_there(my_player):
    if my_player['health']<50:
        while(not (my_player['health']>50)):
            pick_up_health(my_player)