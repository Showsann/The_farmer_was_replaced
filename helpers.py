item_caps = {
    "hay_cap": 1000000,
    "wood_cap": 1000000,
    "carrot_cap": 1000000,
    "pumpkin_cap": 1000000,    
    "bone_cap": 1000000,
    "cactus_cap": 1000000,
    "power_cap": 50000,
    "gold_cap": 100000,
    "fert_min" : 10000
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