from helpers import item_caps, x, y, ws, move_to, soil, water, harvest_now

# Hay Here
def hay_harvest():
    clear()
    for i in range(ws):
        harvest_now()
        plant(Entities.Grass)
        move(North)
    move(East)

# Wood Here		
def wood_harvest():
    clear()
    for i in range(ws):
        harvest_now()
    if (get_pos_x() % 2 == 0 and get_pos_y() == 1) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 0):
        harvest_now()
        water()
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)
        move(North)
    move(East)

# Carrot Here	
def carrot_harvest():
    clear()
    for i in range(ws):
        harvest_now()
        soil()
        water()
        plant(Entities.Carrot)
        move(North)
    move(East)

# Pumpkin Here	
def pumpkin_harvest():    
    clear()
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
        if num_items(Items.Pumpkin) > item_caps[Items.Pumpkin] or num_items(Items.Carrot) < 50000:
            break

        
# Dino Here but only works on even number grid sizes. Uncomment and update set world size as needed.
def dino():
    clear()
    #set_world_size(8)
    change_hat(Hats.Dinosaur_Hat)
    dir = North
    map = get_world_size() - 1

    def hat():
        change_hat(Hats.Dinosaur_Hat)
        change_hat(Hats.Dinosaur_Hat)

    while True:
        for i in range(map):
            if not move(dir):
                hat()
        
            if get_pos_y() == map:
                dir = South
                if not move(East):
                    hat()
                
            if get_pos_y() == 1 and get_pos_x() == map:
                dir = West
                if not move(South):
                    hat()
                        
            if get_pos_y() == 1 and dir == South:
                dir = North
                if not move(East):
                    hat()
                
            if get_pos_x() == 0 and dir == West:
                dir = North
        if num_items(Items.Bone) > item_caps[Items.Bone]:
            break

# Cactus Here
def cactus():
    clear()

    for y in range(ws):
        for x in range(ws):
            move_to(x, y)
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Cactus)

    cactus_sizes = []
    for y in range(ws):
        row = []
        for x in range(ws):
            row.append(0)
        cactus_sizes.append(row)

    for y in range(ws):
        for x in range(ws):
            move_to(x, y)
            cactus_sizes[y][x] = measure()

    changed = True
    while changed:
        changed = False
        for y in range(ws):
            for x in range(ws):
                move_to(x, y)
                if x < ws - 1 and cactus_sizes[y][x] > cactus_sizes[y][x + 1]:
                    swap(East)
                    cactus_sizes[y][x], cactus_sizes[y][x + 1] = cactus_sizes[y][x + 1], cactus_sizes[y][x]
                    changed = True
                if y < ws - 1 and cactus_sizes[y][x] > cactus_sizes[y + 1][x]:
                    swap(North)
                    cactus_sizes[y][x], cactus_sizes[y + 1][x] = cactus_sizes[y + 1][x], cactus_sizes[y][x]
                    changed = True
    move_to(0, 0)
    harvest()
    if num_items(Items.Cactus) > item_caps[Items.Cactus]:
        return True

# Sunflower Here
def sunflower():
    clear()    
    cur = {0:0, 1:0}
    def move_to(x, y):
        global cur
        dx, dy = x - cur[0], y - cur[1]
        cur = {0:x,1:y}
        while dx > 0:
            dx = dx - 1
            move(East)
        while dx < 0:
            dx = dx + 1
            move(West)
        while dy > 0:
            dy = dy - 1
            move(North)
        while dy < 0:
            dy = dy + 1
            move(South)

    clear()
    wSize = get_world_size()
    order = {}
    while True:
        x, y = get_pos_x(), get_pos_y()
        if x == 0 and y == 0:
            for i in range(15, 6, -1):
                if i in order:
                    for pos in order[i]:
                        move_to(pos[0], pos[1])
                        while not can_harvest():
                            use_item(Items.Fertilizer)
                        harvest()
            order = {}
            move_to(0,0)
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Sunflower)
        if get_water() < 0.3:
            use_item(Items.Water)
        if measure() not in order:
            order[measure()] = [{0:x,1:y}]
        else:
            order[measure()].append({0:x,1:y})
        if y == wSize - 1:
            move(East)
        move(North)
        if num_items(Items.Power) > item_caps[Items.Power]:
            return False

# Poly Here
def poly():
    clear()    
    chain = []
    clear()
    soil()
    water()
    plant(Entities.Carrot)
    chain.append((get_entity_type(), get_pos_x(), get_pos_y()))
    
    for _ in range(ws * ws):
        companion = get_companion()
        if companion == None:
            break
        comp_type, (cx, cy) = companion  

        move_to(cx, cy)
        if can_harvest():
            if get_entity_type() in chain:
                chain.remove((get_entity_type(), get_pos_x(), get_pos_y()))
            harvest()
        soil()
        water()
        plant(comp_type)
        chain.append((comp_type, cx, cy))
    for comp_type, x, y in chain:
        move_to(x, y)
        if can_harvest():
            harvest()

# Maze Starter Here
def maze_starter():    
    while True:
        if create_maze():
            if treasure_hunt():
                continue
    


# Create Maze Here
def create_maze():    
    set_world_size(8)
    substance = get_world_size() * get_world_size()
    plant(Entities.Bush)
    while True:
        if substance > get_world_size():
            if num_items(Items.Weird_Substance) >= substance:
                use_item(Items.Weird_Substance, substance)
                return True
        elif substance < get_world_size():
            if num_items(Items.Weird_Substance) == 0:
                if can_harvest():
                    harvest()
            plant(Entities.Bush)
        if num_items(Items.Fertilizer) == 0:
            use_item(Items.Fertilizer)
        return True

# Treasure Hunt Here
def treasure_hunt():
    dir = West
    x = get_pos_x()
    y = get_pos_y()
    while num_items(Items.Gold) < item_caps[Items.Gold]:
        move(dir)
        
        x2 = get_pos_x()
        y2 = get_pos_y()
        
        if x==x2 and y==y2:
            if dir==West:
                dir = North
            elif dir==North:
                dir = East
            elif dir==East:
                dir = South
            elif dir==South:
                dir = West
        else:
            x = get_pos_x()
            y = get_pos_y()
            
            if dir==West:
                dir = South
            elif dir==North:
                dir = West
            elif dir==East:
                dir = North
            elif dir==South:
                dir = East
        
        if get_entity_type()==Entities.Treasure:
            harvest()
            return True
        
def weird_farm():
    for i in range(ws):
        harvest_now()
        soil()
        water()
        plant(Entities.Carrot)
        if num_items(Items.Fertilizer) > item_caps[Items.Fertilizer]:
            use_item(Items.Fertilizer)
        move(North)
    move(East)
