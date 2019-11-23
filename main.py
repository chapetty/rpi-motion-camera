import os
from datetime import datetime
from subprocess import call

import picamera
from picam3 import motion

motion_state = False
pic_path = "/home/pi/rpi-motion-camera/images"


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
    return pic_name


def stamp_picture(current_time, pic_path, pic_name):
    # Get full path
    full_path = f"{pic_path}/{pic_name}"
    # Create message to stamp on picture
    message = current_time.strftime("%Y.%m.%d - %h:%M:%S")
    # Create the command
    command = f"/usr/bin/convert {full_path} -pointsize 36 -fill red -annotate +700+650 '{message}' {full_path}"
    # Execute the command
    call([command], shell=True)
    print("Picture has been timestamped")


while True:
    # Check if path directory exists, if not create it
    if not os.path.isdir(pic_path):
        os.mkdir(pic_path)
        print(f"Created directory {pic_path}")

    motion_state = motion()
    print(motion_state)
    if motion_state:
        current_time = get_time()
        pic_name = capture_image(current_time, pic_path)
        stamp_picture(current_time, pic_path, pic_name)
