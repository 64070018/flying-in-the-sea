"""PSIT PROJECT 2021"""
import pygame, random, os
from pygame import mixer

pygame.init()
pygame.display.set_caption('flying-in-the-sea game')
# icon = pygame.image.load(r'Art\icongame.png') #icon game
# pygame.display.set_icon(icon)
screen_height = 360*2
screen_width = 430*2
screen = pygame.display.set_mode((screen_width, screen_height))

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        highpoint = int(file.read())
else:
        highpoint = 0

def main():
    """flying-in-the-sea"""
    pygame.mixer.music.load(r'Art\music.wav') # Music
    pygame.mixer.music.play()
    global points
    points = 0

    bg = pygame.image.load(r'Art\bg.jpg')  # Background
    bg = pygame.transform.scale(bg, (480*2, 360*2))

    player = pygame.image.load(r'Art\Turtle.png')  # Player turtled
    player = pygame.transform.scale(player, (100, 100))

    shark = pygame.image.load(r'Art\Shark.png')  # barrier shark
    shark = pygame.transform.scale(shark, (200, 100))

    boat = pygame.image.load(r'Art\Boat.png')  # barrier boatdw
    boat = pygame.transform.scale(boat, (250, 150))

    coral = pygame.image.load(r'Art\coral.png')  # barrier coral
    coral = pygame.transform.scale(coral, (250, 150))

    bg_x = 0
    shark_x, shark_y = 800, 300
    boat_x = 1000
    coral_x = 700

    distance = 0
    speed = 0

    player_x, player_y = 100, 370*2
    death_count = 0

    run = True
    while run:
        """การทำงาน"""
        distance += 1
        if distance % 900 == 0:
            speed += 1
        if speed >= 10:
            speed -= random.randint(5, 10)
        if distance%100 == 0:
            points += 1

        font = pygame.font.SysFont("Mali", 32, False, False)
        txt = font.render("SCORE:" + str(points), False, [0, 0, 0])
        high_score = font.render("High score: " + str(highpoint), True, (0, 0, 0))
        scoreRect2 = high_score.get_rect()
        scoreRect2 = (700, 10)

        for event in pygame.event.get():
           if event.type == pygame.QUIT:  # ออกจากเกม
               run = False

        action = pygame.key.get_pressed()  # การเคลื่อนที่
        if action[pygame.K_UP] or action[pygame.K_w]:
            player_y -= 1
        if action[pygame.K_DOWN] or action[pygame.K_s]:
            player_y += 1
        if action[pygame.K_LEFT] or action[pygame.K_a]:
            player_x -= 1
        if action[pygame.K_RIGHT] or action[pygame.K_d]:
            player_x += 1

        """การแสดงผลวัตถุในหน้าจอ"""
        playerr = screen.blit(player, (player_x, player_y))
        bg_x = bg_x - 0.5
        if bg_x <= -480*2:  # พื้นหลังเลื่อน
            bg_x = 0

        barrior_shark = screen.blit(shark, (shark_x, shark_y))
        if speed < 1:  # ฉลามเคลื่อนที่
            shark_x -= 1
        else:
            shark_x -= speed
        if shark_x <= -480*2:
            num = [800, 850, 900, 950, 1200]
            shark_x = random.choice(num)

        barrior_boat = screen.blit(shark, (boat_x, 0))
        if speed < 1:  # เรือเคลื่อนที่
            boat_x -= 1
        else:
            boat_x -= speed
        if boat_x <= -550*2:
            num = [860, 870, 900,930, 950, 1200]
            boat_x = random.choice(num)

        barrior_coral = screen.blit(coral, (coral_x, 280*2))
        if speed < 1:  # ปะการังเคลื่อนที่
            coral_x -= 1
        else:
            coral_x -= speed
        if coral_x <= -550*2:
            num = [860, 870, 900, 920]
            coral_x = random.choice(num)

        if player_y >= 310*2:  # ล็อคไม่ให้ตัววละครหลุดเฟรมบน-ล่าง
            player_y = 310*2
        elif player_y <= 0:
            player_y = 0
        elif player_x <= 0:
            player_x = 0

        # ถ้าชนแล้วจบเกม
        if playerr.colliderect(barrior_shark):
            pygame.mixer.music.load(r'Art\explosion.wav') #effect
            pygame.mixer.music.play()
            death_count += 1
            menu(death_count)
            return
        if playerr.colliderect(barrior_boat):
            pygame.mixer.music.load(r'Art\explosion.wav') #effect
            pygame.mixer.music.play()
            death_count += 1
            menu(death_count)
            return
        if playerr.colliderect(barrior_coral):
            pygame.mixer.music.load(r'Art\explosion.wav') #effect
            pygame.mixer.music.play()
            death_count += 1
            menu(death_count)
            return

        # การเรียนใช้ตัวแปรให้แสดงผล
        screen.blit(bg, (bg_x-480*2, 0))
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x+480*2, 0))
        screen.blit(shark, (shark_x, shark_y))
        screen.blit(boat, (boat_x, 0))
        screen.blit(coral, (coral_x, 280*2))
        screen.blit(player, (player_x, player_y))
        screen.blit(txt, (10, 10))
        screen.blit(high_score, scoreRect2)

        pygame.display.update()
    pygame.quit()

    return highpoint

def menu(death_count):
    """menu"""
    global points, highpoint
    run = True
    while run:
        screen.fill((122, 197, 205))
        font = pygame.font.SysFont('constantia', 40)

        #เมนูเริ่มเกม
        if death_count == 0:
            name = font.render("F l y i n g - i n - t h e - s e a", True, (0, 0, 0))
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            nameRect = name.get_rect()
            nameRect.center = (screen_width // 2, screen_height//2 - 50)
            screen.blit(name, nameRect)
        #เมนู restart
        elif death_count > 0:
            if points > highpoint:
                highpoint = points
                with open('score.txt', 'w') as file:
                    file.write(str(highpoint))
            else:
                highpoint = highpoint
                with open('score.txt', 'w') as file:
                    file.write(str(highpoint))
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (screen_width // 2, screen_height//2 - 50)
            screen.blit(score, scoreRect)

            high_score = font.render("High score: " + str(highpoint), True, (0, 0, 0))
            scoreRect2 = high_score.get_rect()
            scoreRect2.center = (screen_width // 2, screen_height//2 + 25)
            screen.blit(high_score, scoreRect2)

        textRect = text.get_rect()
        textRect.center = (screen_width // 2, screen_height//2 + 100)
        screen.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
                return
menu(death_count=0)
