#pragma once
#include <opencv2/opencv.hpp>

enum class ColorType : int{
    COLOR_BGR2GRAY = cv::COLOR_BGR2GRAY,
};

enum Key : long{
    Q = 1048689,
};

// uint8_t
class WebCam;

typedef cv::Mat ImageMatrix; 
typedef cv::VideoCapture VideoCapture;
typedef cv::HOGDescriptor HOGDescriptor;
typedef cv::Rect Rect;
typedef WebCam WebCam;
typedef ColorType ColorType;
typedef Key Key;

// Key Index
