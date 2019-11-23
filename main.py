from picam3 import motion

motion_state = False

while True:
    motion_state = motion()
    print(motion_state)
