# Import the required module
import pyttsx3

# Create a string
string = "You are welcome here. "

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'speech1.mp3')

# Wait until above command is not finished.
engine.runAndWait()
