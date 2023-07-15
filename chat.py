import streamlit as st
from PIL import Image



def generate_response(input_text):
    # Aquí puedes agregar la lógica para generar la respuesta del modelo GPT
    # Basado en el texto de entrada
    # Puedes utilizar tu propio modelo o una API de chatbot como OpenAI GPT-3

    # Ejemplo de respuesta estática
    response = "Hola, soy un chatbot. ¿En qué puedo ayudarte?"

    return response

def main():
    # Configuración de la página
    st.set_page_config(page_title="Chatbot con Streamlit", page_icon=":speech_balloon:")

    #Imagen de fondo
    image = Image.open("iamegenfondo.jpg") 
    st.image(image, use_column_width=True)
    
    # Título y texto de bienvenida
    st.title("Chatbot con Streamlit")
    st.write("¡Bienvenido! Este es un chatbot que puede responder tus preguntas.")

    # Lista para almacenar los mensajes
    messages = []

    # Bucle continuo de preguntas y respuestas
    while True:
        # Mostrar mensajes anteriores y entrada del usuario
        for message in messages:
            if message["from_user"]:
                st.chat_message(message["content"])
            else:
                st.write(f"> {message['content']}")

        # Obtener la entrada del usuario
        user_input = st.chat_input("Escribe un mensaje...")

        # Agregar mensaje del usuario a la lista
        messages.append({"content": user_input, "from_user": True})

        # Generar respuesta
        response = generate_response(user_input)

        # Agregar mensaje del bot a la lista
        messages.append({"content": response, "from_user": False})

        # Mostrar la conversación completa
        st.subheader("Conversación completa")
        for message in messages:
            if message["from_user"]:
                st.text_input("Usuario", message["content"], key=message["content"])
            else:
                st.text_input("Chatbot", message["content"], key=message["content"])

        # Opción para hacer otra pregunta
        another_question = st.button("Hacer otra pregunta")
        if not another_question:
            break

if __name__ == "__main__":
    main()
