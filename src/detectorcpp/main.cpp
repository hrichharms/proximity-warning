#include <iostream>
#include <ctime>

#include "detector.hpp"


void debug(std::string const x) {
    std::time_t now = time(0);
    std::tm *ltm = localtime(&now);
    std::cout << "[" << 5 + ltm->tm_hour << ":" << 30 + ltm->tm_min << ":" << ltm->tm_sec << "] " << x << std::endl;
}


int main(int argc, char *argv[]) {

    return 0;

}
