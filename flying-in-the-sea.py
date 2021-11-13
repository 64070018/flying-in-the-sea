"""PSIT PROJECT 2021"""
import pygame
import random
def main():
    """flying-in-the-sea"""
    pygame.init()
    """ตัวแปรต่าง ๆ"""
    screen = pygame.display.set_mode((480*2, 360*2))
    bg = pygame.image.load(r'C:\Users\chanakarn\Desktop\รวม\it64\PSIT2021\project\img\bg.jpg') #Background
    bg = pygame.transform.scale(bg, (480*2, 360*2))
    pygame.display.set_caption("flying-in-the-sea")
    player = pygame.image.load(r'C:\Users\chanakarn\Desktop\รวม\it64\PSIT2021\project\img\Turtle.png') #Player turtle
    player = pygame.transform.scale(player, (100, 100))
    shark = pygame.image.load(r'C:\Users\chanakarn\Desktop\รวม\it64\PSIT2021\project\img\Shark.png') #Character shark
    shark = pygame.transform.scale(shark, (100, 100))
    boat = pygame.image.load(r'C:\Users\chanakarn\Desktop\รวม\it64\PSIT2021\project\img\Boat.png') #Object boat
    boat = pygame.transform.scale(boat, (250,250))
    bg_x = 0
    shark_x = 480
    boat_x = 550

    player_x, player_y = 500, 370*2

    while True:
        """หน้าหลัก"""



        """การทำงาน"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        action = pygame.key.get_pressed()
        if action[pygame.K_UP or pygame.K_w]: player_y -= 1
        if action[pygame.K_DOWN or pygame.K_s]: player_y += 1
        # if action[pygame.K_LEFT]: player_x -= 1
        # if action[pygame.K_RIGHT]: player_x += 1


        """การแสดงผลวัตถุในหน้าจอ"""
        playerr = screen.blit(player, (player_x, player_y))
        bg_x = bg_x - 0.5
        if bg_x <= -480*2:
            bg_x = 0

        barrior_shark = screen.blit(shark, (shark_x, 0))
        shark_x -= 1
        if shark_x <= -480*2:
            shark_x = 480*2

        boat_x -= 1
        if boat_x <= -550*2:
            boat_x = 550*2

        if player_y >= 285*2:
            player_y = 285*2
        elif player_y <= 0:
            player_y = 0

        if playerr.colliderect(barrior_shark):
            return
        screen.blit(bg, (bg_x-480*2, 0))
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x+480*2, 0))
        screen.blit(shark, (shark_x, 0))
        screen.blit(boat, (boat_x, 0))
        screen.blit(player, (100, player_y))
        pygame.display.update()
main()
