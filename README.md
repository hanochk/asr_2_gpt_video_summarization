# asr_2_gpt_video_summarization
Video summarization by ASR based video sound-track plot transcription

This Soundtrack based video summarization demonstrates the ability to use video transcription for summarization as an additional source of information but not limited to.

ASR engine based on OpenAI Whisper

GPT : both OpenAI GPT3.x and TBD: ChatGPT


Use case : 
Your TL:DR for movie trailers or clip that you can hear while you are driving in a car and ask your PDA “GPT please summarizes for me the movie of John Wick : Chapter 4 by Keanu Reeves”

'https://www.youtube.com/watch?v=qEVUtrk8_B4&t=5s&ab_channel=LionsgateMovies'

♪♪ Say goodbyes? Say hello. ♪♪ You think your wife can hear you? No. Then why bother? ♪♪ Maybe I'm wrong. ♪♪ You're going to die. Maybe not. ♪ Goodbye to you, my trusted friend ♪ ♪♪ A new day is dawning. New ideas, new rules, new management. ♪ We've known each other since we were in my hotel ♪ Who is this? The Marquis de Gramont. Challenge him to single combat. Win or lose, it's a way out. I don't sit at the table. Your family does. ♪ Please pray for me ♪ ♪ I was the black sheep of the family ♪ A man has to look his best when it's time to get married. Or buried. I'm going to need a gun. ♪ Goodbye, my friend, it's hard to die now ♪ ♪♪ If you win, the table will honor its word. You'll have your freedom. ♪ It's hard to die now ♪ Under the old laws, only one can survive. Failure to meet its sunrise will result in execution. ♪♪ Last words, Winston? Just have fun out there. ♪♪ I want you to find your peace. But a good death only comes after a good life. ♪♪ You and I left a good life behind a long time ago, my friend. ♪♪ Let's start again. ♪♪

GPT: 
"This song summarizes a story of two people who have been friends for years. They accept the challenge by the Marquis de Gramont to a single combat, with the understanding that one of them will die. They accept this as a way out, despite the chance of the other being executed for failure to meet sunrise if he does not win. They acknowledge the good life they left behind and encourage each other to find peace, with the last words being for the other to 'just have fun out there'. The song ends with a call to start again and a goodbye."

'https://www.youtube.com/watch?v=xnvpceRnk_E&ab_channel=NBCNews'
Tonight, President Biden taking his State of the Union message on the road. Last night I reported on the State of the Union. It is strong. To battleground Wisconsin, a state he won last time by just 20,000 votes. Well, hello Madison, hello laborers. And last night's address sounding a lot like a warm up to another presidential run. Let's finish the job. We've got to finish the job. Let's finish the job. Despite polls showing most Americans think the country is on the wrong track, Mr. Biden striking an upbeat tone. I've never been more optimistic about our future. The fiery address sparking a raucous response from Republicans, including when Mr. Biden called on Congress to tackle the fentanyl crisis. But the line that brought the biggest backlash, accusing Republicans of wanting to cut popular entitlements. Some Republicans want Medicare and Social Security to sunset. I'm not saying it's a majority. The remark sparking outrage, including from conservative firebrand Marjorie Taylor Greene. Today, the president firing back. Marjorie Taylor Greene, another stood up and said, liar, liar. Minds been liar, liar, house on fire. The cuts were only officially proposed by a single Republican Senator Rick Scott last year and rejected by other Republicans, including GOP leaders. The president was saying is something that he knew was not true. I just spent an hour with him. I've said it many times before. Social Security and Medicare are off the table. In one of the most powerful moments, applause from both sides of the aisle when the president acknowledged the parents of Tyree Nichols, the faith of God. She said her son was, quote, a beautiful soul and something good will come of this. But Republicans criticizing the president for making only passing mentions of China, the border crisis and crime and accusing him of being hijacked by the, quote, radical left. The dividing line in America is no longer between right or left. The choice is between normal or crazy. And Kristen, the president says stays on the road now going to Florida tomorrow. Lester, that's right. And the White House wants to build momentum after a speech they think went well and included some savvy unscripted moments in a new interview tonight. The president said despite those interruptions, most Republicans were gracious.

GPT:

'President Biden took his State of the Union message on the road to Wisconsin, a state he narrowly won in the last election. Despite polls showing most Americans think the country is on the wrong track, the president maintained an optimistic tone. A particular point of contention was Biden accusing Republicans of wanting to sunset popular entitlements, sparking outrage such as from Marjorie Taylor Greene. Biden later clarified that the proposed cuts were only proposed by a single Republican Senator, that Social Security and Medicare are off the table, and the gesture received applause from both sides. Republicans however accused him of not acknowledging border crisis, crime, and China, and being hijacked by the radical left. The president is staying on the road now, continuing to Florida tomorrow.'


Prerequisite
pip install git+https://github.com/openai/whisper.git
pip install git+https://github.com/mmabrouk/chatgpt-wrapper
pip install -r requirements.txt
