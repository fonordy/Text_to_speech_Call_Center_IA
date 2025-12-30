# =================================================================
# Proyecto: AI Call Center Analyzer & Speech Validator
# Descripción: Transcripción con Whisper y Auditoría con GPT-3.5
# =================================================================

import whisper
from openai import OpenAI
from docx import Document
import os

# --- 1. FUNCIONES DE UTILIDAD ---

def leer_documento_word(ruta_archivo):
    """Lee un archivo .docx y devuelve el texto completo."""
    try:
        documento = Document(ruta_archivo)
        texto_completo = []
        for parrafo in documento.paragraphs:
            texto_completo.append(parrafo.text)
        return "\n".join(texto_completo)
    except Exception as e:
        print(f"Error al leer el archivo Word: {e}")
        return "Guion base no encontrado."

# --- 2. CONFIGURACIÓN DE RUTAS Y CLIENTES ---

# NOTA: Reemplaza con tus archivos locales para pruebas
ruta_archivo_guion = "tu_guion_de_ventas.docx" 
texto_speech = leer_documento_word(ruta_archivo_guion)

# SEGURIDAD: Se recomienda usar variables de entorno para la API Key
# En local puedes usar: os.environ["OPENAI_API_KEY"] = "tu_key"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "TU_API_KEY_AQUI")
client = OpenAI(api_key=OPENAI_API_KEY)

# --- 3. PROCESAMIENTO DE AUDIO (WHISPER) ---

print("Cargando modelo Whisper...")
model = whisper.load_model("base")

# Lista de audios a procesar
archivos_audio = [
    "Llamada_Hot_Lead_1.mp3",
    "Llamada_Hot_Lead_2.mp3",
    "Llamada_Hot_Lead_3.mp3",
    "Llamada_Hot_Lead_4.mp3",
    "Llamada_Hot_Lead_5.mp3"
]

textos_transcritos = {}

print("Iniciando transcripciones...")
for archivo in archivos_audio:
    if os.path.exists(archivo):
        print(f"Transcribiendo: {archivo}...")
        resultado = model.transcribe(archivo)
        textos_transcritos[archivo] = resultado['text']
    else:
        print(f"Aviso: El archivo {archivo} no se encontró en la ruta local.")

# --- 4. ANÁLISIS DE INTELIGENCIA DE NEGOCIO (GPT) ---

if textos_transcritos:
    # --- Pregunta 1: Análisis de Interés ---
    prompt_interes = f"""
    Analiza las siguientes 5 transcripciones de conversaciones de venta. 
    Determina por separado el nivel de interés de cada cliente.
    Indica un porcentaje estimado de interés por cada una y concluye quién es 
    el cliente más interesado y el menos interesado:
    \n{textos_transcritos}
    """

    print("\nGenerando reporte de interés del cliente...")
    resp_interes = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en análisis de ventas y calidad."},
            {"role": "user", "content": prompt_interes},
        ]
    )
    print("REPORTE DE INTERÉS:")
    print(resp_interes.choices[0].message.content)

    # --- Pregunta 2: Validación de Speech Text ---
    prompt_validacion = f"""
    Compara las siguientes transcripciones contra el guion de ventas (Speech Text) proporcionado.
    Dime si cada conversación se alinea o se desvía del guion, detalla similitudes 
    y entrega un porcentaje de cumplimiento por llamada:
    \nGuion: {texto_speech}
    \nTranscripciones: {textos_transcritos}
    """

    print("\nGenerando reporte de cumplimiento de script...")
    resp_validacion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un auditor de calidad de Call Center."},
            {"role": "user", "content": prompt_validacion},
        ]
    )
    print("REPORTE DE CUMPLIMIENTO:")
    print(resp_validacion.choices[0].message.content)
else:
    print("No hay transcripciones disponibles para analizar.")
