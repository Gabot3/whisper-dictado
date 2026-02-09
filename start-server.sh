#!/bin/bash

cd /home/gabot3/whisper-lab || exit 1
source venv/bin/activate

exec python server.py
