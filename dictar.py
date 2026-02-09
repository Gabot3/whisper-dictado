import whisper
import subprocess
import pyperclip
import tempfile
import os
os.environ.setdefault("DISPLAY", ":0")
import threading
import time
import toml
import requests

DEBUG = False

def log(msg):
    if DEBUG:
        print(msg)


CONFIG_PATH = os.path.expanduser("~/.config/whisper-dictado/config.toml")

def llm_activado():
    if not os.path.exists(CONFIG_PATH):
        return False
    try:
        config = toml.load(CONFIG_PATH)
        return config.get("use_llm", False)
    except Exception:
        return False

def mejorar_con_llm(texto):
    # Skip textos muy cortos
    if len(texto.split()) < 6:
        log("Texto muy corto, salteando LLM")
        return texto

    prompt = f"""
Reescribí el texto en español, con tono profesional y claro,
adecuado para un correo laboral. No cambies el significado.

Texto:
{texto}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["response"].strip()

    except Exception as e:
        log(f"⚠️ Error LLM, usando texto original: {e}")
        return texto


MAX_SECONDS = 600  # 10 minutos

def grabar_audio(audio_path):
    subprocess.run([
        "arecord",
        "-f", "cd",
        "-t", "wav",
        "-d", str(MAX_SECONDS),
        audio_path
    ])

log("🎤 Grabación iniciada")

with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as audio_file:
    audio_path = audio_file.name

# Lanzar grabación en thread
grabacion = threading.Thread(target=grabar_audio, args=(audio_path,))
grabacion.start()

# Ventana para detener
try:
    subprocess.run([
        "/usr/bin/zenity",
        "--info",
        "--title=Whisper Dictado",
        "--text=Grabando audio...\n\nPresioná ACEPTAR para detener y transcribir.",
    ])
except Exception as e:
    log(f"Zenity no disponible: {e}")

# Cortar grabación
subprocess.run(["pkill", "-f", audio_path])
time.sleep(0.5)

log("🧠 Cargando modelo Whisper...")
model = whisper.load_model("base")

log("✍️ Transcribiendo...")
result = model.transcribe(audio_path, language="es")

texto = result["text"].strip()

if llm_activado():
    log("🧠 LLM activado: mejorando texto...")
    texto = mejorar_con_llm(texto)
else:
    log("✍️ LLM desactivado: texto directo")


pyperclip.copy(texto)

subprocess.Popen([
    "/usr/bin/notify-send",
    "Whisper Dictado",
    "✅ Transcripción lista.\nTexto copiado al portapapeles."
])

os.remove(audio_path)

