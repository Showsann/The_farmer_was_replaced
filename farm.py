from helpers import move_to, ws

# Poly Here
def poly():
    while num_items(Items.Carrot) < 1000000:
        clear()
        if get_ground_type() != Grounds.Soil:
            till()
        if get_water() < 0.5:
            use_item(Items.Water)
        plant(Entities.Carrot)

        companion = get_companion()
        while companion != None:
            _, (x, y) = companion
            move_to(x, y)
            if can_harvest():
                harvest()
            if get_ground_type() != Grounds.Soil:
                till()
            if get_water() < 0.5:
                use_item(Items.Water)
            plant(companion[0])
            if num_items(Items.Fertilizer) > 100000:
                use_item(Items.Fertilizer)
            companion = get_companion()


# Pumpkin Here
def pumpkin():    
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

# Cactus Here
def cactus():
    while True:
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
        if num_items(Items.Cactus) > 3000000:
            break
         

# Dino Here
def dino():
    clear()
    def moveCheck(dir):
        if move(dir) == False:
            change_hat(Hats.Straw_Hat)
            change_hat(Hats.Dinosaur_Hat)
    
    while True:
        clear()
        change_hat(Hats.Dinosaur_Hat)
        
        while True:
            x = get_pos_x()
            y = get_pos_y()
            onEdge = False
            if x % 2 == 1:
                moveCheck(South)
                if y == 2:
                    onEdge = True
            else:
                moveCheck(North)
                if y == ws - 2:
                    onEdge = True
            if onEdge:
                if x == ws - 1:
                    move(South)
                    while move(West):
                        continue
                else:
                    moveCheck(East)
            if num_items(Items.Bone) > 3000000:
                break
        if num_items(Items.Bone) > 3000000:
            break

# Sunflower Here
def sunflower():
    cur = {0:0, 1:0}
    def moveTo(x, y):
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
                        moveTo(pos[0], pos[1])
                        while not can_harvest():
                            use_item(Items.Fertilizer)
                        harvest()
            order = {}
            moveTo(0,0)
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
        if num_items(Items.Power) > 2000000:
            break

# Maze Starter Here
def maze_starter():
    while True:
        if create_maze():
            if treasure_hunt():
                continue
        if num_items(Items.Gold) > 2000000:
            break


def create_maze():    
    set_world_size(8)
    substance = get_world_size() * num_unlocked(Unlocks.Mazes)
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

def treasure_hunt():
    dir = West
    x = get_pos_x()
    y = get_pos_y()
    while num_items(Items.Gold) < 5000000:
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