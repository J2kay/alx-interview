#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""

def can_unlock_all(boxes):
	"""lockboxes checker code"""
    opened_boxes = {0}
    unused_keys = set()

    for box_number, box in enumerate(boxes):
        if box_number in opened_boxes:
            continue

        if any(key in opened_boxes for key in box):
            unused_keys.update(box)

        opened_boxes.add(box_number)

    return len(opened_boxes) == len(boxes)
