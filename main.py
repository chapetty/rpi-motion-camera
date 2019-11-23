import os
from datetime import datetime

import picamera
from picam3 import motion

motion_state = False
pic_path = "images/"


def get_time():
    # Fetch current time
    return datetime.now()


def capture_image(current_time, pic_path):
    # Generate filename
    pic_name = current_time.strftime("%Y.%m.%d-%H:%M:%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(f"{pic_path}/{pic_name}")
    print("Picture taken")


while True:
    # Check if path directory exists, if not create it
    if os.path.isdir(pic_path):
        os.mkdir(pic_path)
        print(f"Created directory {pic_path}")

    motion_state = motion()
    print(motion_state)
    if motion_state:
        capture_image(get_time(), pic_path)
