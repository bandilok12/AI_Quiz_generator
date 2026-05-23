from datetime import datetime

def save_score(username, score, percentage, difficulty):
    with open("scores.txt", "a") as file:
        file.write(
            f"{datetime.now()} | "
            f"User: {username} | "
            f"Difficulty: {difficulty} | "
            f"Score: {score} | "
            f"Percentage: {percentage:.2f}%\n"
        )