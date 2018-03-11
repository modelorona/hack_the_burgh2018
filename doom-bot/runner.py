from helper import *
import pprint
pp = pprint.PrettyPrinter(indent=4)

my_player,other_players = get_all_player()


closest_enemy = get_closest_enemy(my_player,other_players)    

dead = False
have_shotgun = False

#Initial moves to prepare it
move(Moves.RIGHT,Amount.MEDIUM)
move(Moves.FORWARD,Amount.SAVAGE)

while(not dead):
    if not have_shotgun:
        have_shotgun = square_up(my_player)
    print("1")
    move_to_enemy(my_player,closest_enemy)
    print("2")    
    if is_enemy_dead(closest_enemy):
        other_players.remove(closest_enemy)
    print("3")
        
    closest_enemy = get_closest_enemy(my_player,other_players)
    reload_ammo(my_player)
    health_is_up_there(my_player)