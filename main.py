from helpers import (
	item_caps,
	target_items,
	try_unlock
)
import farm

while True:
	if try_unlock():
		continue

	did_refill = False
	for item, cap, handler in target_items:
		if num_items(item) < cap:
			handler()
			did_refill = True				
			break

	if not did_refill:
		clear()
		do_a_flip()
