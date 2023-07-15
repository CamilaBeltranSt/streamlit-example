import streamlit as st

class Chatbot:
    def __init__(self):
        self.messages = []

    def add_user_message(self, message):
        self.messages.append({"content": message, "from_user": True})

    def add_bot_message(self, message):
        self.messages.append({"content": message, "from_user": False})

    def show_chat(self):
        for message in self.messages:
            if message["from_user"]:
                st.text_input("Usuario", message["content"], key=message["content"])
            else:
                st.text_input("Chatbot", message["content"], key=message["content"])

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

    # Título y texto de bienvenida
    st.title("Chatbot con Streamlit")
    st.write("¡Bienvenido! Este es un chatbot que puede responder tus preguntas.")

    # Inicializar el chatbot
    chatbot = Chatbot()

    # Bucle continuo de preguntas y respuestas
    while True:
        # Mostrar la conversación completa
        st.subheader("Conversación completa")
        chatbot.show_chat()

        # Obtener la entrada del usuario
        user_input = st.text_input("Escribe un mensaje...")

        # Agregar mensaje del usuario al chatbot
        chatbot.add_user_message(user_input)

        # Generar respuesta
        response = generate_response(user_input)

        # Agregar mensaje del bot al chatbot
        chatbot.add_bot_message(response)

        # Opción para hacer otra pregunta
        another_question = st.button("Hacer otra pregunta")
        if not another_question:
            break

if __name__ == "__main__":
    main()
