#recording and playing audio
import sounddevice as sd
#saving file
from scipy.io.wavfile import write
#loading file
import soundfile as sf

#rate at which audio is recorded
RECORDING_FREQUENCY = 44100

#records audio and saves to WAV file with specified name
def recordAudio(name, recordLength):
	#set name
	fileName = f"recordings/{name}.wav"
	#recording duration
	nSeconds = recordLength
	print(f"recording for {nSeconds} seconds...")
	#start recording
	myRecording = sd.rec(int(nSeconds * RECORDING_FREQUENCY), samplerate=RECORDING_FREQUENCY, channels=2)
	#wait till recording finished
	sd.wait()
	print("recording finished")
	#save as WAV file
	write(fileName, RECORDING_FREQUENCY, myRecording)
	print("recording saved")

#plays audio from recordings directory
def playAudio(name):
	#set name
	fileName = f"recordings/{name}.wav"

	# Extract data and sampling rate from file
	data, frequency = sf.read(fileName, dtype='float32')

	#play audio
	sd.play(data, frequency)
	print("playing audio...")
	#wait for audio to finish
	status = sd.wait()

while True:
	#menu
	print("All audio is saved and loaded from the recordings directory (./recordings)")
	print("1: Record Audio")
	print("2: Play Audio")
	print("3: Exit")
	
	#user selects from menu
	userSelection = input("Enter desired option(1, 2, 3)\n")
	
	#exits if selected by user
	if userSelection == "3":
		break
	
	#retrieves file name from user
	name = input("What is the name of the audio file (.wav files only)\n")
	
	#record audio with desired file name
	if userSelection == "1":
		#request recording length
		recordLength = int(input("How long is the recording going to be? (in seconds, no decimal, max 60)"))
		
		#verify recording length and record if valid
		if 0 < recordLength and recordLength <= 60:
			recordAudio(name, recordLength)
		else:
			print(f"{recordLength} is not a valid number of seconds to record")
		#return to menu
		continue

	#play audio with desired file name
	elif userSelection == "2":
		playAudio(name)
		#return to menu
		continue

	#if no option was selected notify user
	print("please select a valid option")