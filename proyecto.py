import pygame
import random

class MapGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.biomes = ["Desierto", "Nieve", "Tropical"]
        self.colors = {"Desierto": (255, 255, 102), "Nieve": (255, 255, 255), "Tropical": (34, 139, 34)}
        self.map_data = self.generate_map()

    def generate_map(self):
        return [[random.choice(self.biomes) for _ in range(self.width)] for _ in range(self.height)]

    def display_map(self):
        pygame.init()
        screen_size = (self.width * 20, self.height * 20)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Mapa 2D con Biomas")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for y in range(self.height):
                for x in range(self.width):
                    pygame.draw.rect(screen, self.colors[self.map_data[y][x]], (x * 20, y * 20, 20, 20))

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    width = 40  # Puedes ajustar el tamaño del mapa cambiando estos valores
    height = 40
    map_generator = MapGenerator(width, height)
    map_generator.display_map()