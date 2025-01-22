import pygame

class Scoreboard():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def add_points(self, points):
        self.score += points

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, "white")
        screen.blit(score_text, (10, 10))