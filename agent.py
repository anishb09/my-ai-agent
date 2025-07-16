# /my_ai_agent/agent.py
import datetime
import random
import re

class Agent:
    """A more functional AI agent that can perform several tasks."""

    def __init__(self, name="Assistant"):
        """Initializes the agent."""
        self.name = name
        self.user_name = None

    # --- Core Agent Loop ---

    def listen(self):
        """Gets input from the user."""
        return input("You: ")

    def think(self, user_input):
        """Processes the user input and decides on an action."""
        user_input_lower = user_input.lower()

        # The order of these checks matters. More specific phrases should come first.
        if "my name is" in user_input_lower:
            return self._set_name(user_input_lower)
        elif "what is my name" in user_input_lower:
            return self._get_name()
        elif "what time is it" in user_input_lower:
            return self._get_time()
        elif "what is the date" in user_input_lower or "what's the date" in user_input_lower:
            return self._get_date()
        elif "tell me a joke" in user_input_lower or "say a joke" in user_input_lower:
            return self._tell_joke()
        elif "calculate" in user_input_lower or "compute" in user_input_lower:
            return self._calculate(user_input_lower)
        elif any(greeting in user_input_lower for greeting in ["hello", "hi", "hey"]):
            return f"Hello there! I am {self.name}. How can I help you?"
        elif any(exit_word in user_input_lower for exit_word in ["bye", "exit", "quit"]):
            return "goodbye"  # Special signal to exit the loop
        
        return self._handle_unknown()

    def speak(self, response):
        """Prints the agent's response."""
        print(f"{self.name}: {response}")

    def start(self):
        """Starts the main interaction loop of the agent."""
        self.speak(f"Hello! I am {self.name}. Type 'bye' or 'exit' to quit.")
        
        while True:
            user_input = self.listen()
            response = self.think(user_input)
            
            if response == "goodbye":
                self.speak("Goodbye! Have a great day.")
                break
            
            self.speak(response)

    # --- Agent Skills ---

    def _set_name(self, user_input):
        """Extracts and stores the user's name."""
        name_token = user_input.split("my name is")[-1].strip()
        if not name_token:
            return "It sounds like you were about to tell me your name, but I didn't catch it."
        self.user_name = name_token.capitalize()
        return f"Nice to meet you, {self.user_name}!"

    def _get_name(self):
        """Retrieves the stored user's name."""
        if self.user_name:
            return f"Your name is {self.user_name}."
        else:
            return "I don't know your name yet. You can tell me by saying 'my name is [your name]'."

    def _get_time(self):
        """Gets the current time."""
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    def _get_date(self):
        """Gets the current date."""
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."

    def _tell_joke(self):
        """Tells a random joke from a predefined list."""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "What do you call a fake noodle? An Impasta!",
        ]
        return random.choice(jokes)

    def _calculate(self, user_input):
        """
        Performs a simple calculation from the user input.
        Example: 'calculate 5 * 10'
        """
        # Find a simple mathematical expression in the input string
        match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', user_input)

        if not match:
            return "I can't find a calculation to perform. Please ask like this: 'calculate 5 + 3'."

        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "I can't divide by zero!"
            result = num1 / num2
        else:
            return "I can only handle addition, subtraction, multiplication, and division."
        
        return f"The result of {num1} {operator} {num2} is {result}."

    def _handle_unknown(self):
        return "I'm sorry, I don't understand. I can tell time/date, do calculations, or tell a joke."

if __name__ == "__main__":
    my_agent = Agent(name="Gemini")
    my_agent.start()
