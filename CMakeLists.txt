cmake_minimum_required(VERSION 3.13)
project(webcam)

set(CMAKE_CXX_STANDARD 11)

include_directories(${OpenCV_INCLUDE_DIRS})

find_package(OpenCV REQUIRED)

file( GLOB APP_SOURCES src/*.cpp )

add_executable(webcam ${APP_SOURCES})

target_link_libraries(webcam ${OpenCV_LIBS})