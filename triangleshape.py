import pygame

class triangleshape(pygame.sprite.Sprite):
    def __init__(self,points,color=None):
        if not color:
            color=(255,0,0)
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.polygon(self.image, color, points)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.velocity = 5
        self.position=self.rect.center
                                        
    
    def draw(self,screen):
        pass
    def update(self,dt):
        pass