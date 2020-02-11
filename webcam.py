import cv2


def webcam(URL, video_capture):
    print("Pressed")
    # Started FaceDetection Work
    # Prepare the Url To work Perfectly
    # video_capture = cv2.VideoCapture(URL)
    # print(video_capture)
    while True:
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.resize(frame, None, fx=0.2, fy=0.2)

            # cv2.show is a cv2 function the show the frames one by one
            cv2.imshow('Press Q For Destroy', frame)

            # waiting for the q to be press then we will exit.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # video_capture.release() --> is to release the variable which is capturing the the data from webcam
    video_capture.release()
    cv2.destroyAllWindows()
