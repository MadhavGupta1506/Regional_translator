import streamlit as st
import lang
st.title("Welcome to langauage translator")
languages="""English,Hindi,Bengali,Telugu,Marathi,Tamil,Urdu,Gujarati,Kannada,Odia,Punjabi,Malayalam,Assamese,Konkani,Kashmiri,Manipuri (Meitei)""".split(",")
language1=st.sidebar.selectbox("Select language to translate from",options=languages)
sentence=st.text_input("Type here")
language2=st.sidebar.selectbox("Select language to translate",options=languages)
# print(sentence)
st.write(lang.get_response(sentence,language1,language2))