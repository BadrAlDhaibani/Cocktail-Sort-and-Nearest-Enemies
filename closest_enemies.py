def dist(a,b):
    return ((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5

def closest_enemies(hero_position,enemy_positions):
    while True:
        swapped = False
        for i in range(0,len(enemy_positions)-1,1):
            if dist(hero_position,enemy_positions[i]) > dist(hero_position,enemy_positions[i+1]):
                enemy_positions[i], enemy_positions[i+1] = enemy_positions[i+1], enemy_positions[i]
                swapped = True
        if swapped == False:
            break

    return print(enemy_positions)

PLAYER =  (10,10)
ENEMIES = [(20,1),(4,15),(11,10),(5,2)]

closest_enemies(PLAYER, ENEMIES)

