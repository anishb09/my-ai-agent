# My AI Agent

A simple, extensible command-line personal assistant built with Python. This project serves as a foundational template for creating more complex, rule-based or model-driven AI agents.

## 🚀 Features

This agent is capable of handling a variety of simple tasks through a conversational command-line interface:

- **Greets the user:** Responds to hellos and other greetings.
- **Tells Time & Date:** Can provide the current system time and date.
- **Tells Jokes:** Has a small, curated collection of jokes to share.
- **Basic Calculator:** Can perform simple arithmetic operations (`+`, `-`, `*`, `/`).
- **Remembers Your Name:** Can store and recall your name for the duration of a single session.

---

## 📋 Prerequisites

Before you begin, ensure you have Python installed on your system. This project is developed with Python 3.

- Python 3.x

## ⚙️ Installation

1.  **Clone the repository (replace `your-username` with your GitHub username):**
    ```sh
    git clone https://github.com/your-username/my-ai-agent.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd my-ai-agent
    ```

## ▶️ How to Run

To start the agent, simply run the `agent.py` script from your terminal:

```sh
python agent.py
```

The agent will greet you, and you can start giving it commands. To exit the program, type `bye`, `quit`, or `exit`.

### Example Interaction

```
Gemini: Hello! I am Gemini. Type 'bye' or 'exit' to quit.
You: hi
Gemini: Hello there! I am Gemini. How can I help you?
You: my name is anish
Gemini: Nice to meet you, Anish!
You: what is the date?
Gemini: Today's date is October 27, 2023.
You: tell me a joke
Gemini: Why did the scarecrow win an award? Because he was outstanding in his field!
You: calculate 100 / 4
Gemini: The result of 100 / 4 is 25.0.
You: what is my name
Gemini: Your name is Anish.
You: bye
Gemini: Goodbye! Have a great day.
```

---

## 🛣️ Project Roadmap

This project is a starting point. Future enhancements could include:

- [ ] **Persistent Memory:** Saving user details (like name) to a file so the agent remembers them across sessions.
- [ ] **API Integration:** Connecting to external services (e.g., weather, news, Wikipedia) to provide real-world data.
- [ ] **LLM Integration:** Using a Large Language Model (like Google's Gemini) for more natural and flexible conversation handling.
- [ ] **Modular Skills:** Refactoring skills into a more dynamic, plug-and-play architecture.

Contributions are welcome! Feel free to fork the repository and submit a pull request.
