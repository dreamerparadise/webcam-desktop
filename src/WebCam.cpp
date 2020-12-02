#include "WebCam.hpp"

WebCam::WebCam() : CamIndex(0)
{ 
    vcapture.open(CamIndex); // Most Likely Default Index for all webcams
}

WebCam::WebCam(int _camIndex) : CamIndex(_camIndex)
{
    vcapture.open(CamIndex);
}

void WebCam::SetCamIndex(int *index)
{
    vcapture.open(*index);
}

void WebCam::SetCustomeWindowName(const char *__window_name__)
{
    WindowName = __window_name__;
}

bool WebCam::IsOpen()
{
    return vcapture.isOpened();
}

void WebCam::Release()
{
    vcapture.release();
}

void WebCam::Display(void)
{
    imageshow();
}

void WebCam::Display(ImageMatrix &frame)
{
    imageshow(frame);
}

bool WebCam::FrameRead()
{
    return vcapture.read(image_mat);
}

bool WebCam::FrameRead(ImageMatrix *frame)
{
    return vcapture.read(*frame);
}

int WebCam::waitKey(int delay, int ButtonIndex)
{
    return cv::waitKey(delay);
}