import pygame
import sys
import random


# Pygame Initialization
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
FONT = pygame.font.SysFont('Comic Sans MS', 32)  # Playful font for a kids' game
QUESTION_FONT = pygame.font.SysFont('Comic Sans MS', 20)  # Smaller playful font for the question

# Game States
START_SCREEN = 1
QUESTION_SCREEN = 2
GAME_OVER = 3

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Treasure Hunt Game')

# Function to load images safely (using .jpg instead of .png)
def load_image(image_path, scale=(SCREEN_WIDTH, SCREEN_HEIGHT)):
    try:
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, scale)
        return image
    except pygame.error as e:
        print(f"Error loading image {image_path}: {e}")
        return None

# Load background (treasure box), fish, and speech bubble
background_image = load_image('images/treasure_box.jpg')
open_box_image = load_image('images/open_box.jpg')
fish_image = load_image('images/fish.jpg', scale=(400, 400))
bubble_image = load_image('images/speech_bubble.png', scale=(300, 150))  # Adjust bubble scale if needed

if not background_image or not fish_image or not bubble_image:
    print("Error: One or more images failed to load!")
    pygame.quit()
    sys.exit()

# Questions and Answers
questions = [
     {
        "question": "Which of the following will you use to create a tuple?",
        "options": ["{}", "()", "[]", "<>"],
        "answer": "()"
    },
     
     {
        "question": "Which function is used to convert a string into an integer?",
        "options": ["str()", "int()", "float()", "char()"],
        "answer": "int()"
    },
     {
        'question': 'What does len([1, 2, 3]) return?',
        'options': [
            'a) 3',
            'b) [1, 2, 3]',
            'c) Error',
            'd) None'
        ],
        'answer': 'a) 3'
    },
    {
        "question": "Which of the following is used to create a list?",
        "options": ["{}", "[]", "()","<>"],
        "answer": "[]"
    },
     {
        'question': 'Which of the following creates a new set in Python?',
        'options': [
            'a) x = {}',
            'b) x = []',
            'c) x = set()',
            'd) x = ()'
        ],
        "answer": "c) x = set()"

     }
]

current_question = 0
score = 0

# Function to wrap text within a given width
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0
    for word in words:
        word_width, _ = font.size(word + ' ')
        if current_width + word_width <= max_width:
            current_line.append(word)
            current_width += word_width
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
    lines.append(' '.join(current_line))
    return lines

