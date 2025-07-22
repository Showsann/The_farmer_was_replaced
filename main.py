from helpers import item_caps
import farm

while True:	
	if num_items(Items.Carrot) < item_caps["carrot_cap"]:
		farm.poly()
	elif num_items(Items.Pumpkin) < item_caps["pumpkin_cap"]:
		farm.pumpkin_harvest()
	elif num_items(Items.Bone) < item_caps["bone_cap"]:
		farm.dino()
	elif num_items(Items.Cactus) < item_caps["cactus_cap"]:
		farm.cactus()
	elif num_items(Items.Power) < item_caps["power_cap"] and num_items(Items.Fertilizer) > item_caps["fert_min"]:	
		farm.sunflower()
	elif num_items(Items.Gold) < item_caps["gold_cap"]:
		farm.maze_starter()
	else:
		clear()		
		do_a_flip()
		print("Done Massa!")