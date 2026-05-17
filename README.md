# DecodeLabs-Internship
1 month internship - 4 weekly tasks<br>
# 🤖 HarshBot — Rule-Based AI Chatbot

A Python-based conversational chatbot that uses **rule-based logic** (if-else + dictionary lookup) to respond to user inputs — built as part of the **DecodeLabs AI Internship**.

---

## ✨ Features

### 💬 Smart Greeting Recognition
- Responds to common greetings like `hi`, `hello`, and `hey`
- Handles casual expressions like `how r u` alongside formal ones
- Uses a **dictionary with `.get()`** for instant static response lookup

### 🧠 Dictionary-Based Response Engine
- All static replies are stored in a `responses` dictionary
- Looked up using Python's `.get()` method — clean, efficient, and beginner-friendly
- No repetitive if-else chains for simple replies

### 📅 Real-Time Date & Time
- Type `date` → Bot replies with today's date (e.g. `17 May 2026`)
- Type `time` → Bot replies with the current time (e.g. `10:45 AM`)
- Powered by Python's built-in `datetime` module

### 😄 Random Joke Generator
- Type `joke` or `tell me a joke` → Bot picks a random programming joke
- Uses Python's `random.choice()` for variety every time

### 🔢 Built-in Calculator
- Type `calculate 5 + 3` → Bot replies `The answer is 8`
- Supports `+`, `-`, `*`, `/` and more
- Wrapped in `try-except` to handle invalid expressions gracefully

### 💙 Mood Check-ins
- Detects when you say `i am sad` or `i feel happy`
- Responds with an empathetic, uplifting message

### ❓ Help Menu
- Type `help` to see a list of everything HarshBot can do
- Great for first-time users

### 🔁 Continuous Conversation Loop
- Runs continuously using a `while True` loop
- Gracefully exits when you type `bye`, `exit`, `quit`, or `goodbye`

### 🔡 Case-Insensitive Input
- Uses `.lower().strip()` on every input
- Works whether you type `HI`, `Hi`, or `hi`

### ⚠️ Unknown Input Handling
- If the bot doesn't understand, it suggests typing `help`
- Never crashes on unexpected input

---

## 🗣️ Example Conversation

```
========================================
   Welcome to HarshBot 🤖
   Type 'bye' or 'exit' to quit
========================================

You: hi
Bot: Hey there! How can I help you? 😊

You: what is today's date
Bot: Today's date is 17 May 2026.

You: calculate 15 * 4
Bot: The answer is 60

You: tell me a joke
Bot: Why did the programmer quit? Because he didn't get arrays! 😂

You: i am sad
Bot: Aww, cheer up! 😊 You're doing amazing. Keep going!

You: bye
Bot: Goodbye! Have a great day! 👋
```

---

## 🚀 How to Run

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/harshbot.git

# 2. Navigate to the project folder
cd harshbot

# 3. Run the chatbot
python chatbot.py
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3   | Core programming language |
| `datetime` | Real-time date and time responses |
| `random`   | Random joke selection |
| Dictionary | `.get()` based response lookup |
| `while` loop | Continuous conversation flow |

---

## 📁 Project Structure

```
harshbot/
│
├── chatbot.py   # Main chatbot file
└── README.md    # Project documentation
```

---

## 🧩 Concepts Used

- `input()` and `print()` for console interaction
- `while True` loop for continuous execution
- `if-elif-else` for decision making
- `dict.get()` for clean key-value lookups
- `.lower()` and `.strip()` for input normalization
- `try-except` for safe expression evaluation
- `random.choice()` for dynamic responses
- `datetime` module for live date/time

---

## 👨‍💻 Author

**Harsh Raj**
 AI Intern 