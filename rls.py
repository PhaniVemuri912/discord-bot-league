import random

lanes = ['Top','ADC','Support','Jungle','Mid']

def rls():
    i = 5
    selected_lanes = []
    while i > 0:
        if len(lanes) > 1:
            randselection = random.randint(0,i-1)
        else:
            randselection = 0
        selected_lanes.append(lanes[randselection])
        lanes.remove(lanes[randselection])
        i = i-1
    return selected_lanes

print(rls())