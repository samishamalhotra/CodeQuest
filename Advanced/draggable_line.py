import pygame

class DraggableLine():
    def __init__(self, text, y_pos):
        self.text = text
        self.y_pos = y_pos
        self.font = pygame.font.SysFont(None, 25)
        self.text_surface = self.font.render(self.text, True, (0, 0, 255))  # Text in blue
        self.text_rect = self.text_surface.get_rect(center=(400, y_pos))
        self.border_padding = 10  # Padding for the border around the text
        self.border_radius = 15  # Radius for rounded corners
        self.dragging = False
        self.bg_color = (211, 211, 211)  # Background color (dark grey)

    def update(self, screen):
        # Fill the background with solid color (light grey)
        bg_rect = self.text_rect.inflate(self.border_padding * 2, self.border_padding * 2)
        pygame.draw.rect(screen, self.bg_color, bg_rect, border_radius=self.border_radius)  # Solid background color
        pygame.draw.rect(screen, (0, 0, 0), bg_rect, 2, border_radius=self.border_radius)  # Border around the box
        screen.blit(self.text_surface, self.text_rect)

    def check_for_click(self, mouse_pos):
        return self.text_rect.collidepoint(mouse_pos)

    def drag(self, mouse_pos):
        if self.dragging:
            self.text_rect.center = mouse_pos

    def stop_drag(self):
        self.dragging = False
