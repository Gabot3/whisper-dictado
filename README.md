📘 README.md — VERSIÓN 1.0 (PROFESIONAL + HUMANA)
# Whisper Dictado 🎤🧠

Dictado por voz en Linux utilizando **Whisper** y **LLM local (Ollama)**,  
con atajo global y extensión para navegador.

Productividad, privacidad y software libre, todo en uno.


🚀 ¿Qué es Whisper Dictado?
Whisper Dictado es una herramienta para Linux que te permite:
Hablar por micrófono 🎙️
Transcribir tu voz a texto usando Whisper
(Opcional) Mejorar el texto con un modelo de lenguaje local
Copiar automáticamente el resultado al portapapeles
Pegar el texto en cualquier aplicación (mail, chat, documento, etc.)
Todo el procesamiento se realiza localmente, sin enviar audio ni texto a la nube.

🎯 ¿Para qué sirve?
Este proyecto nace de una necesidad real:
Redactar correos profesionales más rápido
Crear minutas y notas técnicas sin tipear
Usar IA como herramienta diaria, no como curiosidad
Mantener control total sobre los datos
Ideal para:
Profesionales IT
Usuarios Linux
Personas que valoran la privacidad
Entornos corporativos

✨ Características principales
🎙️ Dictado por voz con Whisper
🧠 Mejora opcional de texto con LLM local (Ollama)
⌨️ Atajo global configurable
🌐 Extensión para Brave (compatible Chromium)
🔔 Notificaciones de estado
🔒 100 % local y privado
🐧 Diseñado para Ubuntu / Linux



🖥️ Requisitos del sistema
Ubuntu 22.04+ (probado en 24.04)
Python 3.10 o superior
arecord
zenity
notify-send
Whisper
Ollama (opcional, para LLM)






📦 Instalación
Opción 1 — Paquete .deb (recomendado)
sudo dpkg -i whisper-dictado.deb

Próximamente disponible en la sección Releases.
Opción 2 — Instalación manual (desarrolladores)
git clone https://github.com/gabot3/whisper-dictado.git
cd whisper-dictado
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 dictar.py

▶️ Uso
Ejecutar Whisper Dictado (atajo global o extensión)
Comenzar a hablar 🎙️
Presionar ACEPTAR para detener la grabación
Esperar la notificación de “Transcripción lista”
Pegar el texto con Ctrl + V
🧠 Uso de LLM (opcional)
Whisper Dictado puede mejorar el texto utilizando un modelo local.
Archivo de configuración:
~/.config/whisper-dictado/config.toml
Ejemplo:
use_llm = true

<img width="501" height="93" alt="Captura desde 2026-02-09 18-28-59" src="https://github.com/user-attachments/assets/7d1794da-c9eb-4e4b-af12-0ab1cc173ae0" />
<img width="548" height="369" alt="Captura desde 2026-02-09 18-29-09" src="https://github.com/user-attachments/assets/99d2f50d-3b58-4260-ae20-3455ff556300" />
<img width="501" height="93" alt="Captura desde 2026-02-09 18-30-23" src="https://github.com/user-attachments/assets/28b11008-2971-4831-955e-4efa1761abfa" />





Modelos recomendados:
phi3 → rápido y eficiente en CPU
llama3 → mejor calidad, más lento
El prompt puede modificarse directamente en dictar.py.

🔐 Privacidad
El audio se graba de forma temporal
El archivo de audio se elimina automáticamente
No se envía información a internet
El LLM se ejecuta de forma local
Tus datos son tuyos.

🧩 Arquitectura (resumen)
Micrófono
   ↓
Audio temporal
   ↓
Whisper (STT)
   ↓
LLM local (opcional)
   ↓
Portapapeles


📄 Licencia
Este proyecto es freeware y open source.
Licencia recomendada: MIT


👥 Créditos
Idea, testing y concepto: Gabot3
Desarrollo y arquitectura: ChatGPT
Tecnologías: Whisper, Ollama, Python, Linux

❤️ Filosofía
Este proyecto fue creado con una idea clara:
Usar la inteligencia artificial como una herramienta real,
cotidiana y al servicio de las personas,
respetando la privacidad y el software libre.

Para el mundo con cariño!! 

Gabot3
