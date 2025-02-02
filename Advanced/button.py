import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria",30)

class Button():
    def __init__(self, x_pos, y_pos, text_input):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        self.width = self.text_rect.width + 40  
        self.height = self.text_rect.height + 20
        self.rect = pygame.Rect(
            self.text_rect.left - 20, self.text_rect.top - 10, self.width, self.height
        )

    def update(self, screen):
        pygame.draw.rect(screen, "black", self.rect, border_radius=15, width=3)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.text_rect.collidepoint(position):
            print(f"Button '{self.text_input}' Pressed!")
            return True
        return False

    def changeColor(self, position):
        if self.text_rect.collidepoint(position):
            self.text = main_font.render(self.text_input, True, "dark grey")
        else:
            self.text = main_font.render(self.text_input, True, "black")

# buttonA = Button(400, 300, "Puzzle A")
# buttonB = Button(400, 300, "Puzzle B")
# buttonC = Button(400, 300, "Puzzle C")
