# AI Quiz Generator

## Project Description
AI Quiz Generator is a Python-based terminal application that generates quiz questions automatically using the Groq AI API. The system supports user registration, login authentication, difficulty levels, score calculation, and score storage.

---

## Features
- User Registration & Login
- Password Encryption using bcrypt
- AI Generated Quiz Questions
- Difficulty Levels (Easy, Medium, Hard)
- Multiple Choice Questions
- Input Validation
- Random Question Order
- Score Calculation
- Percentage Calculation
- Save Scores in Text File
- Secure API Key Management

---

## Technologies Used
- Python
- Groq API
- JSON
- bcrypt
- dotenv
- Regular Expressions
- File Handling

---

## Project Structure

AI_QUIZ_GENERATOR/
│
├── data/
│   └── users.json
│
├── .env
├── .gitignore
├── ai_questions.py
├── app.py
├── auth.py
├── save_score.py
├── scores.txt
├── requirements.txt
└── README.md

---

## Installation

### Step 1: Clone Repository

git clone <repository_url>

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Add Groq API Key

Create a `.env` file:

GROQ_API_KEY=your_api_key_here

### Step 4: Run Application

python app.py

---

## Password Rules
1. First character must be uppercase
2. Must contain special character
3. Must end with numbers

Example:
Password@123

---

## Sample Features
- AI-generated Python quiz questions
- Automatic score calculation
- Secure login system
- Quiz result storage

---

## Future Enhancements
- GUI version using Tkinter or Flask
- Database integration
- Leaderboard system
- Timer-based quiz
- Certificate generation
- Web deployment

---

## Author
Lokesh Bandi