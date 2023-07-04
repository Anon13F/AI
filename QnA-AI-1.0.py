import openai
from gtts import gTTS
import pyglet
import os

# List API yang digunakan
openai.api_key = 'YOUR_API_KEY'

# Fungsi untuk Menerima input teks dan Memberi Output berupa suara
def speak(text):
    tts = gTTS(text=text, lang='id', slow=False)
    filename = 'output.mp3'
    tts.save(filename)

    # Membuka file audio dengan pyglet
    music = pyglet.media.load(filename)

    # Memainkan audio
    music.play()

    # menjadwalkan eksekusi setelah putaran selesai
    pyglet.clock.schedule_once(lambda dt: pyglet.app.exit(), music.duration)

    # Menunggu hingga pemutaran selesai
    pyglet.app.run()

    # Menghapus file audio setelah pemutaran selesai
    os.remove(filename)

# Fungsi untuk mengambil response ChatGPT
def ChatGPT(user_input):
    prompt = "anda adalah assisten yang membantu." + user_input
    # prompt = "you are a helpful assistant." + user_input
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=128,
    temperature=0.7,
    n=1,
    stop=None
    )


    # mendapatkan response dari model
    model_response = response.choices[0].text.strip()

    # mengembalikan response dari model
    return model_response


# Menerima Input dan mengelola Output
while True:
    print("\n==== QnA ====")
    UserInput = input("User: ")
    # Pertanyaan seputar Identitas AI
    # Jawaban dari pertanyaan siapa indentitas AI
    dataJwb_i = ["siapa anda","siapa kamu"]
    for i in range(0,2):
        if UserInput == dataJwb_i[i]:
            speak("Saya adalah assistent Virtual berbasis AI bernama Miku yang di ciptakan oleh Anon13F")
            print("Miku: Saya adalah assistent Virtual berbasis AI bernama Miku yang di ciptakan oleh Anon13F")

    # Petanyaan bebas
    model_response = ChatGPT(UserInput)
    print("Miku: ", model_response)
    speak(model_response)
    
    # Lanjut atau Selesai
    tanya = input("\nLanjut?(y/n): ")
    if tanya == 'n':
        break
