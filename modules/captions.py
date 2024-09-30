from datetime import timedelta, datetime
import os
import whisper

def transcribe_audio(path):
    model = whisper.load_model("small") 
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    video_filename = os.path.splitext(os.path.basename(path))[0]

    os.makedirs("srtFiles", exist_ok=True)

    srt_filename = os.path.join("srtFiles", f"{video_filename}.srt")

    for segment in segments:
        text = segment['text'].strip()
        words = text.split()  
        word_count = len(words)

        start_time = float(segment['start'])
        end_time = float(segment['end'])

        duration_per_word = (end_time - start_time) / word_count

        for i, word in enumerate(words):
            word_start_time = start_time + i * duration_per_word
            word_end_time = word_start_time + duration_per_word

            start_time_formatted = (datetime(1, 1, 1) + timedelta(seconds=word_start_time)).strftime("%H:%M:%S,%f")[:-3]
            end_time_formatted = (datetime(1, 1, 1) + timedelta(seconds=word_end_time)).strftime("%H:%M:%S,%f")[:-3]

            segment_content = f"{i+1}\n{start_time_formatted} --> {end_time_formatted}\n{word}\n\n"

            # Append each word to the SRT file
            with open(srt_filename, 'a', encoding='utf-8') as srt_file:
                srt_file.write(segment_content)

    print('SRT file generated:', srt_filename)
    return srt_filename
