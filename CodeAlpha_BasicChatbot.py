# ============================================================
#  CodeAlpha_BasicChatbot
#  A beginner-friendly rule-based chatbot in Python
#  Author  : Monika M
#  Intern  : CodeAlpha Python Programming Internship
# ============================================================

# ── Imports ─────────────────────────────────────────────────
import time   # used for a small typing delay to feel more natural
import random # used to pick one response from several options

# ── Response Bank ────────────────────────────────────────────
# Each key is a "pattern" (lowercase keyword / phrase).
# Each value is a LIST of possible replies – the bot picks one
# at random so it doesn't feel too robotic.

RESPONSES = {
    # Greetings
    "hello": [
        "Hello! 😊 How can I help you today?",
        "Hey there! Great to see you!",
        "Hi! I'm CodeBot. Ask me anything!",
    ],
    "hi": [
        "Hi! 👋 What's on your mind?",
        "Hey! How are you doing?",
    ],
    "hey": [
        "Hey! 😄 How can I assist you?",
        "Hey hey! What's up?",
    ],

    # Well-being
    "how are you": [
        "I'm doing great, thanks for asking! 😊 How about you?",
        "Feeling fantastic! I'm just a bot, but a happy one! 🤖",
        "All systems running smoothly! How can I help?",
    ],
    "how are you doing": [
        "Pretty good! Ready to chat. 😄",
        "I'm wonderful, thank you! What can I do for you?",
    ],

    # Identity
    "what is your name": [
        "My name is CodeBot! 🤖 Built with ❤️ for CodeAlpha.",
        "I'm CodeBot, your friendly Python chatbot!",
    ],
    "what's your name": [
        "I go by CodeBot! Nice to meet you. 😊",
    ],
    "who are you": [
        "I'm CodeBot – a simple rule-based chatbot created as part of the CodeAlpha Python Internship!",
        "I'm CodeBot, here to have a conversation with you. 🤖",
    ],
    "who made you": [
        "I was built by a CodeAlpha Python intern as a learning project!",
        "A passionate Python developer made me during their CodeAlpha internship. 🐍",
    ],

    # Age
    "how old are you": [
        "I'm ageless! But if you must know, I was born the day this code was run. 😄",
        "Just a few lines of Python old! Pretty young, right?",
    ],

    # Capabilities
    "what can you do": [
        "I can chat with you, answer simple questions, and keep you company! 😊",
        "I can greet you, tell you about myself, share a joke, and more!",
    ],

    # Jokes
    "tell me a joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
        "Why was the computer cold? It left its Windows open! 💻❄️",
        "A SQL query walks into a bar, walks up to two tables and asks… 'Can I join you?' 😄",
    ],
    "joke": [
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads! 🍫😂",
        "Why do Python programmers wear glasses? Because they can't C! 😂",
    ],

    # Feelings input from user
    "i am fine": [
        "That's wonderful to hear! 😊",
        "Great! Keep smiling! 😄",
    ],
    "i am good": [
        "Awesome! Glad to hear that! 🎉",
    ],
    "i am sad": [
        "Aw, I'm sorry to hear that. 😔 Things will get better, I promise! 💪",
        "Cheer up! Here's a virtual hug 🤗",
    ],
    "i am bored": [
        "Let's fix that! Ask me for a joke, or we can just chat! 😄",
        "Boredom? Not on my watch! Ask me something fun! 🎉",
    ],

    # Compliments
    "you are great": [
        "Aww, thank you! You're pretty awesome yourself! 😊",
        "That's so kind of you! 🥰",
    ],
    "you are cool": [
        "Thanks! You're cooler! 😎",
        "I try my best! 😄",
    ],

    # Python / Programming
    "what is python": [
        "Python is a high-level, beginner-friendly programming language known for its clean syntax! 🐍",
        "Python is one of the most popular programming languages in the world – great for AI, web, and automation!",
    ],
    "do you like python": [
        "Of course! Python is literally what I'm made of! 🐍❤️",
    ],

    # Time / Date (static response since we're rule-based)
    "what time is it": [
        f"It's {time.strftime('%I:%M %p')} on my clock! ⏰",
    ],
    "what is today": [
        f"Today is {time.strftime('%A, %B %d, %Y')}. 📅",
    ],

    # Farewell
    "bye": [
        "Goodbye! 👋 It was great chatting with you!",
        "See you later! Take care! 😊",
        "Bye bye! Come back anytime! 🤖",
    ],
    "goodbye": [
        "Goodbye! Have a wonderful day! 🌟",
    ],
    "see you": [
        "See you soon! 👋",
    ],

    # Thanks
    "thank you": [
        "You're very welcome! 😊",
        "Happy to help! 🎉",
        "Anytime! That's what I'm here for. 🤖",
    ],
    "thanks": [
        "No problem at all! 😊",
        "Glad I could help! 👍",
    ],
}

