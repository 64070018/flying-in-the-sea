"""PSIT PROJECT 2021"""
import pygame
import random
pygame.init()


def main():
    """flying-in-the-sea"""
    screen_height = 360*2
    screen_width = 480*2
    screen = pygame.display.set_mode((screen_width, screen_height))

    bg = pygame.image.load(r'project\img\bg.jpg')  # Background
    bg = pygame.transform.scale(bg, (480*2, 360*2))

    player = pygame.image.load(r'project\img\Turtle.png')  # Player turtle
    player = pygame.transform.scale(player, (100, 100))

    shark = pygame.image.load(r'project\img\Shark.png')  # Character shark
    shark = pygame.transform.scale(shark, (200, 100))

    boat = pygame.image.load(r'project\img\Boat.png')  # Object boat
    boat = pygame.transform.scale(boat, (250, 150))

    coral = pygame.image.load(r'project\img\coral.png')
    coral = pygame.transform.scale(coral, (250, 150))

    font = pygame.font.Font('freesansbold.ttf', 20)

    pygame.display.set_caption("flying-in-the-sea")
    bg_x = 0
    shark_x = 800
    boat_x = 1000
    coral_x = 700

    distance = 0
    points = 0

    player_x, player_y = 100, 370*2

    run = True
    while run:
        """การทำงาน"""
        distance += 1
        if distance % 900 == 0:
            points += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        action = pygame.key.get_pressed()
        if action[pygame.K_UP or pygame.K_w]:
            player_y -= 1
        if action[pygame.K_DOWN or pygame.K_s]:
            player_y += 1
        if action[pygame.K_LEFT]:
            player_x -= 1
        if action[pygame.K_RIGHT]:
            player_x += 1

        """การแสดงผลวัตถุในหน้าจอ"""
        playerr = screen.blit(player, (player_x, player_y))
        bg_x = bg_x - 0.5
        if bg_x <= -480*2:
            bg_x = 0

        barrior_shark = screen.blit(shark, (shark_x, 200))
        if points < 1:
            shark_x -= 1
        else:
            shark_x -= points
        if shark_x <= -480*2:
            shark_x = random.randint(800, 1200)

        barrior_boat = screen.blit(shark, (boat_x, 0))
        if points < 1:
            boat_x -= 1
        else:
            boat_x -= points
        if boat_x <= -550*2:
            boat_x = random.randint(1000, 500*3.5)

        if points < 1:
            coral_x -= 1
        else:
            coral_x -= points
        if coral_x <= -550*2:
            coral_x = random.randint(950, 1150)

        barrior_coral = screen.blit(coral, (coral_x, 280*2))
        if player_y >= 310*2:
            player_y = 310*2
        elif player_y <= 0:
            player_y = 0

        if playerr.colliderect(barrior_shark):
            return
        if playerr.colliderect(barrior_boat):
            return
        if playerr.colliderect(barrior_coral):
            return
        screen.blit(bg, (bg_x-480*2, 0))
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x+480*2, 0))
        screen.blit(shark, (shark_x, 200))
        screen.blit(boat, (boat_x, 0))
        screen.blit(coral, (coral_x, 280*2))
        screen.blit(player, (player_x, player_y))
        pygame.display.update()
    pygame.quit()


main()
