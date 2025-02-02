import asyncio
import pygame
from button import Button
from draggable_line import DraggableLine
from drop_box import DropBox
import random
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("UNSCRAMBLE THE CODE")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

codeA_answer = [
    "def fibonacci(n):",
    "   if n == 1 or n == 2:",
    "       return 1",
    "   else:",
    "       return fibonacci(n - 1) + fibonacci(n - 2)",
    "print(fibonacci(7))"
]

def codeA():
    pygame.display.set_caption("UNSCRAMBLE PUZZLE A")
    running = True

    scrambled_lines = codeA_answer.copy()
    random.shuffle(scrambled_lines)

    lines = [DraggableLine(line, 100 + i * 80) for i, line in enumerate(scrambled_lines)]

    boxes = [DropBox("", 100 + i * 80) for i in range(len(scrambled_lines))]

    while running:
        screen.fill(WHITE) 

        font = pygame.font.SysFont(None, 30)
        text = font.render("Put each line of code in the correct order!", True, BLACK)
        text_rect = text.get_rect(center=(400, 50))
        screen.blit(text, text_rect)

        for line in lines:
            line.update(screen)

        for box in boxes:
            box.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for line in lines:
                    if line.check_for_click(mouse_pos):
                        line.dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                for line in lines:
                    line.stop_drag()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for line in lines:
                    line.drag(mouse_pos)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Press ESC to return to menu

        pygame.display.update()

codeB_answer = [
    "def to_string(n, base):",
    "    conver_tString = \"0123456789ABCDEF\"",
    "    if n < base:",
    "       return conver_tString[n]",
    "   else:"
    "       return to_string(n // base, base) + conver_tString[n %\ base]",
    "print(to_string(2835, 16))"
]

def codeB():
    pygame.display.set_caption("UNSCRAMBLE PUZZLE B")
    running = True

    scrambled_lines = codeB_answer.copy()
    random.shuffle(scrambled_lines)

    lines = [DraggableLine(line, 100 + i * 80) for i, line in enumerate(scrambled_lines)]

    boxes = [DropBox("", 100 + i * 80) for i in range(len(scrambled_lines))]

    while running:
        screen.fill(WHITE) 

        font = pygame.font.SysFont(None, 30)
        text = font.render("Put each line of code in the correct order!", True, BLACK)
        text_rect = text.get_rect(center=(400, 50))
        screen.blit(text, text_rect)

        for line in lines:
            line.update(screen)

        for box in boxes:
            box.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for line in lines:
                    if line.check_for_click(mouse_pos):
                        line.dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                for line in lines:
                    line.stop_drag()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for line in lines:
                    line.drag(mouse_pos)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Press ESC to return to menu

        pygame.display.update()

codeC_answer = [
    "def list_sum(num_List):",
    "   if len(num_List) == 1:",
    "       return num_List[0]",
    "   else:",
    "       return num_List[0] + list_sum(num_List[1:])",
    "print(list_sum([2, 4, 5, 6, 7]))"
]

def codeC():
    pygame.display.set_caption("UNSCRAMBLE PUZZLE C")
    running = True

    scrambled_lines = codeC_answer.copy()
    random.shuffle(scrambled_lines)

    lines = [DraggableLine(line, 100 + i * 80) for i, line in enumerate(scrambled_lines)]

    boxes = [DropBox("", 100 + i * 80) for i in range(len(scrambled_lines))]

    while running:
        screen.fill(WHITE) 

        font = pygame.font.SysFont(None, 30)
        text = font.render("Put each line of code in the correct order!", True, BLACK)
        text_rect = text.get_rect(center=(400, 50))
        screen.blit(text, text_rect)

        for line in lines:
            line.update(screen)

        for box in boxes:
            box.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for line in lines:
                    if line.check_for_click(mouse_pos):
                        line.dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                for line in lines:
                    line.stop_drag()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for line in lines:
                    line.drag(mouse_pos)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Press ESC to return to menu

        pygame.display.update()

async def main():
    while True:
        screen.fill(WHITE)
        menu_mouse_position = pygame.mouse.get_pos()

        # Create buttons
        puzzle_A = Button(400, 250, "Puzzle A")
        puzzle_B = Button(400, 350, "Puzzle B")
        puzzle_C = Button(400, 450, "Puzzle C")

        for button in [puzzle_A, puzzle_B, puzzle_C]:
            button.changeColor(menu_mouse_position)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if puzzle_A.checkForInput(menu_mouse_position):  
                    codeA()  
                if puzzle_B.checkForInput(menu_mouse_position):
                    codeB()  
                if puzzle_C.checkForInput(menu_mouse_position):
                    codeC()  
        
        pygame.display.update()
        await asyncio.sleep(0)

asyncio.run(main())
