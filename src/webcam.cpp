/*
 * Programe to create a Cam application
 * Using C++ and opencv
 */

#include "webcam.hpp"


int main (int arg, const char* args[]){
    
    WebCam::WebCam* webcam = new WebCam::WebCam(1);

    if ( !webcam->IsVideoCaptureOpened( ) ){
        printf("Cannot Connect Device\n");
        std::cin.get();
        exit(1);
    }


    printf("Cam Working Fine\n");
    for(;;)
    {
        if (!webcam->FrameRead()) {
            printf("Video Stream is ended\n");
            exit(0);
        }

        webcam->Display();
        int index = WebCam::waitKey(1);
        if (index >= 0)
        {
            std::cout << "Esc key is pressed by user. Stoppig the video : " << index << std::endl;
            break;
        }
    }
    
    free(webcam); // free the webcam
    return 0;
}

