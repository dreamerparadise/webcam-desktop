import cv2
import kivy
import face_recognition
import dlib
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		#Declearing the class as a super class
		super(MyGrid, self).__init__(**kwargs)
		#set colom of main gridlayout as 1
		self.cols = 1
		#Creating a new grid layout name as Information
		self.Information = GridLayout()
		#set the coloms of Informtaion to 1
		self.Information.cols = 1
		information = "First You Need To Download IPWebcam From Playstore."
		self.Information.add_widget(Label(text = information))
		#Add the Information Layout into the main Layout
		self.add_widget(self.Information)
		#Againg creat a new Layout name as getData
		self.getData = GridLayout()
		#set cols number of getData
		self.getData.cols = 2
		self.getData.add_widget(Label(text= "Enter Camera Ip"))
		#Addind Text Panel to have the text
		self.url = TextInput(multiline = False)
		self.getData.add_widget(self.url)
		self.add_widget(self.getData)
		#Adding Buttton TO get The Ip of camera
		self.submit = Button(text="submit")
		#Adding Option pressed so if the button pressed all the things happends what i want
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)
	

	def pressed(self, instance):
		print("Pressed")
		#Started FaceDetection Work
		#Prepear the Url To work Perfectly
		if self.url.text:
			URL = ("http://"+self.url.text+"/video")
			face_location = []
			video_capture = cv2.VideoCapture(URL)
			while True:
				ret, frame = video_capture.read()
				frame = cv2.resize(frame, None, fx=0.2, fy=0.2)
				rgb_frame = frame[:, :, ::-1]
				face_locations = face_recognition.face_locations(rgb_frame)

				for top, right, bottom, left in face_locations:
					cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)
				cv2.imshow('Video', frame)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			video_capture.release()
			cv2.destroyAllWindows()
		else:
			self.remove_widget(self.submit)
			self.submit = Button(text="Erro No data Entered\n Enter A data and click again")
			self.add_widget(self.submit)
			self.submit.bind(on_press=self.pressed)

class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	MyApp().run()


