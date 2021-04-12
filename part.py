import streamlit as st
import spacy_streamlit                   #Helps to visualise spacy models with streamlit
import wikipedia                         #This module helps to fetch data from wikipedia
import spacy                             #It helps to perform NER easily
nlp=spacy.load("en_core_web_sm")          #to load spacy model
st.title("NAMED ENTITY RECOGNITION")
st.subheader("NER")
text=st.text_input("Enter serach topic: ")    #to take text_input in streamlit
if text:
    raw_text=wikipedia.summary(text,sentences=6)   #to fetch article from a summary even with fixed number of sentences
    doc=nlp(raw_text)
    spacy_streamlit.visualize_ner(doc,labels=nlp.get_pipe('ner').labels)
    #Helps to visualise any named entity in our text
else:
    st.write("Nothing entered")     #To write on streamlit