import pygame
import sys
import os
import subprocess

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Menu")

# Set up colors
background_color = (30, 30, 30)
text_color = (255, 255, 255)
button_color = (50, 50, 50)
button_hover_color = (70, 70, 70)

# Set up fonts
font = pygame.font.Font(None, 36)

# Define game folders
game_folders = {
    "Style Game": "DOOM-style-game",
    "Car Game": "car-game",
    "Tetris": "tetris-game"
}

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        screen.fill(background_color)

        draw_text("Choose a game:", font, text_color, screen_width // 2, 50)

        button_width, button_height = 200, 50
        button_margin = 20

        selected_game = None  # Variable to store the selected game

        for i, (game_name, game_folder) in enumerate(game_folders.items()):
            button_x = (screen_width - button_width) // 2
            button_y = 200 + i * (button_height + button_margin)

            pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
            draw_text(game_name, font, text_color, button_x + button_width // 2, button_y + button_height // 2)

            # Check for button click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                if pygame.mouse.get_pressed()[0]:
                    selected_game = game_folder
                    break  # Exit the loop when a button is clicked

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        pygame.time.Clock().tick(30)

        # Return the selected game outside the loop
        if selected_game is not None:
            return selected_game

def ask_user_preference():
    is_hover_manual = False
    is_hover_questions = False

    while True:
        screen.fill(background_color)

        draw_text("Welcome to the Game Recommender!", font, text_color, screen_width // 2, 50)
        draw_text("How would you like to pick a game?", font, text_color, screen_width // 2, 150)

        button_width, button_height = 300, 50
        button_margin = 20

        # Draw buttons for user choice
        button_x = (screen_width - button_width) // 2
        button_y_manual = 200
        button_y_questions = button_y_manual + button_height + button_margin

        # Check for button hover
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hover_manual = button_x < mouse_x < button_x + button_width and button_y_manual < mouse_y < button_y_manual + button_height
        is_hover_questions = button_x < mouse_x < button_x + button_width and button_y_questions < mouse_y < button_y_questions + button_height

        pygame.draw.rect(screen, button_hover_color if is_hover_manual else button_color, (button_x, button_y_manual, button_width, button_height))
        draw_text("Pick a game manually", font, text_color, button_x + button_width // 2, button_y_manual + button_height // 2)

        pygame.draw.rect(screen, button_hover_color if is_hover_questions else button_color, (button_x, button_y_questions, button_width, button_height))
        draw_text("Answer personalized questions", font, text_color, button_x + button_width // 2, button_y_questions + button_height // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_hover_manual:
                    return "manual"
                elif is_hover_questions:
                    return "questions"
                else:
                    print("Invalid choice. Please enter 1 or 2.")

        pygame.display.flip()
        pygame.time.Clock().tick(30)

def ask_questions_for_game():
    responses = []

    while True:
        screen.fill(background_color)

        draw_text("Answer the following questions to get personalized game recommendations:", font, text_color, screen_width // 2, 50)

        # Display questions
        questions = [
            "What type of game do you prefer?\n(a) Action-packed (b) Puzzle-solving (c) Simulation",
            "How competitive are you?\n(a) Very competitive (b) Somewhat competitive (c) Not competitive at all",
            "What type of music do you enjoy listening to the most?\n(a) Rock (b) Pop (c) Classical",
            "What's your favorite season of the year?\n(a) Spring (b) Summer (c) Fall"
        ]

        question_y = 150
        for i, question in enumerate(questions):
            draw_text(question, font, text_color, screen_width // 2, question_y + i * 50)

        # Back button
        button_width, button_height = 100, 40
        button_x, button_y = 20, screen_height - button_height - 20

        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hover_back = button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height
        pygame.draw.rect(screen, button_hover_color if is_hover_back else button_color, (button_x, button_y, button_width, button_height))
        draw_text("Back", font, text_color, button_x + button_width // 2, button_y + button_height // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_hover_back:
                    return "back"
            elif event.type == pygame.KEYDOWN:
                # Capture key events to get user responses
                if event.key in [pygame.K_a, pygame.K_b, pygame.K_c]:
                    response = chr(event.key)
                    responses.append(response)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

def recommend_game_based_on_personality(responses):
    # Example: Simple recommendation logic
    action_preferences = ['a', 'a', 'a', 'a']
    puzzle_preferences = ['b', 'b', 'b', 'b']
    simulation_preferences = ['c', 'c', 'c', 'c']

    if responses == action_preferences:
        return "DOOM-style-game"
    elif responses == puzzle_preferences:
        return "car-game"
    elif responses == simulation_preferences:
        return "tetris-game"
    else:
        preference_counts = {'a': 0, 'b': 0, 'c': 0}
        for response in responses:
            preference_counts[response] += 1

        most_common_preference = max(preference_counts, key=preference_counts.get)

        if most_common_preference == 'a':
            return "DOOM-style-game"
        elif most_common_preference == 'b':
            return "car-game"
        elif most_common_preference == 'c':
            return "tetris-game"
        
def questions_page():
    responses = []

    while True:
        screen.fill(background_color)

        draw_text("Answer the following questions to get personalized game recommendations:", font, text_color, screen_width // 2, 50)

        # Display questions with numbered options
        questions = [
            "1. What type of game do you prefer?\n   (a) Action-packed   (b) Puzzle-solving   (c) Simulation",
            "2. How competitive are you?\n   (a) Very competitive   (b) Somewhat competitive   (c) Not competitive at all",
            "3. What type of music do you enjoy listening to the most?\n   (a) Rock   (b) Pop   (c) Classical",
            "4. What's your favorite season of the year?\n   (a) Spring   (b) Summer   (c) Fall",
            "5. What's your ideal vacation destination?\n   (a) Beach resort with lots of water activities   (b) Historic city with museums and cultural experiences   (c) Quiet countryside or nature retreat",
            "6. What art style do you envision for your game?\n   (a) Realistic and detailed graphics   (b) Cartoonish or stylized visuals   (c) Minimalistic and abstract design",
            "7. Which additional feature would you like in the car game?\n   (a) Racing against AI opponents   (b) Puzzle-solving challenges   (c) Free-roaming exploration",
            "8. How challenging do you want the car game to be?\n   (a) Very challenging with complex obstacles   (b) Moderately challenging with a mix of difficulty   (c) Casual and easygoing"
        ]

        question_y = 150
        spacing = 70  # Adjust this value for spacing

        for i, question in enumerate(questions):
            draw_text(question, font, text_color, screen_width // 2, question_y + i * spacing)

        # Back button
        button_width, button_height = 100, 40
        button_x, button_y = 20, screen_height - button_height - 20

        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hover_back = button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height
        pygame.draw.rect(screen, button_hover_color if is_hover_back else button_color, (button_x, button_y, button_width, button_height))
        draw_text("Back", font, text_color, button_x + button_width // 2, button_y + button_height // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_hover_back:
                    return "back"
            elif event.type == pygame.KEYDOWN:
                # Capture key events to get user responses
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8]:
                    response = chr(event.key)
                    responses.append(response)

        pygame.display.flip()
        pygame.time.Clock().tick(30)




if __name__ == "__main__":
    choice = ask_user_preference()

    if choice == "manual":
        selected_game = main_menu()
    elif choice == "questions":
        response = questions_page()
        if response == "back":
            selected_game = main_menu()
        else:
            user_responses = ask_questions_for_game()
            selected_game = recommend_game_based_on_personality(user_responses)
    else:
        print("Invalid choice. Exiting.")
        pygame.quit()
        sys.exit()

    # Launch the selected game
    main_script = os.path.join(selected_game, "main.py")
    try:
        os.chdir(selected_game)
        subprocess.run(["python", "main.py"], check=True)  # Use check=True to raise an error if the process fails
    except FileNotFoundError:
        print(f"Error: Could not find {main_script}")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to launch {main_script}")

    pygame.quit()
    sys.exit()
