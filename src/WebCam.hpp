/*
 * Programe to create a webcam application
 * Using C++ and opencv
 */

/*
** Documentation 
        To create a Webcam Simply create a object File
        ImageMatrix is the matrix where we store the image data
        VideoCapture to Capture anyvideo

    TO See the example check webcam.cpp
 */

#pragma once
#include "Defination.hpp"

class WebCam
{   
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

    WebCam(void);

    WebCam(int _camIndex = 0);

    void SetCamIndex(int*);
    
    void SetCustomeWindowName(const char*);

    bool IsOpen();

    void Release();

    void Display(void);

    void Display(ImageMatrix&);

    bool FrameRead();

    bool FrameRead(ImageMatrix*);

    int waitKey(int delay = 10, int ButtonIndex = 0);

};


