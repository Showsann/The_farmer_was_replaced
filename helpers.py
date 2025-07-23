item_caps = {
    Items.Hay : 1000000,
    Items.Wood : 1000000,
    Items.Carrot : 1000000,
    Items.Pumpkin : 1000000,    
    Items.Bone : 1000000,
    Items.Cactus : 1000000,
    Items.Power : 100000,
    Items.Gold : 1000000,
    Items.Fertilizer : 10000,
    Items.Weird_Substance : 100000
    }

x = get_pos_x()
y = get_pos_y()

ws = get_world_size()

def move_to(target_x, target_y):
    while get_pos_x() != target_x:
        if (target_x - get_pos_x()) % get_world_size() > get_world_size() / 2:
            move(West)
        else:
            move(East)
    while get_pos_y() != target_y:
        if (target_y - get_pos_y()) % get_world_size() > get_world_size() / 2:
            move(South)
        else:
            move(North)

def soil():
    if get_ground_type() != Grounds.Soil:
        till()

def water():
    if get_water() < 0.3:
        use_item(Items.Water)

def harvest_now():
    if can_harvest():
        harvest()

import farm
target_items = [
    (Items.Hay, item_caps[Items.Hay], farm.hay_harvest()),
    (Items.Wood, item_caps[Items.Wood], farm.poly()),
    (Items.Carrot, item_caps[Items.Carrot], farm.poly()),
    (Items.Pumpkin, item_caps[Items.Pumpkin], farm.pumpkin_harvest()),
    (Items.Bone, item_caps[Items.Bone], farm.dino()),
    (Items.Cactus, item_caps[Items.Cactus], farm.cactus()),
    (Items.Weird_Substance, item_caps[Items.Weird_Substance], farm.weird_farm()),
    (Items.Gold, item_caps[Items.Gold], farm.maze_starter())
]

unlockables = [
	Unlocks.Loops,
	Unlocks.Speed,
	Unlocks.Grass,
	Unlocks.Expand,
	Unlocks.Plant,
	Unlocks.Carrots,
	Unlocks.Debug,
	Unlocks.Operators,
	Unlocks.Watering,
	Unlocks.Trees,
	Unlocks.Debug_2,
	Unlocks.Timing,
	Unlocks.Senses,
	Unlocks.Variables,
	Unlocks.Fertilizer,
	Unlocks.Sunflowers,
	Unlocks.Pumpkins,
	Unlocks.Simulation,
	Unlocks.Lists,
	Unlocks.Functions,
	Unlocks.Cactus,
	Unlocks.Dinosaurs,
	Unlocks.Mazes,
	Unlocks.Leaderboard,
	Unlocks.Dictionaries,
	Unlocks.Import,
	Unlocks.Utilities,
	Unlocks.Costs,
	Unlocks.Polyculture,
	Unlocks.Auto_Unlock,
]


def try_unlock():
    for u in unlockables:
        cost = get_cost(u)
        if cost == {}:
            continue

        affordable = True
        for item, amt, in cost.items():
            if num_items(item) < amt:
                break

        if affordable:
            unlock(u)
            return True
    return False
