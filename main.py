import pygame
import assets


class Main:

    @staticmethod
    def main():
        print("Hello")
        assets.Assets.load()

        pygame.init()

        screen_size = (454, 504)
        screen = pygame.display.set_mode(screen_size)
        screen.blit(assets.Assets.BACKGROUND_IMAGE, (0, 0))

        pygame.display.set_caption("TIC TAC TOE GAME")

        clock = pygame.time.Clock()

        running = True

        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)


if __name__ == "__main__":
    Main.main()
