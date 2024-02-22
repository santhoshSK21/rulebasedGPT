import speech_recognition as sr
from bs4 import BeautifulSoup
import requests
import datetime
import wikipedia
from googlesearch import search
recognizer = sr.Recognizer()
def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

def getweather(text):     
    #Sending requests to get the IP Location Information
    res = requests.get('https://ipinfo.io/')
    # Receiving the response in JSON format
    data = res.json()
    # Extracting the Location of the City from the response
    citydata = data['city']
    # Prints the Current Location
    print(citydata)
    # Passing the City name to the url
    url = 'https://wttr.in/{}'.format(citydata)
    # Getting the Weather Data of the City
    res = requests.get(url)
    # Printing the results!
    print(res.text)   
def getdate():
    # using now() to get current time
    current_time = datetime.datetime.now()
    # Printing value of now.
    print("Time now at greenwich meridian is:", current_time)
def getresult(text):
    text = text.replace('search','',1)
    print(text)
    result = wikipedia.summary(text,sentences=2)
    print(result)
def searchgoogle(text):
   # to search
    query = text

    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	    print(j)
def getjoke():
    
  url = "https://icanhazdadjoke.com/api"
  headers = {"Accept": "application/json"}
  response = requests.get(url, headers=headers)
  joke = response.json()["joke"]
  return joke

def process_voice_command(text):
    text = text.lower()
    if "hello" in text:
        print("Hello! How can I help you?")
    elif "today weather" in text :
        print("Getting Weather")
        getweather()
    elif "today date" in text :
        print("date loading")
        getdate()
    elif "search" in text:
        print("searching in wikipedia")
        getresult(text)
    elif "searchgoogle" in text:
        print("search results from google")
        searchgoogle(text)
    elif "tell jokes" in text:
        print("searching for jokes")
        joke=getjoke()
        print(joke)
    elif "goodbye" in text:
        print("Goodbye! Have a great day!")
        return True
    else:
        print("I didn't understand that command. Please try again.")
    return False
def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()
