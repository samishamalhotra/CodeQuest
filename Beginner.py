import pygame
import random
import os
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CATCH THE DATA TYPES")

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
RED = (255,0,0)

# basket
basket_img = pygame.image.load("images/basket.png")  
basket_img = pygame.transform.scale(basket_img, (170, 50))  
basket_x = (screen_width/2) - (100/2)
basket_y = screen_height - 70
basket_speed = 10

# data types
data_type_images = [
    pygame.image.load(os.path.join("images/data_types", img))
    for img in os.listdir("images/data_types")
    if img.endswith((".png", ".jpg", ".jpeg"))
]
data_type_images = [pygame.transform.scale(img, (100, 50)) for img in data_type_images]
data_type_speed = 5

# random
random_images = [
    pygame.image.load(os.path.join("images/random", img))
    for img in os.listdir("images/random")
    if img.endswith((".png", ".jpg", ".jpeg"))
]
random_images = [pygame.transform.scale(img, (100, 50)) for img in random_images]
random_speed = 5

max_score = 30
score = 0
clock = pygame.time.Clock()

def draw_basket(img, x, y):
    screen.blit(img, (x, y))
def draw_data_type(img, x, y):
    screen.blit(img, (x, y))
def draw_random(img, x, y):
    screen.blit(img, (x, y))

def display_score(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

def game_over():
    font = pygame.font.SysFont(None, 40)
    message = ""
    image = None 

    if score == max_score:
        message = "BRAVO!! You know your data types :D"
        image = pygame.image.load("images/happy.png")  # Replace with the image path you want
    elif score == -max_score:
        message = "GAME OVER!! Time to re-learn your data types :("
        image = pygame.image.load("images/sad.png")  # Replace with the image path you want
    
    if image:
        image = pygame.transform.scale(image, (100, 100))  # Adjust the size of the image
    text = font.render(message, True, BLACK)
    
    screen.fill(WHITE) 
    screen.blit(text, ((screen_width // 2) - (text.get_width() // 2), screen_height // 2 - (text.get_height() // 2)))
    
    if image:
        screen.blit(image, ((screen_width // 2) - (image.get_width() // 2), screen_height // 2 + (text.get_height() // 2)))

    exit = "[ press spacebar to exit... ]"
    closing_text = font.render(exit, True, BLACK)
    screen.blit(closing_text, ((screen_width // 2) - (closing_text.get_width() // 2), screen_height // 1 - (closing_text.get_height() // 1)))

    pygame.display.update()
    pygame.time.delay(2000)

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.quit()
            sys.exit()

def game_loop():
    global score, basket_x

    # Track the last spawn time 
    last_data_spawn = pygame.time.get_ticks()
    last_random_spawn = pygame.time.get_ticks()

    data_types = []
    randoms = []

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed  

        basket_x = max(0, min(screen_width - basket_img.get_width(), basket_x))

        # Spawn a new data type every 3 seconds
        if pygame.time.get_ticks() - last_data_spawn >= 3000:
            data_types.append({
                "x": random.randint(0, screen_width - 100),
                "y": -50,
                "img": random.choice(data_type_images)
            })
            last_data_spawn = pygame.time.get_ticks()

        # Spawn a new random object every 2 seconds
        if pygame.time.get_ticks() - last_random_spawn >= 2000:
            randoms.append({
                "x": random.randint(0, screen_width - 100),
                "y": -50,
                "img": random.choice(random_images)
            })
            last_random_spawn = pygame.time.get_ticks()

        # Move and draw data types
        for obj in data_types[:]:  
            obj["y"] += data_type_speed  
            if obj["y"] > screen_height:
                data_types.remove(obj)  
            draw_data_type(obj["img"], obj["x"], obj["y"])

            # Collision detection with basket
            if (obj["y"] + obj["img"].get_height() >= basket_y and obj["y"] <= basket_y + basket_img.get_height()) and \
               (basket_x <= obj["x"] + obj["img"].get_width() and obj["x"] <= basket_x + basket_img.get_width()):
                score += 10
                data_types.remove(obj)

        # Move and draw random objects
        for obj in randoms[:]:  
            obj["y"] += random_speed  
            if obj["y"] > screen_height:
                randoms.remove(obj)
            draw_random(obj["img"], obj["x"], obj["y"])

            # Collision detection with basket
            if (obj["y"] + obj["img"].get_height() >= basket_y and obj["y"] <= basket_y + basket_img.get_height()) and \
               (basket_x <= obj["x"] + obj["img"].get_width() and obj["x"] <= basket_x + basket_img.get_width()):
                score -= 10
                randoms.remove(obj)

        # Draw basket and score
        draw_basket(basket_img, basket_x, basket_y)
        display_score(score)

        pygame.display.update()
        clock.tick(60)

        if score == max_score or score == -max_score:
            running = False

    game_over()
game_loop()

