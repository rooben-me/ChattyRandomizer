import random
import csv
import datetime

def random_case(s):
    """
    Returns a new string with the characters of the input string randomly converted to uppercase or lowercase.

    Arguments:
    s -- the string to be randomized

    Returns:
    A new string with randomized upper and lower case characters.
    """
    result = ""
    for char in s:
        if random.choice([True, False]):
            result += char.upper()
        else:
            result += char.lower()
    return result

# Generate a unique conversation ID using the current date and time
conversation_id = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# Create a filename for the conversation history CSV file
conversation_file = f"conversation_history_{conversation_id}.csv"

# Initialize an empty list to store the conversation history
history = []

# Start the conversation loop
while True:
    # Get input from the user
    user_input = input("You: ")
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Check if the user has entered "quit" to end the conversation
    if user_input.lower() == "quit":
        # Write the conversation history to a CSV file
        with open(conversation_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(history)
        # Print a message to indicate that the conversation history has been saved
        print(f"Conversation history saved to {conversation_file}")
        # Exit the loop
        break
    # Generate a response from the bot
    response = random_case(user_input)
    # Add the current message and response to the conversation history
    history.append((timestamp, user_input, response))
    # Print the bot's response with the current timestamp
    print(f"Bot ({timestamp}):", response)