#!/usr/bin/env python3
"""Word-level timestamps for a voiceover (faster-whisper, base.en, CPU).

  python3 production/shorts/words.py voice.mp3  -> prints JSON [[start, end, word], ...]

Audio is decoded with ffmpeg (16 kHz mono float) to avoid the PyAV dependency.
Model download needs huggingface.co + us.aws.cdn.hf.co allowed (environment, 2026-11-23).
"""
import json, subprocess, sys, os
import numpy as np
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
from faster_whisper import WhisperModel


def words(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'],
                         capture_output=True, check=True).stdout
    audio = np.frombuffer(raw, np.float32)
    m = WhisperModel('base.en', device='cpu', compute_type='int8')
    segs, _ = m.transcribe(audio, word_timestamps=True)
    return [[round(w.start, 2), round(w.end, 2), w.word.strip()] for s in segs for w in s.words]


if __name__ == '__main__':
    print(json.dumps(words(sys.argv[1])))
