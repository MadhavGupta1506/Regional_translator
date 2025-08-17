import streamlit as st
import lang
st.title("Welcome to language translator")
languages="""English,Hindi,Bengali,Telugu,Marathi,Tamil,Urdu,Gujarati,Kannada,Odia,Punjabi,Malayalam,Assamese,Konkani,Kashmiri,Manipuri (Meitei)""".split(",")
language1=st.sidebar.selectbox("Select language to translate from",languages,)
sentence=st.text_input("Type here")
language2=st.sidebar.selectbox("Select language to translate",languages)
# print(sentence)
if(sentence and language1 and language2):
    
    now=st.write(lang.get_response(sentence,language1,language2))
else:
    now=st.write("Hello! how can I help?")