# Fish class to simulate fish swimming
class Fish:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.image = fish_image
        self.bubble_image = bubble_image  # Add the speech bubble image to the Fish class
        self.speed = 4  # Increased speed to reduce lag
        self.reached_center = False
        
    def draw(self):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        if self.reached_center:
            bubble_x = self.x - self.bubble_image.get_width() - 20  # Position bubble to the left of the fish
            bubble_y = self.y - self.bubble_image.get_height() // 2 - 30  # Position bubble slightly higher
            screen.blit(self.bubble_image, (bubble_x, bubble_y))
            wrapped_text = wrap_text(self.text, QUESTION_FONT, self.bubble_image.get_width() - 20)  # Wrap text to fit the bubble
            text_y = bubble_y + 30  # Adjust starting Y position of text
            for line in wrapped_text:
                question_text = QUESTION_FONT.render(line, True, BLACK)
                text_rect = question_text.get_rect(midtop=(bubble_x + self.bubble_image.get_width() // 2, text_y))
                screen.blit(question_text, text_rect)
                text_y += QUESTION_FONT.get_height() + 5  # Add small padding between lines

    def move(self):
        target_x = SCREEN_WIDTH - self.image.get_width()  # Position fish on the right side
        if not self.reached_center:
            if self.x < target_x:
                self.x += self.speed
            elif self.x > target_x:
                self.x -= self.speed
            else:
                self.x = target_x
                self.reached_center = True

    def display_feedback(self, feedback_text):
        feedback_rendered_text = FONT.render(feedback_text, True, BLACK)
        feedback_rect = feedback_rendered_text.get_rect(center=(self.x + self.image.get_width() // 2, self.y - 40))
        feedback_background_rect = feedback_rect.inflate(20, 20)
        pygame.draw.rect(screen, WHITE, feedback_background_rect, border_radius=15)  # Rounded edges
        screen.blit(feedback_rendered_text, feedback_rect)
        pygame.display.update()


# Button class
class Button:
    def __init__(self, x, y, text, action=None, color=BLUE):
        self.x = x
        self.y = y
        self.width = 150  # Adjusted width for the options
        self.height = 50
        self.text = text
        self.action = action
        self.color = color  # Button color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), border_radius=10)  # Ensure the background color covers the whole button
        label = FONT.render(self.text, True, WHITE)
        surface.blit(label, (self.x + (self.width - label.get_width()) // 2, self.y + (self.height - label.get_height()) // 2))

    def is_clicked(self, pos):
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


# Display the question and options
def display_question():
    global current_question
    question = questions[current_question]
    question_text = question['question']

    # Create fish for the question
    fish = Fish(0, SCREEN_HEIGHT // 2 - fish_image.get_height() // 2, question_text)
    fishes.clear()
    fishes.append(fish)

    # Create buttons for answer options with different colors
    buttons.clear()
    options = question['options']
    colors = [BLUE, RED, GREEN, YELLOW]  # Colors for buttons
    y_position = SCREEN_HEIGHT - 70
    total_width = len(options) * 150 + (len(options) - 1) * 30  # Total width of buttons plus spacing
    x_start_position = (SCREEN_WIDTH - total_width) // 2  # Centering buttons

    for i, option in enumerate(options):
        button = Button(x_start_position + i * 180, y_position, option, action=lambda opt=option: check_answer(opt), color=colors[i])
        buttons.append(button)

def check_answer(selected_option):
    global current_question
    global score
    global feedback_text  # Add a global variable to hold the feedback text

    question = questions[current_question]
    if selected_option == question['answer']:
        score += 1
        feedback_text = "Correct!"
    else:
        feedback_text = "Wrong!"

    # Display feedback above the fish
    fishes[0].display_feedback(feedback_text)

    # Move to the next question after a short delay
    pygame.time.delay(2000)  # Delay for 2 seconds
    current_question += 1
    if current_question >= len(questions):
        game_loop(GAME_OVER)
    else:
        display_question()


# Start Screen
def start_game():
    global current_question
    global fishes
    current_question = 0
    fishes.clear()


    # Start Button
    start_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 'Start', action=start_game, color=GREEN)
    buttons.append(start_button)

    screen.fill(WHITE)
    if background_image:
        screen.blit(background_image, (0, 0))
    start_button.draw(screen)
    pygame.display.update()

# Game Over screen
def game_over():
    global score
    screen.fill(WHITE)
    
    # Check if the player has a perfect score
    if score == len(questions):
        if open_box_image:
            screen.blit(open_box_image, (0, 0))
        congrats_text = FONT.render("Congrats! You got the treasure!", True, BLACK)
        congrats_rect = congrats_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
        congrats_background_rect = congrats_rect.inflate(10, 10)
        pygame.draw.rect(screen, WHITE, congrats_background_rect, border_radius=15)  # Rounded edges
        screen.blit(congrats_text, congrats_rect)
    else:
        if background_image:
            screen.blit(background_image, (0, 0))
        game_over_text = FONT.render(f"Game Over! Your final score: {score}", True, BLACK)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
        game_over_background_rect = game_over_rect.inflate(20, 20)
        pygame.draw.rect(screen, WHITE, game_over_background_rect, border_radius=15)  # Rounded edges
        screen.blit(game_over_text, game_over_rect)

    pygame.display.update()



# Game loop
def game_loop(game_state):
    global current_question
    global score
    global fishes
    global buttons

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game_state == START_SCREEN:
                    for button in buttons:
                        if button.is_clicked(pos):
                            game_state = QUESTION_SCREEN
                            display_question()
                elif game_state == QUESTION_SCREEN:
                    for button in buttons:
                        if button.is_clicked(pos):
                            button.action()
                elif game_state == GAME_OVER:
                    running = False

        if game_state == START_SCREEN:
            start_game()
        elif game_state == QUESTION_SCREEN:
            screen.fill(WHITE)
            if background_image:
                screen.blit(background_image, (0, 0))
            for fish in fishes:
                fish.move()
                fish.draw()
            for button in buttons:
                button.draw(screen)
            pygame.display.update()
        elif game_state == GAME_OVER:
            game_over()
        
        pygame.display.update()


# Initialize buttons and fishes
buttons = []
fishes = []

# Start the game
game_loop(START_SCREEN)

# Quit Pygame
pygame.quit()
sys.exit()
