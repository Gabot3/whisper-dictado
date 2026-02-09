#!/bin/bash

notify-send "Whisper" "Dictado iniciado 🎤"

cd /home/gabot3/whisper-lab || exit 1
source venv/bin/activate

python dictar.py
