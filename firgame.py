import pygame
pygame.init()
screen_size= [400, 400]
screen=pygame.display.set_mode(screen_size)

#background image
background=pygame.image.load('background.jpg')

#planet image
planet=pygame.image.load ("planet.png")
planet_img= pygame.transform.scale(planet, [120, 90])

#bullet image
bullet=pygame.image.load("bullet.jpg")
bullet_img= pygame.transform.scale(bullet, (60, 60))

#bullet stored area
bullet_station=pygame.image.load("bullet_station.png")
bullet_station_transparent=pygame.transform.scale(bullet_station, [200, 130])
#screen.blit(background, [0,0])

#screen.blit(p_img,[140, 50])
#p_img.set_colorkey((255, 255, 255))


font = pygame.font.SysFont(None, 36)
text = font.render('Press Space to Fire', True, (255, 255, 255))


move_direction= 'right'
planet_x=150
fired=False
bullet_y=300
score = 0

keep_alive=True
while keep_alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handle the window close event
            keep_alive = False
            
    screen.blit(background,[0,0])
    #screen.blit(p_img,[150,40])
    screen.blit(planet_img,[planet_x, 40])
    screen.blit(bullet_img,[170, bullet_y])
    screen.blit(bullet_station_transparent,[100, 290])
    screen.blit(text, [100, 200])
    score_texts = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_texts, [10, 20])

    pygame.display.update()

    keys= pygame.key.get_pressed()
    if keys[pygame.K_SPACE]==True:
        fired= True
        print('Space key pressed')
    if fired is True:
            bullet_y= bullet_y-5
            if bullet_y==50:
                fired= False
                bullet_y=300
    
    if move_direction=='right':
        planet_x= planet_x+5
        if planet_x == 290:  # Simple boundary check (400 - 110 = 290)
            move_direction = 'left'
    else: 
        planet_x= planet_x-5
        if planet_x == 0:
            move_direction='right'

    if bullet_y < 130:
        if planet_x < 170 + 60 and planet_x + 120 > 170: 
            print("Good job")
            score= score+1  # Increment score
            fired = False  # Reset bullet
            bullet_y = 300
        else:
            score= 0
            

    
    clock= pygame.time.Clock()
    clock.tick(60)