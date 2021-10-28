cmake_minimum_required(VERSION 3.9)
project(DetectorCPP)

set(CMAKE_CXX_STANDARD 11)
find_package(OpenCV REQUIRED)
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable(DetectorCPP src/detectorcpp/main.cpp src/detectorcpp/detector.cpp)
target_link_libraries(DetectorCPP ${OpenCV_LIBS})
