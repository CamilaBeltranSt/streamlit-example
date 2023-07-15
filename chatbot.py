import streamlit as st
from PIL import Image
import requests

def generate_response(input_text):
    url='http://127.0.0.1:8000/predict'

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
    messages = []

    # Bucle continuo de preguntas y respuestas
    while True:
         # Área de texto para que el usuario ingrese la pregunta
        user_input = st.text_input("Enter your question here:")

        # Verificar si se presiona la tecla Enter en el teclado
        if user_input and (st.button("Send") or st.session_state.enter_pressed):
            # Generar respuesta
            response = generate_response(user_input)

            # Agregar la pregunta y respuesta al historial
            messages.append((user_input, response))

            # Restablecer el valor de enter_pressed
            st.session_state.enter_pressed = False

        # Mostrar el historial de preguntas y respuestas
        container = st.container()
        for i, (question, answer) in enumerate(messages, 1):
                st.write(f"**Question {i}:** {question}")
                st.write(f"**Answer {i}:** {answer}")

        # Mostrar la respuesta más reciente
        if len(messages) > 0:
            st.subheader("Respuesta más reciente:")
            st.text(messages[-1][1])
        
        break
    
if __name__ == "__main__":
    main()