import ctypes, pygame, sys
from options import Options

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((1680, 1050), pygame.RESIZABLE)
        pygame.display.set_caption('CGR Slot Machine')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(r'Sprite\BG_Cleos_Gold.png').convert_alpha()
        self.bg_image2 = pygame.image.load('Sprite\Cleos_BG.png').convert_alpha()
        self.bg_image3 = pygame.image.load(r'Sprite\frame.png').convert_alpha()
        self.delta_time = 0
        self.aspect_ratio = 1600 / 900
        self.options_menu = Options()

        self.click_sound = pygame.mixer.Sound('Audio\Click (Click_Standard_02).wav')

        # Sound
        main_sound = pygame.mixer.Sound('Audio\Mysteries of Ancient Egypt.mp3')
        # main_sound.play(loops = -1)
    
    def get_font(self, size):
        return pygame.font.Font('Font\Hieroglike.otf', size)
    
    def get_font2(self, size):
        return pygame.font.Font('Font\ThroneOfEgypt-Regular.ttf', size)

    def options(self):

        self.start_time = pygame.time.get_ticks()
        running = True

        while running:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                        exit(0)

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            # Update and draw option menu elements
            self.screen.fill((0, 0, 0))
            self.draw_options()

            pygame.display.update()
            self.clock.tick(120)

    def draw_options(self):
        # Calculate scaled dimensions for background image based on aspect ratio
        bg_width = int(self.screen.get_height() * self.aspect_ratio)
        bg_height = self.screen.get_height()
        scaled_bg_image = pygame.transform.scale(self.bg_image, (bg_width, bg_height))
    
        # Calculate centering offsets for background image
        bg_offset_x = (self.screen.get_width() - bg_width) // 2
        bg_offset_y = 0  # Align to the top
    
        # Blit scaled background image
        self.screen.blit(scaled_bg_image, (bg_offset_x, bg_offset_y))
        self.screen.blit(self.bg_image2, (0, 0))
    
        # Draw other game elements at their original size
        # Update and draw machine elements (you'll need to implement this)
        self.options_menu.update(self.delta_time)


if __name__ == '__main__':
    game = Game()
    game.options()
