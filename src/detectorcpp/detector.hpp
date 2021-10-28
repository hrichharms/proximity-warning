#include <opencv2/imgcodecs.hpp>
#include <opencv2/objdetect.hpp>


class Detector {

    public:

        int threshold;
        float scale_factor;
        int min_neighbors;
        cv::CascadeClassifier classifier;

        Detector(std::string cpath, int t, float s, int m);

        bool check_frame(cv::Mat frame, int &n, cv::Rect &closest);

};
