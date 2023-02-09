"""
References
https://github.com/mmabrouk/chatgpt-wrapper

prerequisite 
# pip install git+https://github.com/mmabrouk/chatgpt-wrapper
# pip install git+https://github.com/openai/whisper.git

"""
import pytube
import whisper
import openai

def gpt_execute(prompt_template, *args, **kwargs):
    verbose = kwargs.pop('verbose', False)            
    prompt = prompt_template.format(*args)
    try:   # Sometimeds GPT returns HTTP 503 error
        response = openai.Completion.create(prompt=prompt, max_tokens=256, **kwargs)   
        if verbose:
            print("Top K {}".format([x['index'] for x in response['choices']]))
            print("Top prompt_tokens : {} total_tokens: {}".format(response['usage']['prompt_tokens'] ,response['usage']['total_tokens']))
        # return response
        return [x['text'].strip() for x in response['choices']]
    except Exception as e:
        print(e)
        return []

def main(video_path, gpt_type='text-davinci-003'):
    data = pytube.YouTube(video_path)
    # Converting and downloading as 'MP4' file
    audio = data.streams.get_audio_only()
    path = audio.download()

    # Importing Whisper library
    # Installing Whisper libary

    model = whisper.load_model('large')
    text = model.transcribe(path)
    #printing the transcribe
    print(text['text'])
    prompt = "summarize the following :{}".format(text['text'])
    if gpt_type == 'text-davinci-003':
        rc = gpt_execute(prompt, model='text-davinci-003', n=1)
    elif gpt_type == 'chat_gpt':
    # chatgpt install
        from chatgpt_wrapper import ChatGPT
        bot = ChatGPT()
        response = bot.ask(prompt)
        print(response)  # prints the response from chatGPT
    pass





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # video_path = 'https://www.youtube.com/watch?v=qEVUtrk8_B4&t=5s&ab_channel=LionsgateMovies'
    video_path = 'https://www.youtube.com/watch?v=xnvpceRnk_E&ab_channel=NBCNews'
    main(video_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
