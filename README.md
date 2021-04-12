# Streamlit-NER-app

INSTRUCTIONS:

CODE FILE- part.py

MODULES USED- Specified in requirements.txt

procfile- To run program with streamlit  


WORKING:


This project works on Named Entity Recognition(NER) which is used to classify named entities in text into pre-defined categories such as Person's name,organisation,date,location and so on.In this project, I have worked with spacy module to peform NER.In this,we load the en_core_web_sm pipeline using spacy.load(), which will return all the components and data needed to process the text.
Afetr that,I have inserted an input box with streamlit to enter the user data.This data is then searched in the wikipedia using wikipedia.summary(),which has two parameters.
First one is the data to be searched and the second one is the number of sentences to be fetched from wikipedia.
I have also inserted a conditional statement which checks if the user has entered the text or not.
Afetr this,I have called nlp object on a string of text which will return a processed text. 
Then, I have used spacy_streamlit which is used for building interactive spacy powered apps with streamlit. I have called visualize_ner() method which visualise the named entities using displacy visualiser.It's parameter labels is used to show the entities in a drop down table.It provides an excellent feature to keep the entities of our choice and omit others at a time.
If user dosen't enter any text,it will go in else part,where I have used write command of streamlit to display the message on streamlit app.

LIVE URL:

After creating a web app using streamlit,I have deployed my project on heroku platform.
Here's the link to access the project on heroku:

https://stream-nerapp.herokuapp.com/

