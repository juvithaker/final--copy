import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os
import subprocess

def start_game(game_folder):
    main_script = os.path.join(game_folder, "main.py")

    try:
        os.chdir(game_folder)
        subprocess.run(["python", "main.py"])  # Assumes 'python' is in the system's PATH
    except FileNotFoundError:
        messagebox.showerror("Error", f"Could not find {main_script}")

def manual_selection():
    root = tk.Tk()
    root.title("Manual Selection Menu")

    label = tk.Label(root, text="Choose a Game:")
    label.pack(pady=10)

    button_style = tk.Button(root, text="Style Game", command=lambda: start_game("DOOM-style-game"))
    button_style.pack(pady=20)

    button_car = tk.Button(root, text="Car Game", command=lambda: start_game("car-game"))
    button_car.pack(pady=20)

    button_tetris = tk.Button(root, text="Tetris", command=lambda: start_game("tetris"))
    button_tetris.pack(pady=20)

    root.mainloop()

def personalized_recommendation():
    questions = [
        "What type of game do you prefer?\na. Action-packed b. Puzzle-solving c. Simulation",
        "How competitive are you?\na. Very competitive b. Somewhat competitive c. Not competitive at all",
        "What type of music do you enjoy listening to the most?\na. Rock b. Pop c. Classical",
        "What's your favorite season of the year?\na. Spring b. Summer c. Fall"
    ]

    user_responses = []

    for question in questions:
        response = simpledialog.askstring("Question", question)
        user_responses.append(response.lower())

    recommended_game_folder = match_game(user_responses)
    messagebox.showinfo("Recommended Game", f"We recommend the {recommended_game_folder} game!")

    if recommended_game_folder:
        start_game(recommended_game_folder)

def simple_question(question):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    response = simpledialog.askstring("Question", question)
    root.destroy()  # Explicitly destroy the window

    return response

def match_game(responses):
    action_preferences = ['a', 'a', 'a', 'a']
    puzzle_preferences = ['b', 'b', 'b', 'b']
    simulation_preferences = ['c', 'c', 'c', 'c']

    if responses == action_preferences:
        return "DOOM-style-game"
    elif responses == puzzle_preferences:
        return "car-game"
    elif responses == simulation_preferences:
        return "tetris"
    else:
        # If no exact match, return a game based on the most common preference
        preference_counts = {'a': 0, 'b': 0, 'c': 0}
        for response in responses:
            preference_counts[response] += 1

        most_common_preference = max(preference_counts, key=preference_counts.get)

        if most_common_preference == 'a':
            return "DOOM-style-game"
        elif most_common_preference == 'b':
            return "car-game"
        elif most_common_preference == 'c':
            return "tetris"
    
    return None

def main_menu():
    root = tk.Tk()
    root.title("Game Menu")

    label = tk.Label(root, text="Choose an Option:")
    label.pack(pady=10)

    button_manual = tk.Button(root, text="Manually Select Games", command=manual_selection)
    button_manual.pack(pady=20)

    button_personalized = tk.Button(root, text="Personalized Recommendations", command=personalized_recommendation)
    button_personalized.pack(pady=20)

    button_quit = tk.Button(root, text="Quit", command=root.destroy)
    button_quit.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
