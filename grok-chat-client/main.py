import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
import requests
import json
import sqlite3
import os

# API Key handling (using keyring for security)
import keyring

API_KEY = keyring.get_password("grok-chat", "api_key")
if not API_KEY:
    # Prompt for API key if not set
    API_KEY = input("Enter your Grok API key: ")
    keyring.set_password("grok-chat", "api_key", API_KEY)

# Database setup
DB_PATH = "chat_history.db"
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            role TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_message(role, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def load_messages():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM messages ORDER BY timestamp")
    messages = cursor.fetchall()
    conn.close()
    return messages

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.messages = load_messages()  # Load previous messages
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Grok Chat Client")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # Input layout
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message...")
        self.input_field.returnPressed.connect(self.send_message)
        input_layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)

        self.setLayout(layout)

        # Load and display existing messages
        self.update_chat_display()

    def update_chat_display(self):
        self.chat_display.clear()
        for role, content in self.messages:
            prefix = "You: " if role == "user" else "Grok: "
            self.chat_display.append(f"{prefix}{content}")

    def send_message(self):
        user_message = self.input_field.text().strip()
        if not user_message:
            return

        # Add user message
        self.messages.append(("user", user_message))
        save_message("user", user_message)
        self.update_chat_display()
        self.input_field.clear()

        # Call Grok API
        self.call_grok_api(user_message)

    def call_grok_api(self, user_message):
        url = "https://api.x.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "grok-4.20",
            "messages": [{"role": "user", "content": user_message}],
            # Tools will be added later
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                grok_response = response.json()["choices"][0]["message"]["content"]
                self.messages.append(("assistant", grok_response))
                save_message("assistant", grok_response)
                self.update_chat_display()
            else:
                self.chat_display.append("Error: " + response.text)
        except Exception as e:
            self.chat_display.append(f"Error: {str(e)}")

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = ChatApp()
    window.show()
    sys.exit(app.exec_())