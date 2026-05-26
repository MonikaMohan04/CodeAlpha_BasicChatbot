# 🤖 CodeAlpha_BasicChatbot


---

## 📌 Project Description

**CodeAlpha_BasicChatbot** is a simple yet polished conversational chatbot that runs entirely in the terminal. It uses a rule-based approach: the bot matches the user's message against a dictionary of predefined patterns and replies with one of several handcrafted responses.

No external libraries, no APIs, no machine learning — just clean Python logic that demonstrates core programming concepts such as functions, loops, conditionals, string manipulation, and randomness.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🗣️ Natural Conversation | Greetings, well-being, identity, jokes, farewells and more |
| 🎲 Varied Replies | Multiple responses per pattern — picked randomly to avoid repetition |
| 🔍 Flexible Matching | Both exact and keyword/partial matching so typos are forgiven |
| ⏱️ Typing Delay | Small pause before each reply for a more human feel |
| 🎨 Styled UI | Banner, dividers, and emoji-enhanced output in the terminal |
| 🛡️ Graceful Exit | Handles empty input, `Ctrl+C`, and farewell keywords cleanly |
| 📅 Live Date & Time | Responds with the actual current time / date when asked |

---

## 💬 Supported Inputs (examples)

```
hello / hi / hey
how are you
what is your name / who are you / who made you
what can you do
tell me a joke / joke
i am sad / i am bored / i am fine
you are great / you are cool
what is python
what time is it / what is today
thank you / thanks
bye / goodbye / see you
```

_(The bot also handles partial matches, so "tell me a joke please" works too.)_

---

## 🗂️ Folder Structure

```
CodeAlpha_BasicChatbot/
│
├── main.py            # Complete chatbot source code
├── README.md          # Project documentation (this file)
└── requirements.txt   # No external dependencies needed
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| `random` (stdlib) | Pick varied responses from a list |
| `time` (stdlib) | Typing delay + live date/time |

> ✅ No third-party packages required — works out of the box with any Python 3 installation.

---

## 🚀 How to Run

### Prerequisites
- Python **3.6 or higher** installed  
  Check with: `python --version` or `python3 --version`

### Steps

```bash
# 1. Clone or download the project
git clone https://github.com/your-username/CodeAlpha_BasicChatbot.git

# 2. Navigate into the folder
cd CodeAlpha_BasicChatbot

# 3. Run the chatbot
python main.py
```

> On some systems, use `python3 main.py` instead of `python main.py`.

---

## 🖥️ Sample Output

```
  ╔══════════════════════════════════════════════════╗
  ║          Welcome to  BasicChatbot                ║
  ║              Powered by Python 🐍                ║
  ║      Type 'bye' anytime to end the chat          ║
  ╚══════════════════════════════════════════════════╝

  🤖 CodeBot : Hello! I'm CodeBot. How can I help you today? 😊

  ────────────────────────────────────────────────
  👤 You       : hello

  🤖 CodeBot : Hey there! Great to see you!

  ────────────────────────────────────────────────
  👤 You       : how are you

  🤖 CodeBot : Feeling fantastic! I'm just a bot, but a happy one! 🤖

  ────────────────────────────────────────────────
  👤 You       : tell me a joke

  🤖 CodeBot : Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂

  ────────────────────────────────────────────────
  👤 You       : what is your name

  🤖 CodeBot : My name is CodeBot! 🤖 Built with ❤️ for CodeAlpha.

  ────────────────────────────────────────────────
  👤 You       : bye

  🤖 CodeBot : Goodbye! 👋 It was great chatting with you!

  ✅  Thanks for chatting! Session ended.
```

---

## 🧠 Key Python Concepts Demonstrated

- **Functions** — `get_response()`, `print_with_delay()`, `print_banner()`, etc.
- **Loops** — `while True` loop that keeps the chatbot running
- **if-elif / in conditions** — Pattern matching logic
- **Dictionaries** — Storing response patterns as key-value pairs
- **Lists & `random.choice()`** — Multiple reply options per pattern
- **String methods** — `.lower()`, `.strip()`, `in` keyword
- **`time` module** — Delays and live date/time formatting
- **Exception Handling** — `try/except` for `KeyboardInterrupt`

---

## 👩‍💻 Author

Monika M

---

## 📄 License

This project is open-source and free to use for educational purposes.
