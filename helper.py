import requests
import math

HOST = "http://localhost:6001/api/"

class Moves:
    SHOOT = "shoot"
    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "turn-left"
    RIGHT = "turn-right"
    USE = "use"
    SLEFT = "strafe-left"
    SRIGHT = "strafe-right"
    SWITCH = "switch-weapon"


class Amount:
    WEEBIT = 2
    SLOW = 5
    MEDIUM = 10
    FAST = 20    
    NUTS = 30
    WILD = 40
    SAVAGE = 50    



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
    return requests.get(HOST+"player")

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

def turn_to_point(my_player,other_player):    
    MY_POS , POS  = my_player['position'], other_player['position']
    rad_angle = math.atan2(MY_POS['y']-POS['y'],MY_POS['x']-POS['x'])
    deg_angle = rad2deg(rad_angle)
    norm_angle = deg_angle if deg_angle > 0 else deg_angle + 360
    remain = my_player['angle'] - norm_angle
    remain = remain if remain >=0 else remain + 360

    distance = get_distance(my_player['position'],other_player['position'])    
    print(distance)

    if remain < 185 and remain > 175 and distance < 200:
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