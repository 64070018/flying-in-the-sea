"""PSIT PROJECT 2021"""
import pygame
def main():
    """flying-in-the-sea"""
    pygame.init()

    """ตัวแปรต่าง ๆ"""
    screen = pygame.display.set_mode((480*2, 360*2))
    bg = pygame.image.load(r'project\img\bg.jpg')
    bg = pygame.transform.scale(bg, (480*2, 360*2))
    pygame.display.set_caption("flying-in-the-sea")
    x, y = 0, 0

    while True:
        """การทำงาน"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        """การแสดงผลวัตถุในหน้าจอ"""
        x = x - 0.5
        if x <= -480*2:
            x = 0

        screen.blit(bg, (x-480*2, 0))
        screen.blit(bg, (x, 0))
        screen.blit(bg, (x+480*2, 0))
        pygame.display.update()
main()
