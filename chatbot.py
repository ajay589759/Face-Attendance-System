import csv
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk
from googlesearch import search


class Chatbot:
    def __init__(self, csv_file):
        self.questions = []
        self.answers = []
        try:
            with open(csv_file, "r", encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:  # Ensure there are at least two columns
                        self.questions.append(row[0].strip().lower())  # Convert questions to lowercase
                        self.answers.append(row[1].strip())
        except FileNotFoundError:
            print(f"Error: The file {csv_file} was not found.")
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")

    def answer_question(self, question):
        question = question.lower().strip()
        for i, csv_question in enumerate(self.questions):
            csv_words = set(csv_question.split())
            user_words = set(question.split())
            if csv_words & user_words:  # Check if there's any common word
                return self.answers[i]
        return None


def google_search(query, num_results=1):
    try:
        search_results = list(search(query, stop=num_results))
        return search_results
    except Exception as e:
        print(f"An error occurred during Google search: {e}")
        return []


def get_google_search_result(query):
    search_results = google_search(query, num_results=1)
    if search_results:
        return search_results[0]  # Return the first search result URL
    else:
        return "I couldn't find any relevant information for your query."


def chatbot_response(chatbot, user_input):
    if user_input.lower() == 'exit':
        return "Goodbye!"
    else:
        csv_response = chatbot.answer_question(user_input)
        if csv_response:
            return csv_response
        else:
            response = get_google_search_result(user_input)
            return response


def send_message():
    user_input = user_input_entry.get()
    if not user_input.strip():
        return

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\n")

    response = chatbot_response(chatbot, user_input)
    chat_history.insert(tk.END, f"Bot: {response}\n\n")

    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)  # Scroll to the end
    user_input_entry.delete(0, tk.END)  # Clear input field


# Create the main application window
root = tk.Tk()
root.title("Chatbot Interface")

# Load background image
bg_image = Image.open(r"C:\Users\ajays\PycharmProjects\chatbot\chatbotimage.jpg")
bg_image = bg_image.resize((600, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0)

# Create a scrolled text area for chat history
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg='white')
chat_history.place(x=20, y=20, width=560, height=300)

# Entry widget for user input
user_input_entry = tk.Entry(root, width=50)
user_input_entry.place(x=20, y=340)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.place(x=500, y=337)

chatbot = Chatbot("chat_bot.csv")  # Initialize the chatbot

root.geometry("600x400")  # Set the size of the window
root.mainloop()
