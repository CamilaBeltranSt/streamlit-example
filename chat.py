import streamlit as st
from PIL import Image
from streamlit_chat import message
import requests
import os
import random
import base64

def generate_response(input_text):
    url='http://127.0.0.1:8000/predict'

    params= {'user_query':input_text
         }
    response=requests.get(url=url,params=params).json()

    return response['answer_query']['Respuesta']['content']

with st.sidebar: 
    # Configuración de la página
    st.set_page_config(page_title="FunesBot Project", page_icon=":speech_balloon:")

    #Imagen
    image = Image.open("imagenfondo1.jpg") 
    st.image(image, use_column_width=True)

    # Título y texto de bienvenida
    st.title("Chatbot FunesBot Project")
    st.write("Welcome! This is a chatbot created by the FunesBot team at Data Science 1203 Le Wagon. He can answer your questions about a book. Please enter your questions in the text field below.")
    #Gatito estudioso
    #st.image(
    #    "https://i.gifer.com/Ao.gif",
    #    width=200,
    #)
    ran_gif = random.randint(1,5)
    if ran_gif == 1:
        st.image(
        "https://i.gifer.com/Ao.gif",
        width=200,
    )

    if ran_gif == 2:
        st.image(
            "https://i.gifer.com/48Z.gif",
            width = 200,

        )

    if ran_gif == 3:
        st.image(
            "https://i.gifer.com/2GU.gif",
                    width = 200,

        )

    if ran_gif == 4:
        st.image(
            "https://i.gifer.com/Aw.gif",
                                width = 200,

        )

    if ran_gif == 5:
        st.image(
            "https://i.gifer.com/A7PB.gif",
                                width = 200,

        )
   #Musica autoreproducción en sidebar
    #def autoplay_audio(file_path: str):
    #     with open(file_path, "rb") as f:
    #         data = f.read()
    #         b64 = base64.b64encode(data).decode()
    #         md = f"""
    #             <audio controls autoplay="true">
    #             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    #             </audio>
    #             """
    #         st.markdown(
    #             md,
    #             unsafe_allow_html=True,
    #         )
    #st.write("Ambiental Music!")
    #autoplay_audio("music.mp3")

#Define imagen de fondo principal
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
         encoded_string = base64.b64encode(image_file.read())
    st.markdown(
     f"""
     <style>
     .stApp {{
         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
         background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
     )
add_bg_from_local('duotone.png')

def main():  
   
    ##  CHATBOT 
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if user_input := st.chat_input("Enter your question here:"):
        # Display user message in chat message container
        st.chat_message("user").markdown(user_input)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = generate_response(user_input)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
if __name__ == "__main__":
    main()