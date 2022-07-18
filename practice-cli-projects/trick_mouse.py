import pyautogui as p

distance = 200

while True:
    p.moveRel(distance, 0, duration=15)    # move Right
    distance -= 5
    p.moveRel(0, distance, duration=15)    # move down
    p.moveRel(-distance, 0, duration=15)   # move left
    distance -= 5
    p.moveRel(0, -distance, duration=15)    # move up
    distance += 10