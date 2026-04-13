from youtube_transcript_api import YouTubeTranscriptApi

transcript = YouTubeTranscriptApi.get_transcript('bTA8sjgvA4c')
with open('transcript.txt', 'w', encoding='utf-8') as f:
    for entry in transcript:
        f.write(entry['text'] + '\n')
