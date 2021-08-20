# Um-The-Presentation-Tracker
Utilizing Apple’s native speech recognition software, “Um, the presentation tracker” listens to a presenter’s speech in real time and auto-detects any flawed speech habits.

### How it works
"Um" The presentation tracker, is a 2-part program. 
1. The first part, is for the user to manually activate text to speech on a .txt file. Speaker should do this prior to the presentation. While the speaker presents, Apple's native Text-to-Speach will write down all the words stated by the speaker. As soon, as the speaker finishes their presentation, they will have to manually stop the Text-to-Speech. 
2. The second part, is for the user to run the python script. The python script will read what Apple's Text-to-Speech wrote down on the .txt file, and count how many "um" and "like" words were stated. 
