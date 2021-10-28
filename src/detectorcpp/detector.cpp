#include <opencv2/core/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>

#include "detector.hpp"


Detector::Detector(std::string classifier_path, int t, int s, int m) {
    threshold = t;
    scale_factor = s;
    min_neighbors = m;
    classifier.load(classifier_path);
}


bool Detector::check_frame(cv::Mat frame, int &n, cv::Rect &closest) {

    // convert frame from bgr to grayscale colorspace
    cv::Mat gray_frame;
    cv::cvtColor(frame, gray_frame, cv::COLOR_BGR2GRAY);

    // locate objects in frame
    std::vector<cv::Rect> objects;
    classifier.detectMultiScale(gray_frame, objects);
    n = objects.size();

    // if no objects have been found, return no warning and leave closest unchanged
    if (!n) {
        return false;
    }

    // find "closest" rectangle
    cv::Rect closest_obj;
    for (int i=0; i<n; i++) {
        if (objects[i].y + objects[i].height > closest_obj.y + closest_obj.height) {
            closest_obj = objects[i];
        }
    }
    closest = closest_obj;

    // check if a proximity warning should be given
    bool warning = closest_obj.y + closest_obj.height > frame.size().height - threshold;

    return warning;

}
