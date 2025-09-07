# Simulation parameters.
filename    = "sim1"                               # file to simulate
sim_unlocks = None                                 # start with no unlocks
sim_items   = {Items.Carrot: 10000, Items.Hay: 50} # Start with Carrots and Hay
sim_globals = {}                                   # no extra globals
seed        = 0                                    # random seed
speedup     = 1                                    # normal speed

# Import necessary modules
from helpers import move_to, x, y, item_caps, harvest_now, water, soil
import farm
import main

# Run initial simulation and report time
run_time = simulate(
    filename,
    sim_unlocks,
    sim_items,
    sim_globals,
    seed,
    speedup
)
print("Initial simulation took", run_time, "seconds")

# Pretty sure this is still broken
