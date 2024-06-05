import requests
import openai


def getDataFromKeyboard():
    fraseTeclado = input()
    return fraseTeclado

def getDataFromServer(URL):
    API_KEY = 'pPb418u25lwWTU6MwkOOdw==SJLn4cC8fasbzkyD'
    response = requests.get(URL,headers={'X-Api-Key':API_KEY})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:",response.status_code,response.text)

import requests
def getDataFromChatGPT(prompt):

    openai.api_key = "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"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6
    )
    return response.choices[0].text

def getDataFromFile(fileName):
    dades=""
    return dades



    
