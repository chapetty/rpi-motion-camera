from picam3 import motion
import picamera

motion_state = False

while True:
    motion_state = motion()
    print(motion_state)
    if motion_state:
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.capture("motion_pic.jpg")
        print("Picture taken")
