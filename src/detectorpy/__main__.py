from sys import argv
from datetime import datetime

from detector import Detector


CAMERA_RESOLUTION = (640, 640)
FPS_LIMIT = 32
CLASSIFIER_FILENAME = "classifiers/c1.xml"


def debug(x: str):
    print(str(datetime.now()).split()[1].split(".")[0], x)


if __name__ == "__main__":

    if len(argv) < 2:
        print("ERROR: Invalid arguments!")
        exit()

    if argv[1] == "-f": # takes filename and gui flag arguments
        # argv[2] -> video filename
        # argv[3] -> gui flag (1 = gui, 0 = no gui)

        debug("Importing video capture class from opencv...")
        from cv2 import VideoCapture

        # check if gui i sactivated
        gui = bool(int(argv[3]))

        if gui:
            debug("Importing opencv gui functions...")
            from cv2 import rectangle, imshow, waitKey

        debug("Loading video capture object...")
        vid = VideoCapture(argv[2])

        # check if video was opened successfully
        if not vid.isOpened():
            print("ERROR: Unable to open video file!")
            exit()

        debug("Loading detector object...")
        detector = Detector(CLASSIFIER_FILENAME)

        debug("Starting decision loop...")
        s = datetime.now()
        frames = 0
        while vid.isOpened():
            
            try:
                frames += 1
                
                # load next frame from loaded video file
                _, frame = vid.read()

                # check frame with detector object
                closest, warning = detector.check_frame(frame)

                # if gui activated, display frame and check for exit command
                if gui:

                    if len(closest):
                        pt1 = closest[0], closest[1]
                        pt2 = closest[0] + closest[2], closest[1] + closest[3]
                        color = (0, 0, 255) if warning else (255, 0, 0)
                        gui_frame = rectangle(frame, pt1, pt2, color, 3)
                        imshow("Frame", gui_frame)
                    else:
                        imshow("Frame", frame)

                    # check if exit key pressed
                    if waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    if warning:
                        debug("PROXIMITY WARNING!")

            except KeyboardInterrupt:
                break

        print(f"\nAVG. FPS: {frames // (datetime.now() - s).seconds}")

    elif argv[1] == "-c": # takes no further arguments

        debug("Importing Raspberry Pi camera modules...")
        from picamera.array import PiRGBArray
        from picamera import PiCamera

        debug("Initializing camera object and capture settings...")
        camera = PiCamera()
        camera.resolution = CAMERA_RESOLUTION
        camera.framerate = FPS_LIMIT

        debug("Initializing capture buffer...")
        raw_capture = PiRGBArray(camera, size=CAMERA_RESOLUTION)

        debug("Loading detector object...")
        detector = Detector(CLASSIFIER_FILENAME)

        debug("Starting decision loop...")
        for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):

            # check frame with detector object
            _, warning = detector.check_frame(frame)

            if warning:
                debug("PROXIMITY WARNING!")