# Default replies when the bot doesn't understand the input
DEFAULT_RESPONSES = [
    "Hmm, I'm not sure I understand. Could you rephrase that? 🤔",
    "I'm still learning! Could you try asking something else? 😅",
    "Sorry, I didn't quite get that. Try 'hello', 'joke', or 'bye'!",
    "Oops! That went over my head. 😄 Ask me something simpler?",
]


# ── Helper Functions ─────────────────────────────────────────

def get_response(user_input: str) -> str:
    """
    Match the user's input against known patterns and return a reply.

    Steps:
      1. Convert input to lowercase and strip extra spaces.
      2. Check if the cleaned input (or a keyword) is in RESPONSES.
      3. Return a random reply from the matching list.
      4. If nothing matches, return a random default response.
    """
    cleaned = user_input.lower().strip()

    # Direct key match first (most efficient)
    if cleaned in RESPONSES:
        return random.choice(RESPONSES[cleaned])

    # Partial / keyword match – checks if any known key
    # appears anywhere inside what the user typed
    for key in RESPONSES:
        if key in cleaned:
            return random.choice(RESPONSES[key])

    # Nothing matched
    return random.choice(DEFAULT_RESPONSES)


def print_with_delay(text: str, delay: float = 0.6) -> None:
    """
    Print the bot's response after a short pause to simulate
    a natural typing effect.
    """
    time.sleep(delay)
    print(f"\n  🤖 CodeBot : {text}\n")


def print_banner() -> None:
    """Display a welcome banner when the chatbot starts."""
    banner = """
  ╔══════════════════════════════════════════════════╗
  ║          Welcome to  BasicChatbot                ║
  ║              Powered by Python 🐍                ║
  ║      Type 'bye' anytime to end the chat          ║
  ╚══════════════════════════════════════════════════╝
    """
    print(banner)


def print_divider() -> None:
    """Print a simple visual divider between turns."""
    print("  " + "─" * 48)


# ── Main Chat Loop ───────────────────────────────────────────

def run_chatbot() -> None:
    """
    Core loop of the chatbot.
    - Keeps running until the user types 'bye' or 'goodbye'.
    - Reads user input, gets a response, and prints it.
    """
    print_banner()
    print_with_delay("Hello! I'm CodeBot. How can I help you today? 😊", delay=0.2)

    while True:
        print_divider()

        # Read input; handle Ctrl+C gracefully
        try:
            user_input = input("  👤 You       : ").strip()
        except (KeyboardInterrupt, EOFError):
            print_with_delay("Session interrupted. Goodbye! 👋")
            break

        # Skip empty input
        if not user_input:
            print_with_delay("Please type something! I'm listening. 😊")
            continue

        # Get and display the bot's reply
        reply = get_response(user_input)
        print_with_delay(reply)

        # Exit condition
        if any(word in user_input.lower() for word in ["bye", "goodbye", "see you"]):
            break   # Exit the loop – the reply has already been printed

    print("\n  ✅  Thanks for chatting! Session ended.\n")


# ── Entry Point ──────────────────────────────────────────────

if __name__ == "__main__":
    run_chatbot()
