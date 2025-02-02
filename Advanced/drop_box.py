import pygame

class DropBox():
    def __init__(self, text, y_pos):
        self.text = text
        self.y_pos = y_pos
        self.box_width = 700  # Fixed width for the drop box
        self.box_height = 70  # Fixed height for the drop box
        self.font = pygame.font.SysFont(None, 45)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))  # Text in black
        # Center the text inside the fixed box
        self.text_rect = self.text_surface.get_rect(center=(400, self.y_pos))
        self.border_padding = 10  # Padding for the border around the text
        self.border_radius = 15  # Radius for rounded corners
        self.dragging = False

    def update(self, screen):
        # Draw the rounded border (black rectangle) around the text
        box_rect = pygame.Rect(400 - self.box_width // 2, self.y_pos - self.box_height // 2, self.box_width, self.box_height)
        pygame.draw.rect(screen, (0, 0, 0), box_rect, 2, border_radius=self.border_radius)
        screen.blit(self.text_surface, self.text_rect)
