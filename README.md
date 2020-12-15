Hello everyone, I have used here a very simple tool that is, Google Text to Speech API known as the **gTTS API**. It converts text entered by the user, into audio which can be saved as a mp3 file.

### **Installation**

Open the terminal and install 

`pip install gTTS`

`pip install playsound`

###  **Here is the sample code** 

```
# Import the required module
from gtts import gTTS
from playsound import playsound


# function
def function(language):
    mytext = input("Type in your preferred language :\t")
    object = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    object.save("audio.mp3")

    # Playing the converted file
    playsound('audio.mp3')


if __name__ == '__main__':
    #  languages
    print(" en: English\n hi:Hindi\n ml: Malayalam\n ta:Tamil\n ")
    language = input("Enter the language code you want to convert to speech\n")
    function(language)  # calling function

```
Create a python file and name it as you wish with *.py* extension.
Run the above sample code.
*Input:*
Enter the code in the language you want to convert into speech.
For example : *en* for English. Then enter the text you wish to convert into speech.
The output will be an audio of your entered text.

## **Explanation about code **

```
from gtts import gTTS
from playsound import playsound
```
Import the necessary packages.

```
object = gTTS(text=mytext, lang=language, slow=False)

```
Parameters :
- text  = It's of string type. The text to be read.
- lang = The language to read the text. It defualt value is *en*. List of language can be accessed by  ` gtts-cli --all ` 

- slow = Reads text more slowly. Defaults is *False*.

```
object.save("audio.mp3")
```
Saves to mp3 format.


```
playsound('audio.mp3')
```
It plays the saved mp3 file.

**Note : ** For more details refer [gTTS]( http://gtts.readthedocs.org/) documentation and [playsound](https://pypi.org/project/playsound/).
