from utils import load_audio, remove_noise
from pause_detection import detect_pauses
from repetition_detection import detect_repetitions

from speech_to_text import transcribe_audio
from word_repetition import detect_word_repetition

audio_path = "samples/sample1.wav"

print("Loading audio...")
y, sr = load_audio(audio_path)

if y is None:
    print("❌ Error: Could not load audio file.")
    exit()

y = y[:sr * 5]

print("Removing noise...")
y = remove_noise(y)

print("Detecting pauses...")
pauses, total_pause = detect_pauses(y, sr)

print("Detecting acoustic repetitions...")
repetitions = detect_repetitions(y, sr)

print("Transcribing speech...")
text = transcribe_audio(audio_path)

print("Transcribed Text:", text)

print("Detecting word-level repetitions...")
word_reps = detect_word_repetition(text)


print("\n" + "="*50)
print("🎧 AUDIO ANALYSIS RESULTS")
print("="*50)

print(f"\n📁 File: {audio_path}\n")


print("⏸️ Pause Segments:")
if pauses:
    for start, end in pauses:
        print(f"  ➤ [{start:.2f}s - {end:.2f}s]")
else:
    print("  ➤ No pauses detected")

print(f"\n⏱️ Total Pause Duration: {total_pause:.2f}s\n")


print("🔁 Acoustic Repetitions:")
if repetitions:
    for idx, rep in enumerate(repetitions, 1):
        print(f"\n  🔹 Repetition {idx}:")
        print(f'     Pattern      : "{rep["pattern"]}"')
        print(f'     Time Range   : {rep["start"]:.2f}s - {rep["end"]:.2f}s')
        print(f'     Count        : {rep["count"]}')
        print(f'     Confidence   : {rep["confidence"]}')
else:
    print("  ➤ No acoustic repetitions detected")


print("\n🗣️ Word-Level Repetitions:")

if word_reps:
    for idx, rep in enumerate(word_reps, 1):
        print(f"\n  🔹 Repetition {idx}:")
        print(f'     Word   : "{rep["word"]}"')
        print(f'     Count  : {rep["count"]}')
else:
    print("  ➤ No word repetitions detected")

print("\n" + "="*50)
print("✅ Processing Complete")
print("="*50)