from helper import *
import pprint
pp = pprint.PrettyPrinter(indent=4)

my_player,other_players = get_all_player()


closest_enemy = get_closest_enemy(my_player,other_players)    

dead = False
have_shotgun = False
while(not dead):
    if not have_shotgun:
        have_shotgun = square_up(my_player)
    move_to_enemy(my_player,closest_enemy)
    # shoot()
    if is_enemy_dead(closest_enemy):
        other_players.remove(closest_enemy)
        closest_enemy = get_closest_enemy(my_player,other_players)    
        
    