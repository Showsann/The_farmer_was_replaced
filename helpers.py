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


ws = get_world_size()