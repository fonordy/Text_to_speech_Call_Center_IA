
#Importamos la liberias

import whisper
from openai import OpenAI
from docx import Document

#Lectura de archivo word

def leer_documento_word(ruta_archivo):
    documento = Document(ruta_archivo)
    texto_completo = []
    for parrafo in documento.paragraphs:
        texto_completo.append(parrafo.text)
    return "\n".join(texto_completo)

"""#Ruta del archivo del speech e impresion"""

ruta_archivo = "ponemos el script en doc para poder leerlo.docx"
texto_speech = leer_documento_word(ruta_archivo)
print(texto_speech)

"""#Insertacion de la API de OpenAI"""

OPENAI_API_KEY="*****************************" # Inserta la API de openAI, visita la web para verificar como se consume esta API
client = OpenAI(api_key=OPENAI_API_KEY)

"""# Carga el modelo Whisper."""

model = whisper.load_model("base")

"""#Se cargan los audios, puede variar, esto es de prueba"""

archivos_audio = [
    "Llamada Hot Lead_1.mp3",
    "Llamada Hot Lead_2.mp3",
    "Llamada Hot Lead_3.mp3",
    "Llamada Hot Lead_4.mp3",
    "Llamada Hot Lead_5.mp3"
    
]

"""#Diccionario para almacenar las transcripciones"""

textos_transcritos = {}

"""#Itera sobre cada archivo de audio y transcribe su contenido"""

for archivo in archivos_audio:
    resultado = model.transcribe(archivo)
    texto_transcrito = resultado['text']
    textos_transcritos[archivo] = texto_transcrito

"""#Imprime las transcripciones"""

for i, (archivo, texto) in enumerate(textos_transcritos.items(), start=1):
    print(f"{i}. {archivo}: {texto}\n")

"""#Se reliza la pregunta 1 de un analisis por cada audio"""

pregunta = f"Analiza los sigueintes textos de  conversación que en total son 5 y determina por separado si en cada una de las conversaciones el cliente esta interesado, por cada una de las conversaciones  indica el porcentaje estimado de interés y al final menciona que conversacion contiene el cliente mas y el menos interesado:\n{textos_transcritos}"

"""#Contestacion a la pregunta 1"""

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": pregunta},
  ]
)
response.choices[0].message.content

"""#Pregunta 2 sobre validacion del speech por cada audio"""

pregunta2 = f"haz una lista de las conversaciones y analiza y detalla si cada conversacion se alinea o  se esta desviando del speech text, dime cuales son las similitudes con el speech text y reflejalo en un porcentaje por cada conversacion:\n{texto_speech,textos_transcritos}"

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125", #Este modelo puede variar segun la version de gpt que deseas usar, validar en la pagina los tokens, visita la pagina oficial para mas detalles de eso
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": pregunta2},
  ]
)
response.choices[0].message.content