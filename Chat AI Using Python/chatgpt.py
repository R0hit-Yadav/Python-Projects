from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import pathlib
import pyttsx3
import speech_recognition as sr
ScriptDir = pathlib.Path().absolute()

def speak(text):
    engine = pyttsx3.init()
    Id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Koro AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recogizing....")
        query = r.recognize_google(audio,language="en")
        print(f"==> User : {query}")
        return query.lower()

    except:
        return ""

url="https://chat.tune.app/"
chrome_option=Options()
user_agent="'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'"
chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument('--profile-directory=Default')
chrome_option.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_option)
driver.maximize_window()
driver.get(url=url)
driver.minimize_window()
Chatnumber=2
def iconap():
    while True:
        try:
            xPath='/html/body/div/div/div[3]/div/div[3]/div/div[1]/div[1]/div'
            driver.find_element(by=By.XPATH,value=xPath)
            break
        except:
            pass

def SendMessage(Query):
    spcount=0
    for char in Query:
        if char == ' ':
            spcount += 1
    if  spcount>=2:
        xPath='/html/body/div/div/div[3]/div/div[3]/div/div[3]/div/textarea'
        driver.find_element(by=By.XPATH,value=xPath).send_keys(Query)
        sleep(3)
        Xpath2='/html/body/div/div/div[3]/div/div[3]/div/div[2]/div/div/div[9]/div[2]'
        driver.find_element(by=By.XPATH,value=Xpath2).click()
    else:
        xPath='/html/body/div/div/div[3]/div/div[3]/div/div[3]/div/textarea'
        driver.find_element(by=By.XPATH,value=xPath).send_keys(Query)
        sleep(3)
        Xpath2='/html/body/div/div/div[3]/div/div[3]/div/div[2]/div/div/div[9]/div'
        driver.find_element(by=By.XPATH,value=Xpath2).click()

    
def ResultScrapper():
    global Chatnumber
    Chatnumber=str(Chatnumber)
    Xpath=f'/html/body/div/div/div[3]/div/div[2]/div[{Chatnumber}]/div[2]/div/div[1]'
    Text=driver.find_element(by=By.XPATH,value=Xpath).text
    speak(Text)
    ChatnumberNew=int(Chatnumber)+2
    Chatnumber=ChatnumberNew
    return Text
# Button timer
# sleep(5)
# def gsearch():
#     X_path="/html/body/div[2]/div[2]/div[1]/div[2]"
#     driver.find_element(by=By.XPATH,value=X_path).click()
# gsearch()
# def loginbttn():
#     X_path1="/html/body/div/div/div[1]/div[2]/div/div[2]/button"
#     driver.find_element(by=By.XPATH,value=X_path1).click()
# loginbttn()
# def loginwg():
#     X_path1="/html/body/div[2]/div[2]/div/div[5]"
#     driver.find_element(by=By.XPATH,value=X_path1).click()
# loginwg()
speak("Hello, I am koro, an AI chat Bot at your assistance, I am here to help you, but before we move forward, do you want me to store our conversation in a text file ?")
a=True
while a:
    firstcommand=speechrecognition()
    if firstcommand== 'yes please':
            speak("You will find our chat in conversation.txt")
            f =open("Conversation.txt","w") 
            while True:
                Query=speechrecognition()
                SendMessage(Query=Query)
                if len(Query)==0:
                    speak("Sorry, I didn't quiet get you, could you please repeat ?")
                    sleep(2)
                    pass
                elif Query== 'exit':
                    speak("Goodbye!")
                    a=False
                    break 
                else:
                    f.write("User : ")
                    f.write(Query)
                    f.write('\n')
                    iconap()
                    op=ResultScrapper()
                    f.write("Koro : ")
                    f.write(op)
                    f.close()        

    elif len(firstcommand)==0:
        speak("Sorry, I didn't quiet get you, could you please repeat ?")
        sleep(2)
        pass
    else:
        speak("Continuing chat without saving")
        while True:
            Query=speechrecognition()
            SendMessage(Query=Query)
            if len(Query)==0:
                speak("Sorry, I didn't quiet get you, could you please repeat ?")
                sleep(2)
                pass
            elif Query== 'exit':
                speak("Goodbye!")
                a=False
                break 
            else:
                iconap()
                ResultScrapper()


# Website timer
# while True:
#     Query=speechrecognition()
#     SendMessage(Query=Query)
#     if len(Query)==0:
#         sleep(2)
#         pass
#     elif Query== 'exit':
#             speak("Goodbye!")
#             break 
#     else:
#         iconap()
#         ResultScrapper()
# SendMessage("Hello")
# sleep(1000)
# websiteopener()
# print("Loaded!")
#/html/body/div/div/div[3]/div/div[2]/div[2]/div[1]
#/html/body/div/div/div[3]/div/div[2]/div[4]/div[1]
#/html/body/div/div/div[3]/div/div[2]/div[6]/div[1]
#/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/p
#/html/body/div/div/div[3]/div/div[2]/div[4]/div[2]/div/div[1]/p
    #/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/p/text()

#/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[1]
#/html/body/div/div/div[3]/div/div[2]/div[4]/div[2]/div/div[1]
    #/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div
    #/html/body/div/div/div[3]/div/div[2]/div[4]/div[2]/div
#/html/body/div/div/div[3]/div/div[2]/div[2]/div[1]
#/html/body/div/div/div[3]/div/div[2]/div[4]/div[1]
    #/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div
    #/html/body/div/div/div[3]/div/div[2]/div[4]/div[2]/div
#/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[1]
#/html/body/div/div/div[3]/div/div[2]/div[4]/div[2]/div/div[1]
    #/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[1]
    #/html/body/div/div/div[3]/div/div[2]/div[4]/div[2]/div/div[1]

    #
    #/html/body/div/div/div[3]/div/div[3]/div/div[2]/div/div/div[9]/div

    #/html/body/div/div/div[3]/div/div[3]/div/div[2]/div/div/div[9]/div
    #/html/body/div/div/div[3]/div/div[3]/div/div[2]/div/div/div[9]/div[2]


    