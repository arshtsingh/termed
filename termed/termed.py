from tqdm import tqdm
import time
from time import sleep
import sys

'''
pace (slow, med, fast)

slow => inhale 5 hold 5 exhale 5 hold 5
med => inhale 4 hold 4 exhale 4 hold 4
fast = inhale 3 hold 3 exhale 3 hold 3

1 set = 4 breaths = 1:04 min
2 set = 8 breaths = 2.08 min
'''
cycle = ["inhale", "hold", "exhale", "hold"]
durration = lambda x: 64*x
count = 0
cycle_set = 1
while count != durration(1):
    if count % 16 == 0:
        print(f"set {cycle_set}")
        cycle_set += 1
    for item in cycle:
        for i in tqdm(range(0,4), desc = item):
            sleep(1)
            count += 1
