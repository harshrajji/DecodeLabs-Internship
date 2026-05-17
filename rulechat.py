import datetime
import random

responses = {
    "hi": "Hey there! How can I help you? 😊",
    "hello": "Hey there! How can I help you? 😊",
    "hey": "Hey there! How can I help you? 😊",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "how are you?": "I'm doing great, thanks for asking! How about you?",
    "how r u": "I'm doing great, thanks for asking! How about you?",
    "what is your name": "I'm HarshBot, your personal assistant! 🤖",
    "what's your name": "I'm HarshBot, your personal assistant! 🤖",
    "who are you": "I'm HarshBot, your personal assistant! 🤖",
    "who made you": "I was created by Harsh Raj as part of the DecodeLabs Internship project! 🚀",
    "who created you": "I was created by Harsh Raj as part of the DecodeLabs Internship project! 🚀",
    "i am sad": "Aww, cheer up! 😊 You're doing amazing. Keep going!",
    "i'm sad": "Aww, cheer up! 😊 You're doing amazing. Keep going!",
    "i feel sad": "Aww, cheer up! 😊 You're doing amazing. Keep going!",
    "i am happy": "That's wonderful! Stay positive and keep smiling! 😄",
    "i'm happy": "That's wonderful! Stay positive and keep smiling! 😄",
    "i feel happy": "That's wonderful! Stay positive and keep smiling! 😄",
}

print("=" * 40)
print("   Welcome to HarshBot 🤖")
print("   Type 'bye' or 'exit' to quit")
print("=" * 40)

while True:
    user = input("\nYou: ").lower().strip()

    static_reply = responses.get(user)

    if static_reply:
        print(f"Bot: {static_reply}")

    elif user in ["what is today's date", "today's date", "date"]:
        today = datetime.date.today().strftime("%d %B %Y")
        print(f"Bot: Today's date is {today}.")

    elif user in ["what is the time", "what time is it", "time"]:
        now = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {now}.")

    elif user in ["tell me a joke", "joke", "say something funny"]:
        jokes = [
            "Why do Java developers wear glasses? Because they don't C#! 😄",
            "Why did the programmer quit? Because he didn't get arrays! 😂",
            "What do you call a programmer from Finland? Nerdic! 😁"
        ]
        print(f"Bot: {random.choice(jokes)}")

    elif user.startswith("calculate "):
        try:
            expression = user.replace("calculate ", "")
            result = eval(expression)
            print(f"Bot: The answer is {result}")
        except:
            print("Bot: Sorry, I couldn't calculate that. Try something like 'calculate 5 + 3'.")

    elif user in ["help", "what can you do"]:
        print("Bot: I can help you with:")
        print("     - Greetings")
        print("     - Current date & time")
        print("     - Jokes")
        print("     - Simple calculations (e.g. 'calculate 5 + 3')")
        print("     - Mood check-ins")

    elif user in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    else:
        print("Bot: Hmm, I didn't quite get that. Type 'help' to see what I can do!")