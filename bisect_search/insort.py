import bisect
import random

SIZE = 9
random.seed(669)

container = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    # insort keeps a sorted sequence always sorted
    bisect.insort(container, new_item)
    print(f"{new_item:02} --> {container}")
