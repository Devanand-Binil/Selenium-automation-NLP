#IMPORTING Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import speech_recognition

import pyttsx3

#-----------------------------------------------------------------------------------------------------------------------

#Speech Synthesis
ts=pyttsx3.init()
ts.setProperty("rate",160)
voices=ts.getProperty('voices')
ts.setProperty("voice",voices[1].id)

#-----------------------------------------------------------------------------------------------------------------------

#Web Driver initialisation
rc = speech_recognition.Recognizer()
driver = webdriver.Chrome()
driver.get("https://deepai.org/")
login = WebDriverWait(driver,100).until(lambda driver: driver.find_element('xpath','''/html/body/header/a[3]'''))
login.click()
time.sleep(2)
gmail= WebDriverWait(driver,100).until(lambda driver: driver.find_element('xpath','''//*[@id="login-modal"]/div/form/button[2]'''))
gmail.click()
gmailusername= WebDriverWait(driver,100).until(lambda driver: driver.find_element('xpath','''//*[@id="login-user-email"]'''))
gmailusername.send_keys("devanedu@gmail.com")
gmailpassw= WebDriverWait(driver,100).until(lambda driver: driver.find_element('xpath','''//*[@id="login-user-password"]'''))
gmailpassw.send_keys("devanedu"+Keys.ENTER)
time.sleep(5)
mess= WebDriverWait(driver,100).until(lambda driver: driver.find_element('xpath','''//*[@id="chatSubmitButton"]'''))
mess.click()
mesbox=WebDriverWait(driver,100).until(lambda driver: driver.find_element('xpath','''//*[@id="chatboxWrapperId_0"]/textarea'''))
mesbox.send_keys("Hello"+Keys.ENTER)
num=0
div=4
mes="Initiate001"

#----------------------------------------------------------------------------------------------------------------------
#Chat Mechanism
while True:
    #time.sleep(10)


    check=driver.find_element('xpath','''/html/body/div['''+str(div)+''']''').text[-6:].replace(" ","")
    csd="Delete"
    while check!=csd:
        check = driver.find_element('xpath', '''/html/body/div[''' + str(div) + ''']''').text[-6:].replace(" ","")

    print("Nami :"+driver.find_element('xpath','''/html/body/div['''+str(div)+''']''').text[:-21])
    ts.say(driver.find_element('xpath','''/html/body/div['''+str(div)+''']''').text[:-21])
    ts.runAndWait()
    if mes=="goodbye":
        break
    num=num+1
    div=div+2
    mesbox = WebDriverWait(driver, 100).until(lambda driver: driver.find_element('xpath', '''//*[@id="chatboxWrapperId_'''+str(num)+'''"]/textarea'''))
#---------------------------------------------------------
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                print("Say something")

                rc.adjust_for_ambient_noise(mic, duration=0.2)
                audio = rc.listen(mic)
                text = rc.recognize_google(audio)
                text = text.lower()
                print("You : "+text)
                break
        except speech_recognition.UnknownValueError:
            rc = speech_recognition.Recognizer()
            continue
    mes=text
    mesbox.send_keys(mes + Keys.ENTER)

#-----------------------------------------------------------------------------------------------------------------------


