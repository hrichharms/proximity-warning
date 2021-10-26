from numpy import ndarray, array
from cv2 import cvtColor, CascadeClassifier, COLOR_BGR2GRAY


DEFAULT_THRESHOLD = 100
DEFAULT_SCALE_FACTOR = 1.1
DEFAULT_MIN_NEIGHBORS = 4


class Detector:

    def __init__(self,
        classifier_path: str,
        threshold: int = DEFAULT_THRESHOLD,
        scale_factor: float = DEFAULT_SCALE_FACTOR,
        min_neighbors: int = DEFAULT_MIN_NEIGHBORS
    ):
        self.classifier = CascadeClassifier(classifier_path)
        self.threshold = threshold
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors

    def check_frame(self, frame: ndarray):
        """
        Takes a frame in the BGR color space in the form
        of a numpy array and uses self.classifier to
        determine if a proximity warning is required.
        """

        # convert bgr frame to grayscale
        gray_frame = cvtColor(frame, COLOR_BGR2GRAY)

        # locate objects in frame
        objects = self.classifier.detectMultiScale(gray_frame, self.scale_factor, self.min_neighbors)

        # if no objects are found, return an empty numpy array and no warning
        if not len(objects):
            return array([]), False

        # find the closest object
        closest = max(objects, key=lambda x: x[1] + x[3])

        # check if a proximity warning should be given
        warning = closest[1] + closest[3] > frame.shape[0] - self.threshold

        # return bounding box of closest object and warning decision
        return closest, warning
