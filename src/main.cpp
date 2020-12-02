/*
 * Programe to create a Cam application
 * Using C++ and opencv
 */

#include "WebCam.hpp"

static WebCam* webcam;
static ImageMatrix* image_mat;

bool OpenWebCam();
bool RunWebCam();
void DestroyAllEvent();

int main (int arg, const char* args[]){
    
    if ( !OpenWebCam( ) ) return 1;

    while(1){
        if ( !RunWebCam() )
            break;
    }
    
    DestroyAllEvent();

    return 0;
}

bool OpenWebCam(){

    webcam = new WebCam(0); // 0 is the index of the webcam 
    image_mat = new ImageMatrix();

    if ( !webcam->IsOpen( ) )
    {
        printf("No Device Detected\n");
        webcam->Release();
        free(webcam); // free the webcam
        return false;
    }

    webcam->SetCustomeWindowName("Webcam C++ Press Q to quite");
    return true;
}

bool RunWebCam(){

    if (!webcam->FrameRead(image_mat)) {
        printf("Video Stream is ended\n");
        return false;
    }

    printf("Wecam Running :) \n");

    cv::flip(*image_mat, *image_mat, 1);
    webcam->Display(*image_mat);

    if (webcam->waitKey(1) == (int)Key::Q) // don't know in manjaro index for Q is 1048689
        return false;

    return true;
}

void DestroyAllEvent(){
    webcam->Release();
    free(webcam);
}