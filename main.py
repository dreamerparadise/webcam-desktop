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

				#Converting to RGB color scheme because cv2 uses BGR color scheme
				rgb_frame = frame[:, :, ::-1]

				#face_location is an array where we are collection face location axis in every frame.
				face_locations = face_recognition.face_locations(rgb_frame)

				#in this for loop we are using four axis data we collect in face_location array
				#loop will continue untill the data face array data finishes
				#the array data is = the total no of frames we collected.
				for top, right, bottom, left in face_locations:
					#cv2.rectangle is a funtion to draw rectangle in a perticular axis of a picture
					#basically we are just drawing rectangle with the color (0,0,255) in every frame
					cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)
				
				#cv2.show is a cv2 function the show the frames one by one
				cv2.imshow('Video', frame)

				#waiting for the q to be press then we will exit.
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
			
			#video_capture.release() --> is to release the variable which is capturing the the data from webcam
			video_capture.release()
			cv2.destroyAllWindows()
		else:
			self.remove_widget(self.submit)
			self.submit = Button(text="Erro No data Entered\n Enter A data and click again")
			self.add_widget(self.submit)
			self.submit.bind(on_press=self.pressed)

class MyApp(App):
	
	#build is a pre defines methon
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	MyApp().run()


