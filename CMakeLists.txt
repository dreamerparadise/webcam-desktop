cmake_minimum_required(VERSION 3.13)
project(webcam)

set(CMAKE_CXX_STANDARD 11)

include_directories(${OpenCV_INCLUDE_DIRS})

find_package(OpenCV REQUIRED)
add_executable(webcam src/webcam.cpp)
target_link_libraries(webcam ${OpenCV_LIBS})