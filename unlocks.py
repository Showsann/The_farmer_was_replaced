def can_afford(cost):
    for item in cost:
        if num_items(item) < cost[item]:
            return False
    return True

def auto_unlock_once(verbose=False):
    unlocked_any = False
    for u in Unlocks:
        if get_cost(u) == None:
            continue
        if num_unlocked(u) == 0 or is_repeatable(u):
            cost = get_cost(u)
            if cost and can_afford(cost):
                success = unlock(u)
                if success:
                    unlocked_any = True
                    if verbose:
                        quick_print("Unlocked:", u)
    return unlocked_any

def is_repeatable(unlock):
    repeatables = [
        Unlocks.Speed,
        Unlocks.Expand,
        Unlocks.Carrots,
        Unlocks.Grass,
        Unlocks.Trees,
        Unlocks.Cactus,
        Unlocks.Dinosaurs,
        Unlocks.Mazes
    ]
    return unlock in repeatables

def auto_unlock_loop(verbose=False):
    while True:
        unlocked = auto_unlock_once()
        if not unlocked:
            break
