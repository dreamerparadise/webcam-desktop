import webcam
import cv2
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        # Declaring the class as a super class
        super(MyGrid, self).__init__(**kwargs)
        # set colum of main gridlayout as 1
        self.cols = 1

        # Creating a new grid layout name as Information
        self.Information = GridLayout()

        # set the coloms of Information to 1
        self.Information.cols = 1
        information = "First You Need To Download IPWebcam From Playstore."
        self.Information.add_widget(Label(text=information))

        # Add the Information Layout into the main Layout
        self.add_widget(self.Information)

        # Again create a new Layout name as getData
        self.getData = GridLayout()

        # set cols number of getData
        self.getData.cols = 2
        self.getData.add_widget(Label(text="Enter Camera Ip"))

        # Adding Text Panel to have the text
        self.url = TextInput(multiline=False)
        self.getData.add_widget(self.url)
        self.add_widget(self.getData)

        # Adding Button TO get The Ip of camera
        self.submit = Button(text="SUBMIT")

        # Adding Option pressed so if the button pressed all the things happens what i want
        self.submit.bind(on_press=self.pressed_for_ip_webcam)
        self.add_widget(self.submit)

    def pressed_for_ip_webcam(self, instances):
        if self.url.text:
            URL = ("http://" + self.url.text + "/video")
            video_capture = cv2.VideoCapture(URL)
            ret, frame = video_capture.read()
            if ret:
                print("all working fine")
                webcam.webcam(URL, video_capture)
            else:
                self.remove_widget(self.submit)
                self.submit = Button(text="Error enter Proper link\nand\nclick again")
                self.add_widget(self.submit)
                self.submit.bind(on_press=self.pressed_for_ip_webcam)
        else:
            self.remove_widget(self.submit)
            self.submit = Button(text="Error No data Entered\nEnter A data and click again")
            self.add_widget(self.submit)
            self.submit.bind(on_press=self.pressed)


class MyApp(App):
    # build is a pre defines method
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
