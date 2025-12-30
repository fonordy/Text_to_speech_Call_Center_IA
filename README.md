# 🎙️ AI Call Center Analyzer & Speech Validator

> **Artificial Intelligence & Natural Language Processing**
> Sistema avanzado de auditoría que automatiza la transcripción de llamadas con **OpenAI Whisper** y valida el cumplimiento de guiones de venta mediante **GPT-3.5 Turbo**.

---

## 📖 Descripción del Proyecto
Este sistema soluciona el desafío crítico de la gestión de calidad en centros de llamadas. El flujo de trabajo no solo transforma audio en texto, sino que realiza una **auditoría semántica** comparativa. 

El modelo analiza el nivel de interés del cliente y mide qué tan fiel fue el agente al "Speech Text" (guion institucional), entregando métricas porcentuales de cumplimiento y éxito.



## 🛠️ Stack Tecnológico
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-Black?style=for-the-badge&logo=openai&logoColor=white)
![Microsoft Word](https://img.shields.io/badge/Microsoft%20Word-2B579A?style=for-the-badge&logo=microsoft-word&logoColor=white)

---

## ⚙️ Características Técnicas
* **Transcripción Multi-archivo:** Procesamiento por lotes (batch processing) de archivos MP3/WAV utilizando el modelo **Whisper**.
* **Integración de Documentos:** Lectura y extracción de texto de archivos `.docx` mediante `python-docx` para establecer la base de cumplimiento (Ground Truth).
* **Análisis de Sentimiento e Interés:** Ingeniería de prompts para clasificar el interés del cliente y detectar leads calificados (Hot Leads).
* **Auditoría de Cumplimiento:** Evaluación comparativa entre la llamada real y el guion corporativo, identificando desviaciones y áreas de mejora.

---

## 📂 Estructura del Repositorio
```text
.
├── modelo_audio_rena.py  # Script principal de procesamiento y auditoría
├── install_lib.ipynb     # Notebook para configuración rápida de dependencias
├── requirements.txt      # Listado de librerías necesarias
└── README.md             # Documentación del proyecto
