import pyttsx3 as ai
import speech_recognition as mic_test

listening = mic_test.Recognizer()
def talk_ai(talk):
    print(talk)
    ai.init()
    ai.speak(talk)
def mic_testing():
    command = ""
    try:
        with mic_test.Microphone() as mic:
            talk_ai("Do you have any questions that you can ask? ")
            uservoice = listening.listen(mic)
            command = listening.recognize_google(uservoice)
            command = command.lower()
    except:
        pass
        print("no mic")
    return command

def is_question_contain(text):
    return text in mic_testing()

talk_ai("Hello. My name is Jacob your AI friend")
while True:
    if is_question_contain("your favorite food"):  # Jacob. What is your favorite food?
        talk_ai("My favorite food is spaghetti")
    elif is_question_contain("your course"):  # Jacob What is your course?
        talk_ai("My course is BSIT or Bachelor of Science in Information and Technology")
    elif is_question_contain("your relationship status"):  # Jacob. What is your relationship status right now?
        talk_ai("My relationship status is Single")
    elif is_question_contain("that is enough"): # Ok Jacob that is enough - end the program
        talk_ai("Ok thank you")
        break