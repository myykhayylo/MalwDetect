
import PySimpleGUI as sg
import featureExtraction
import pandas as pd 
from joblib import dump, load
import re
import numpy as np


# questa funzione si preoccupa di creare una riga da dare in input al modello di ML
def createRow(url):
    data = pd.DataFrame(columns = ['IP',"urlLenght","ShortiningServ","numDash","numEqual","dash","httpsDomSub","port","numberSub","lenghtDom","lenghtSub","lenghtPath","numLetters","numDigits","email","PunyCode","suspWords","TLD"])

    f1 = featureExtraction.isIP(url)
    f2 = featureExtraction.urlLenght(url)
    f3 = featureExtraction.usingShortiningServ(url)
    f4 = featureExtraction.numberOfDash(url)
    f5 = featureExtraction.numberOfEqual(url)
    f6 = featureExtraction.dashInDomOrSub(url)
    f7 = featureExtraction.httpsInDomOrSub(url)
    f8 = featureExtraction.port(url)
    f9 = featureExtraction.numberSub(url)    
    f10 = featureExtraction.lenghtDom(url)
    f11 = featureExtraction.lenghtSub(url)
    f12 = featureExtraction.lenghtPath(url)
    f13 = featureExtraction.numberOfLetters(url)
    f14 = featureExtraction.numberOfDigits(url)
    f15 = featureExtraction.hasEmail(url)
    f16 = featureExtraction.usingPunycode(url)
    f17 = featureExtraction.suspiciousWords(url) 
    f18 = featureExtraction.checkTLD(url)
    new_row = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18]
    data.loc[len(data)] = new_row
    return data

##il mio modello è stato allenato su url che non hanno la sottostringa "www.", e che non hanno il protocollo
#puliamo l'input
def cleanUrl(url):
    url = url.replace("www.", "")
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    return url


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('MalwDetect',font=("Helvetica",30,"bold"), text_color='red',pad=(10,30))],
            [sg.Text('Enter the URL:',font=("Helvetica",15,"bold"),pad=(10,10))],
            [sg.InputText(pad=(10,20))],
            [sg.Button('Evaluate',size=(10,2),pad=(10,20))],
            [sg.Text('',font=("Helvetica",15,"bold"),key='-status-')]]

# Create the Window
window = sg.Window('MalwDetect', layout,element_justification='c',size=(600, 400))

# load the model
modelRF = load('modelRF.joblib')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    if event == "Evaluate":
        #pulisci i campi
        window['-status-'].update("")

        userInput = values[0]

        #check if user input is a url
        url = userInput
        regex = "^[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
        r = re.compile(regex)
        if (re.search(r, url)):
           
            #clean the input
            url = cleanUrl(url)
            print("after cleaning:", url)

            #extract the feature from the url
            MLinput = createRow(url)
            #make a prediction 
            pred = modelRF.predict(MLinput)

            #print prediction
            if "legitimate" in pred:
                window['-status-'].update("legitimate",text_color=("green"))
            if "phishing" in pred:
                window['-status-'].update("phishing",text_color=("red"))
            
        else:
            #the input is not a url
            print("Not Valid")
            window['-status-'].update('INPUT NOT VALID')


window.close()


