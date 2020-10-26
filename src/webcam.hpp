/*
 * Programe to create a webcam application
 * Using C++ and opencv
 */

/*
** Documentation 
        To create a Webcam Simply create a object File
        ImageMatrix is the matrix where we store the image data
        VideoCapture to Capture anyvideo
 */

#include <opencv2/opencv.hpp>
#include <stdio.h>
#include <iostream>

class Cam
{   
public:
    typedef cv::Mat ImageMatrix; 
    typedef cv::VideoCapture VideoCapture;

private:
    const char* WindowName = "Sample Window";
    ImageMatrix image_mat;
    VideoCapture vcapture;

    std::string FileName = "";
    int Flags = 1;
    int CamIndex = 0;

    inline void imageshow(){
        cv::imshow(WindowName, image_mat);
    }
    inline void imageshow(ImageMatrix &frame){
        cv::imshow(WindowName, frame);
    }

public:

    Cam();
    Cam(int _camIndex = 0) : CamIndex(_camIndex){
        vcapture.open(CamIndex);
    }
    
    void SetCustomeWindowName(const char* __window_name__){
        WindowName = __window_name__;
    }

    bool IsVideoCaptureOpened(){
        return vcapture.isOpened();
    }

    void Display(void){
        imageshow();
    }

    void Display(ImageMatrix &frame){
        imageshow(frame);
    }

    bool FrameRead(cv::Mat &frame){
        return vcapture.read(frame);
    }

    bool FrameRead(){
        return vcapture.read(image_mat);
    }
};


namespace WebCam
{
    typedef Cam WebCam;

    inline int waitKey(int delay = 10, int ButtonIndex = 0){
        return cv::waitKey(delay);
    }


} // namespace WebCam


