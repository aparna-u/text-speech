# Import the required module for text
# to speech conversion
from gtts import gTTS
from playsound import playsound


# function
def function(language):
    mytext = input("Type in your preferred language :\t")

    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    # Playing the converted file
    playsound('welcome.mp3')


if __name__ == '__main__':
    # list of languages

    print("af: Afrikaans \nar: Arabic\nbn: Bengali\nbs: Bosnian\nca: Catalan\ncs: Czech\ncy: Welsh\nda: Danish\nde: "
          "German\nel: Greek\nen-au: English (Australia)\nen-ca: English (Canada)\nen-gb: English (UK)\nen-gh: "
          "English (Ghana)\nen-ie: English (Ireland)\nen-in: English (India)\nen-ng: English (Nigeria)\nen-nz: "
          "English (New Zealand)\n en-ph: English (Philippines)\nen-tz: English (Tanzania)\n en-uk: English (UK)\n "
          "en-us: English (US)\n en-za: English (South Africa)\nen: English\neo: Esperanto\nes-es: Spanish ("
          "Spain)\nes-us: Spanish (United States)\nes: Spanish\net: Estonian\nfi: Finnish\nfr-ca: French ("
          "Canada)\nfr-fr: French (France)\nfr: French\ngu: Gujarati\nhi: Hindi\nhr: Croatian\nhu: Hungarian\nhy: "
          "Armenian\nid: Indonesian\nis: Icelandic\nit: Italian\nja: Japanese\njw: Javanese\nkm: Khmer\nkn: "
          "Kannada\nko: Korean\nla: Latin\nlv: Latvian\nmk: Macedonian\nml: Malayalam\nmr: Marathi\nmy: Myanmar ("
          "Burmese)\nne: Nepali\nnl: Dutch\nno: Norwegian\npl: Polish\npt-br: Portuguese (Brazil)\npt-pt: Portuguese "
          "(Portugal)\npt: Portuguese\nro: Romanian\nru: Russian\nsi: Sinhala \nsk: Slovak\nsq: Albanian\nsr: "
          "Serbian\nsu: Sundanese\nsv: Swedish\nsw: Swahili\nta: Tamil\nte: Telugu\nth: Thai\ntl: Filipino\ntr: "
          "Turkish\nuk: Ukrainian\nur: Urdu\nvi: Vietnamese\nzh-cn: Chinese (Mandarin/China) \nzh-tw: Chinese ("
          "Mandarin/Taiwan)")

    language = input("Enter the language code you want to convert to speech \n")
    function(language)
