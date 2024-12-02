import pygame
import random
import sys
import asyncio

pygame.init()


WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dragon Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


try:
    dragon_frames = [
        pygame.image.load('dragon1.png'),
        pygame.image.load('dragon2.png'),
        pygame.image.load('dragon3.png'),
        pygame.image.load('dragon4.png'),
        pygame.image.load('dragon5.png'),
        pygame.image.load('dragon6.png')
    ]
    dragon_frames = [pygame.transform.scale(frame, (60, 50)) for frame in dragon_frames]
    obstacle_image = pygame.image.load('obstacle.png')
    obstacle_image = pygame.transform.scale(obstacle_image, (20, 50))
    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Error loading assets: {e}")
    sys.exit()


DRAGON_WIDTH, DRAGON_HEIGHT = 60, 50
dragon_x, dragon_y = 50, HEIGHT // 2
dragon_speed = 5
current_frame = 0
frame_rate = 100


OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 20, 50
obstacle_speed = 5  
obstacle_frequency = 30  


clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 30)


def game_over():
    game_over_text = font.render("You are not good enough! Press R to Restart", True, RED)
    screen.blit(game_over_text, (WIDTH // 5, HEIGHT // 2))
    pygame.display.update()


def draw_dragon(x, y):
    global current_frame
    screen.blit(dragon_frames[current_frame], (x, y))


def draw_obstacles(obstacles):
    for obs in obstacles:
        screen.blit(obstacle_image, obs.topleft)

async def game_loop():
    global dragon_y, current_frame

    dragon_y = HEIGHT // 2
    obstacles = []
    score = 0
    game_running = True
    last_frame_time = pygame.time.get_ticks()
    obstacle_speed = 5  
    obstacle_frequency = 30  

    while game_running:
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return  

        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dragon_y = mouse_y - DRAGON_HEIGHT // 2
        dragon_y = max(0, min(dragon_y, HEIGHT - DRAGON_HEIGHT)) 

        
        current_time = pygame.time.get_ticks()
        if current_time - last_frame_time > frame_rate:
            current_frame = (current_frame + 1) % len(dragon_frames)
            last_frame_time = current_time

        
        if score >= 100:
            obstacle_speed = 10
            obstacle_frequency = 10
        elif score >= 50:
            obstacle_speed = 8
            obstacle_frequency = 15
        elif score >= 20:
            obstacle_speed = 7
            obstacle_frequency = 20

        
        if random.randint(1, obstacle_frequency) == 1:
            obstacle_height = random.randint(30, 100)
            obstacles.append(pygame.Rect(WIDTH, random.randint(0, HEIGHT - obstacle_height), OBSTACLE_WIDTH, obstacle_height))

        
        for obstacle in obstacles[:]:
            obstacle.x -= obstacle_speed
            if obstacle.x + OBSTACLE_WIDTH < 0:
                obstacles.remove(obstacle)
                score += 1

        
        for obstacle in obstacles:
            if obstacle.colliderect(pygame.Rect(dragon_x, dragon_y, DRAGON_WIDTH, DRAGON_HEIGHT)):
                game_over()
                await asyncio.sleep(2)  
                return 

     
        draw_dragon(dragon_x, dragon_y)
        draw_obstacles(obstacles)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        pygame.display.update()

      
        clock.tick(60)
        await asyncio.sleep(0)  


async def main():
    while True:
        await game_loop()


if __name__ == "__main__":
    asyncio.run(main())
