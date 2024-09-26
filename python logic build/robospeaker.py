import pyttsx3

while True:

    if __name__ == '__main__':
        print("Welcome to comp speaker 1.0, created by me")
        x = input("What do you want me to say: ")
        
        if x.spl().lower() == 'quit':
            print("Program terminated")
            break


        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait

        print(f'I just said: "{x}"')
