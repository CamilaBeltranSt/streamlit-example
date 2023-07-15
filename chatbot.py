import streamlit as st
from PIL import Image
from streamlit_chat import message
import requests
import os
import random
import base64

def generate_response(input_text):
    url='http://127.0.0.1:4000/predict'

    params= {'user_query':input_text
         }
    response=requests.get(url=url,params=params).json()

    return response['answer_query']['Respuesta']['content']

def main():
    # Configuración de la página
    st.set_page_config(page_title="FunesBot Project", page_icon=":speech_balloon:")
    
    #Imagen de fondo
    image = Image.open("iamegenfondo.jpg") 
    st.image(image, use_column_width=True)

    # Título y texto de bienvenida
    st.title("Chatbot FunesBot Project ")
    st.write("Welcome! This is a chatbot created by the FunesBot team at Data Science 1203 Le Wagon. He can answer your questions about a book. Please enter your questions in the text field below.")

    # Lista para almacenar el historial de preguntas y respuestas
    if 'message' not in st.session_state:
        st.session_state['message'] = []
    
    messages = st.session_state['message'] 
    
    placeholder = st.empty()
    # Área de texto para que el usuario ingrese la pregunta
    user_input = st.text_input("Enter your question here:")
    button = st.button("Send")
    
    # Verificar si se presiona la tecla Enter en el teclado
    if user_input and (button or st.session_state.enter_pressed):
        # Generar respuesta
        response = generate_response(user_input)

        # Agregar la pregunta y respuesta al historial
        messages.append((user_input, response))
        
        # Restablecer el valor de enter_pressed
        st.session_state.enter_pressed = False

    # Mostrar el historial de preguntas y respuestas
    #container = st.container()
    with placeholder.container():
        for i, (question, answer) in enumerate(messages, 1):
                message(question, True, key=str(i*2))
                #st.write(f"**Question {i}:** {question}")
                message(answer, False, key=str(i*2+1))
                #st.write(f"**Answer {i}:** {answer}")
    
    if st.button('Restart Chat'):
      st.session_state['message'] = []
      placeholder.empty()
     
    # Mostrar la respuesta más reciente
    #if len(messages) > 0:
     #   st.subheader("Respuesta más reciente:")
      #  st.text(messages[-1][1])
        
    
if __name__ == "__main__":
    main()