#include <iostream>
#include <ctime>

#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

#include "detector.hpp"


const std::string CLASSIFIER_PATH = "classifiers/c1.xml";


void debug(std::string const x) {
    std::time_t now = time(0);
    std::tm *ltm = localtime(&now);
    std::cout << "[" << ltm->tm_hour << ":" << ltm->tm_min << ":" << ltm->tm_sec << "] " << x << std::endl;
}


int main(int argc, char *argv[]) {

    if (argc < 2) {
        std::cout << "ERROR: Invalid arguments!\n";
        return 0;
    }

    std::string mode = argv[1];
    if (mode == "-f") {

        if (argc != 4) {
            std::cout << "ERROR: Invalid arguments!\n";
            return 0;
        }

        // parse command line arguments
        std::string vid_filename = argv[2];
        bool gui = true;

        debug("Loading video capture object...");
        cv::VideoCapture vid;
        vid.open(vid_filename);

        // check if video opened successfully
        if (!vid.isOpened()) {
            std::cout << "ERROR: Unable to open video file!\n";
            return 0;
        }

        debug("Initializing detector object...");
        Detector detector(CLASSIFIER_PATH, 100, 1.1, 4);

        debug("Starting decision loop...");
        cv::Mat frame;
        while (vid.read(frame)) {

            cv::namedWindow("Frame", cv::WINDOW_AUTOSIZE);
            cv::imshow("Frame", frame);

            if (cv::waitKey(100) == 27) {
                break;
            }

        }

        debug("Cleaning up...");
        vid.release();
        if (gui) {
            cv::destroyAllWindows();
        }

    } else if (mode == "-c") {

    } else {
        std::cout << "ERROR: Invalid arguments!\n";
    }

    return 0;

}
