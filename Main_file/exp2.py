import speech_recognition as sr
import pyttsx3
import string

class DyslexiaLearningGame:
    def __init__(self):
        # Initialize speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Slow down speech speed for clarity
        self.engine.setProperty('volume', 1)  # Set volume to normal

        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()

        # Game state
        self.score = 0
        self.level = 1
        self.max_level = 2  # Number of levels in the game

    def speak(self, text):
        """Function to convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Function to recognize speech from microphone"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            return self.recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Can you please say that again?")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service. Please try again later.")
            return None

    def level_1_alphabet(self):
        """Level 1: Alphabet recognition game"""
        alphabet = string.ascii_lowercase  # 'a' to 'z'
        self.speak("Let's start Level 1. I will say a letter, and you need to repeat it.")
        
        for letter in alphabet:
            correct = False
            while not correct:
                self.speak(f"Say the letter: {letter.upper()}")
                user_input = self.listen()

                if user_input == letter:
                    self.speak(f"Correct! {letter.upper()} is right.")
                    self.score += 10  # Score points for correct answer
                    correct = True  # Exit loop if answer is correct
                else:
                    self.speak(f"Oops, that was not correct. The letter was {letter.upper()}. Try again.")

            self.speak(f"Your current score is {self.score}.")

        # Move to next level after completing Level 1
        self.level_up()

    def level_2_sentences(self):
        """Level 2: Sentence practice game"""
        self.speak("Let's start Level 2. I will say a sentence, and you need to repeat it.")
        sentences = [
            "The cat is on the mat.",
            "I like to play outside.",
            "It is a sunny day today."
        ]

        for sentence in sentences:
            correct = False
            while not correct:
                self.speak(f"Say this sentence: {sentence}")
                user_input = self.listen()

                if user_input == sentence.lower():
                    self.speak(f"Correct! You said: {sentence}")
                    self.score += 20  # More points for correct sentence
                    correct = True  # Exit loop if sentence is correct
                else:
                    self.speak(f"Oops, that wasn't quite right. Try again.")
                    self.speak(f"The correct sentence is: {sentence}")

                self.speak(f"Your current score is {self.score}.")

        # Game ends after completing Level 2
        self.game_end()

    def level_up(self):
        """Level up to next stage of the game"""
        if self.level == 1:
            self.level = 2
            self.speak("Congratulations! You completed Level 1. Let's move on to Level 2.")
            self.level_2_sentences()
        elif self.level == self.max_level:
            self.speak("You have completed all the levels. Well done!")
            self.game_end()

    def game_end(self):
        """End of the game"""
        self.speak(f"Your final score is {self.score}. Thank you for playing!")
        self.speak("Would you like to play again?")

        user_input = self.listen()
        if "yes" in user_input:
            self.restart_game()
        else:
            self.speak("Goodbye! Hope to see you again soon.")
            exit()

    def restart_game(self):
        """Restart the game from Level 1"""
        self.score = 0
        self.level = 1
        self.speak("Restarting the game...")
        self.level_1_alphabet()

    def run(self):
        """Main game loop"""
        self.speak("Welcome to the Dyslexia Learning Game! Let's start.")
        self.level_1_alphabet()  # Start with Level 1

def main():
    game = DyslexiaLearningGame()
    game.run()

if __name__ == "__main__":
    main()
