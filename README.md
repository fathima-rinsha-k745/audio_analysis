🎧 Audio Pause & Repetition Detection
A Python-based system that analyzes speech audio to detect:

⏸️ Silent pauses in speech
🔁 Acoustic repetition patterns (stuttering)
🗣️ Word-level repetitions (e.g., "I I I")
This project combines signal processing and speech recognition to solve a real-world speech analysis problem.

🚀 Features
Detects pause segments with timestamps
Calculates total pause duration
Identifies repeated acoustic patterns using MFCC
Detects repeated words using speech recognition
Clean and modular Python implementation

🔄 System Pipeline
Audio Input → Preprocessing → Feature Extraction  
→ Pause Detection + Repetition Detection → Output
⚙️ Installation
pip install -r requirements.txt

▶️ Run the Project
py main.py

DEMO VIDEO
https://github.com/user-attachments/assets/dac46fdb-c853-4b19-a5a4-725e8215965d

📊 Sample Output
==================================================
🎧 AUDIO ANALYSIS RESULTS
==================================================

📁 File: samples/sample1.wav

⏸️ Pause Segments:
  ➤ [0.00s - 0.19s]
  ➤ [0.32s - 1.06s]
  ➤ [1.60s - 1.70s]
  ➤ [2.66s - 2.72s]
  ➤ [2.91s - 2.98s]
  ➤ [3.17s - 3.23s]

⏱️ Total Pause Duration: 1.22s

🔁 Acoustic Repetitions:

  🔹 Repetition 1:
     Pattern      : "Mild repetition"
     Time Range   : 2.55s - 3.30s
     Count        : 2
     Confidence   : Medium

🗣️ Word-Level Repetitions:
  ➤ No word repetitions detected

==================================================
✅ Processing Complete
==================================================

🧠 Approach
1. Audio Preprocessing
Loaded using librosa
Normalization and noise reduction applied
2. Pause Detection
RMS energy thresholding used to detect silence
3. Acoustic Repetition Detection
Audio split into segments
MFCC features extracted
Similar segments grouped as repetitions
4. Word-Level Repetition Detection
SpeechRecognition API used
Transcribed text analyzed for repeated words
⚠️ Challenges
Handling noisy audio signals
Choosing optimal thresholds
Detecting repetition without full speech understanding
Variability in speech patterns
🚀 Future Improvements
Integrate Whisper for better accuracy
Add waveform visualization
Improve real-time detection
🛠️ Tech Stack
Python
Librosa
NumPy
SciPy
SpeechRecognition
📁 Project Structure
audio-analysis/
│── main.py
│── utils.py
│── pause_detection.py
│── repetition_detection.py
│── speech_to_text.py
│── word_repetition.py
│── requirements.txt
│── README.md
│── samples/
sample.wav sample1.wav

💡 Notes
Works best with .wav files
Word detection requires internet
Results depend on audio quality
👤 Author
Fathima Rinsha K
