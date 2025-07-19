### This is for early game to quickly get what you need. Depending on your gamestate, comment out code you can't use.

hay_cap = 30000
wood_cap = 30000
carrot_cap = 30000
pumpkin_cap = 30000
x = get_pos_x()
y = get_pos_y()
ws = get_world_size()

def hay_harvest():
	if get_ground_type() != Grounds.Grassland:
		clear()
	for i in range(ws):
		if can_harvest():
			harvest()
			move(North)
	move(East)
		
def wood_harvest():
	for i in range(ws):
		if can_harvest():
			harvest()
		if (get_pos_x() % 2 == 0 and get_pos_y() == 1) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 0):
			if can_harvest():
				harvest()
			if get_water() <= 0.3:
				use_item(Items.Water)
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		move(North)
	move(East)
	
def carrot_harvest():
	for i in range(ws):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		if get_water() <= 0.2:
			use_item(Items.Water)
		plant(Entities.Carrot)
		move(North)
	move(East)
	
def pumpkin_harvest():    
    ready = []
    for _ in range(ws):
        col = []
        for _ in range(ws):
            col.append(False)
        ready.append(col)

    cur_x = get_pos_x()
    if cur_x != 0:
        left  = cur_x
        right = ws - cur_x
        if left <= right:
            for _ in range(left):
                move(West)
        else:
            for _ in range(right):
                move(East)

    cur_y = get_pos_y()
    if cur_y != 0:
        down = cur_y
        up   = ws - cur_y
        if down <= up:
            for _ in range(down):
                move(South)
        else:
            for _ in range(up):
                move(North)

    going_east = True

    while True:
        all_ready = True

        for row in range(ws):
            for step in range(ws):
                x = get_pos_x()
                y = get_pos_y()

                tile_ready = ready[x][y]

                if tile_ready:
                    if get_entity_type() != Entities.Pumpkin or can_harvest() != True:
                        tile_ready      = False
                        ready[x][y]     = False

                if tile_ready != True:
                    if get_ground_type() == Grounds.Grassland:
                        till()

                    if get_entity_type() != Entities.Pumpkin:
                        plant(Entities.Pumpkin)
                    if get_water() < 0.2:
                        use_item(Items.Water)

                    if can_harvest():
                        tile_ready      = True
                        ready[x][y]     = True

                if tile_ready != True:
                    all_ready = False

                if step < ws - 1:
                    if going_east:
                        move(East)
                    else:
                        move(West)

            if row < ws - 1:
                move(North)
            going_east = not going_east

        if all_ready:
            harvest()
            for ix in range(ws):
                for iy in range(ws):
                    ready[ix][iy] = False

        move(North)
        if get_pos_x() != 0:
            move(East)
        if num_items(Items.Pumpkin) > 5000000:
            break


while True:
	if num_items(Items.Hay) < hay_cap:
		hay_harvest()
	elif num_items(Items.Wood) < wood_cap:
		wood_harvest()
	elif num_items(Items.Carrot) < carrot_cap:
		carrot_harvest()
	elif num_items(Items.Pumpkin) < pumpkin_cap:
		pumpkin_harvest()
	else:
		do_a_flip()
	
