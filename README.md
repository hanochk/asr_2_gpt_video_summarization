# asr_2_gpt_video_summarization
Video summarization by ARS based video sound-track plot transcription

This Soundtrack based video summarization demonstrates the ability to use video transcription for summarization as an additional source of information but not limited to.

ASR engine based on OpenAI Whisper

GPT : both OpenAI GPT3.x and TBD: ChatGPT

Use case : 
Your TL:DR for movie trailers or clip that you can hear while you are driving in a car and ask your PDA “GPT please summarizes for me the movie of John Wick : Chapter 4 by Keanu Reeves”

'https://www.youtube.com/watch?v=qEVUtrk8_B4&t=5s&ab_channel=LionsgateMovies'

♪♪ Say goodbyes? Say hello. ♪♪ You think your wife can hear you? No. Then why bother? ♪♪ Maybe I'm wrong. ♪♪ You're going to die. Maybe not. ♪ Goodbye to you, my trusted friend ♪ ♪♪ A new day is dawning. New ideas, new rules, new management. ♪ We've known each other since we were in my hotel ♪ Who is this? The Marquis de Gramont. Challenge him to single combat. Win or lose, it's a way out. I don't sit at the table. Your family does. ♪ Please pray for me ♪ ♪ I was the black sheep of the family ♪ A man has to look his best when it's time to get married. Or buried. I'm going to need a gun. ♪ Goodbye, my friend, it's hard to die now ♪ ♪♪ If you win, the table will honor its word. You'll have your freedom. ♪ It's hard to die now ♪ Under the old laws, only one can survive. Failure to meet its sunrise will result in execution. ♪♪ Last words, Winston? Just have fun out there. ♪♪ I want you to find your peace. But a good death only comes after a good life. ♪♪ You and I left a good life behind a long time ago, my friend. ♪♪ Let's start again. ♪♪

GPT: 
"This song summarizes a story of two people who have been friends for years. They accept the challenge by the Marquis de Gramont to a single combat, with the understanding that one of them will die. They accept this as a way out, despite the chance of the other being executed for failure to meet sunrise if he does not win. They acknowledge the good life they left behind and encourage each other to find peace, with the last words being for the other to 'just have fun out there'. The song ends with a call to start again and a goodbye."


Prerequisite
pip install git+https://github.com/openai/whisper.git
pip install git+https://github.com/mmabrouk/chatgpt-wrapper
pip install -r requirements.txt
