# # # # import random
# # # # player = {    
# # # # 'name': '' ,
# # # # 'armor':100,
# # # # 'hp':100,
# # # # 'attack':10,
# # # # 'money':5000,
# # # # 'inventory': [] }

# # # # enemies =  [
# # # # {'name': 'опытная ведьма',
# # # # 'hp':200,
# # # # 'attack':20},

# # # # {'name': 'молодая ведьма',
# # # # 'hp':150,
# # # # 'attack':15},

# # # # {'name':'новенькая ведьма',
# # # # 'hp':100,
# # # # 'attack':10}
# # # # ]
 
# # # # name = input('Введите имя')
# # # # player['name'] = name
# # # # print('Это было рано утром, пока все спали старик джон промышлял план нападения на ведьм, но он не знал что всё это время у них был предатель и когда он пошел к генералу самураев то на них напали ведьмы, были взрывы,летали бомбы, пострадало много народа.Из городка самурайленд прилетела подмога ты и есть один из них ты должен раз и навсегда покончить с ведьмами.Ты приехал сюда совсем молодым и без опыта,но тебе помогут старик джон который продаст тебе всё оружие со всего мира и самурай дрим который научит тебя хорошо сражаться') 

# # # # while True:
# # # #     action = input('''Выбери действие:
# # # # 1 -  В бой               
# # # # 2 - Тренировка
# # # # 3 - Магазин 
# # # # 4 - Показать твоего персонажа                                                   
# # # # ''')
# # # #     if action == '1':
# # # #         z = random.randint(1,3)
# # # #         print (z)
# # # #         if z == 1:
# # # #             if player['attack'] < enemies['attack']:
# # # #                 print('Хорошо если ты готов, то пожалуйста твой противник-опытная ведьма.')
# # # #                 print('Ведьма решила нападать первой.Она попыталась ударить тебя,но ты увернулся')
# # # #                 print('Ты нанес ей хороший удар,но ей всё равно')
# # # #                 print('Она решила использовать один секретный удар и заморозила тебя, у тебя осталось ', player['hp'] - 20 )
# # # #                 print('Как только ты разморосился ведьмы и след простыл :( ')
# # # #                 player['hp'] -= 20
# # # #             if player['attack'] > enemies['attack']:
# # # #                 print('Твой противник опытная ведьма.Бей первым!')
# # # #                 print('Удар!Ведьма не ожидала,да и ты тоже :).У ведьмы всего лишь 100хп давай')
# # # #                 enemies['hp'] -= 100
# # # #                 print('Ведьма бьёт,удар и ОГО у тебя осталось всего 50хп, соберись!')
# # # #                 player['hp'] -=50
# # # #                 print('-Ну все держись.Ты ударил ведьму несколько раз,ты конечно победил,но бои не твоё')
# # # #                 enemies['hp'] -= 100
# # # #         elif z == 2:
# # # #             if player['attack'] < enemies['attack']:
# # # #                 print('Хорошо если ты готов, то пожалуйста твой противник-молодая ведьма.')
# # # #                 print('Ведьма решила нападать первой.Она попыталась ударить тебя,но ты увернулся')
# # # #                 print('Ты нанес ей хороший удар,но ей всё равно')
# # # #                 print('Она решила использовать один секретный удар и заморозила тебя, у тебя осталось ', player['hp'] - 20 )
# # # #                 print('Как только ты разморосился ведьмы и след простыл :( ')
# # # #                 player['hp'] -= 15
# # # #             if player['attack'] > enemies['attack']:
# # # #                 print('Твой противник молодая ведьма.Бей первым!')
# # # #                 print('Удар!Ведьма не ожидала,да и ты тоже :).У ведьмы всего лишь 100хп давай')
# # # #                 enemies['hp'] -= 100
# # # #                 print('Ведьма бьёт,удар и ОГО у тебя осталось всего 50хп, соберись!')
# # # #                 player['hp'] -=50
# # # #                 print('-Ну все держись.Ты ударил ведьму несколько раз,ты конечно победил,но бои не твоё')
# # # #                 enemies['hp'] -= 100
# # # #         elif z == 3:
# # # #             if player['attack'] < enemies['attack']:
# # # #                 print('Хорошо если ты готов, то пожалуйста твой противник-новенькая ведьма.')
# # # #                 print('Ведьма решила нападать первой.Она попыталась ударить тебя,но ты увернулся')
# # # #                 print('Ты нанес ей хороший удар,но ей всё равно')
# # # #                 print('Она решила использовать один секретный удар и заморозила тебя, у тебя осталось ', player['hp'] - 20 )
# # # #                 print('Как только ты разморосился ведьмы и след простыл :( ')
# # # #                 player['hp'] -= 10
# # # #             if player['attack'] > enemies['attack']:
# # # #                 print('Твой противник новенькая ведьма.Бей первым!')
# # # #                 print('Удар!Ведьма не ожидала,да и ты тоже :).У ведьмы всего лишь 100хп давай')
# # # #                 enemies['hp'] -= 100
# # # #                 print('Ведьма бьёт,удар и ОГО у тебя осталось всего 50хп, соберись!')
# # # #                 player['hp'] -=50
# # # #                 print('-Ну все держись.Ты ударил ведьму несколько раз,ты конечно победил,но бои не твоё')
# # # #                 enemies['hp'] -= 100
# # # #     if action == '2':
# # # #             print('Вот  тут ты будешь тренироваться,это наше стрельбище.За каждые 10попаданий ты будешь получать по 1очку опыта')
# # # #             print('Ты можешь начинать - сказал тебе кто-то из толпы.Как ты попадал ты и сам не догадывался,но все очень удивились и ты тоже')
# # # #             player['attack'] += 1
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #             input('Для тренировки нажмите на пробел')
# # # #     if action == '3':
# # # #         shop = input('''Что хочешь купить?:
# # # #                 1 - Зелье силы('+50 к силе')цена:2500монет
# # # #                 2 - Зелье здоровья('можно восстановить все здоровье прямо в бою,можно использовать только на покупателя')цена:3000монет
# # # #                 3 - Меч мага('атака становится на 20ед больше')цена:2000монет
# # # # ''')
# # # #         if shop == '1':
# # # #             if player['money'] >= 2500:
# # # #                 print('Поздравляю с покупкой.Теперь ты самый сильный')
# # # #         friend = input('''Что сделаешь  с зельем?:
# # # #                     1 - отдать другу
# # # #                     2 - выпить        
# # # # ''')        
# # # #         if friend == '1':
# # # #                 print('Хорошо это  твой выбор.Ты отдал зелье другу и он остался доволен')
# # # #         if friend == '2':
# # # #                 print('Ты выпил зелье.ОГО какое оно вкусное')
# # # #                 player['attack'] += 50
# # # #         if shop == '2':
# # # #             if player['money'] >= 3000:
# # # #                 print('Поздравляю с покупкой.Только часто зелье не употребляй ')
# # # #                 player['money'] -= 3000
# # # #             if player['money'] < 3000:
# # # #                 print('Вам надо заработать монеты')
# # # #         if shop == '3':
# # # #             if player['money'] >= 2000:
# # # #                 print('Поздравляю!Этот меч теперь твой,храни его-у него большая история')
# # # #                 player['money'] -= 2000
# # # #                 player['attack'] += 20
# # # #             if player['money'] < 2000:
# # # #                 print('Вам надо заработать денег')
# # # #     if action == '4':
# # # #         print(player)
         

            

# # # # import pygame
# # # # import sys
# # # # import random
# # # # pygame.init()


# # # # sc = pygame.display.set_mode((500,500))
# # # # clock = pygame.time.Clock()
# # # # bg = (123,23,12) 
# # # # player = pygame.Rect(0,0,50,50)
# # # # player_img_orig = pygame.image.load('steve.png')
# # # # player_img = pygame.transform.scale(player_img_orig,(player.width, player.height))

# # # # enemy = pygame.Rect(50,50,50,50)
# # # # enemy_img = pygame.image.load('creeper.png')
# # # # enemy_img = pygame.transform.scale(enemy_img,(enemy.width,enemy.height))

# # # # font = pygame.font.SysFont("Arial",30)
# # # # start_text_1 = font.render('Добро пожаловать', False, (139,0,255))
# # # # start_text_2 = font.render('Нажмите пробел,чтобы начать', False, (139,0,255))

# # # # end_text_1 = font.render('Вы прошли игру!Нажми пробел', False, (139,0,255))
# # # # end_text_1 = font.render('чтобы начать заного', False, (139,0,255))


# # # # direction = 'none'


# # # game_state = 0


# # # while True:
# # #     sc.fill((255,255,255))

# # #     if game_state == 0:
# # #         for i in pygame.event.get():
# # #             if i.type == pygame.QUIT:
# # #                 sys.exit()
# # #             if i.type == pygame.KEYDOWN:
# # #                 if i.key == pygame.K_SPACE:
# # #                     game_state = 1
# # #         sc.blit(start_text_1,(20,225))
# # #         sc.blit(start_text_2,(20,255))



# # #     if game_state == 2:
# # #         for i in pygame.event.get():
# # #             if i.type == pygame.QUIT:
# # #                sys.exit()
# # #             if i.type == pygame.KEYDOWN:
# # #                 if i.key == pygame.K_SPACE:
# # #                     player.x, player.y, player.width, player.height = 400, 400, 50, 50
# # #                     enemy.x, enemy.y = 50, 50
# # #                     player_img = pygame.transform.scale(player_img_orig,(player.width, player.height))
# # #                     game_state = 1
# # #         sc.blit(end_text_1,(20,225))
# # #         sc.blit(end_text_1,(20,255))

# # #     if game_state == 1:

# # #         for i in pygame.event.get():
# # #             if i.type == pygame.QUIT:
# # #                 sys.exit()
# # #             if i.type == pygame.KEYDOWN:
# # #                 if i.key == pygame.K_LEFT:
# # #                     direction = 'left'
# # #                 if i.key == pygame.K_RIGHT:
# # #                     direction = 'right'
# # #                 if i.key == pygame.K_UP:
# # #                     direction = 'up'
# # #                 if i.key == pygame.K_DOWN:
# # #                     direction = 'down'

# # #         if direction == 'right':
# # #             player.x += 5
# # #         elif direction == 'left':
# # #             player.x -= 5
# # #         elif direction == 'up':
# # #             player.y -= 5
# # #         elif direction == 'down':
# # #             player.y += 5

# # #         if player.colliderect(enemy):
# # #             enemy.x = random.randint(0,470)
# # #             enemy.y = random.randint(0,470)
# # #             player.width += 5
# # #             player.height += 5
# # #             player_img = pygame.transform.scale(player_img_orig,(player.width, player.height))
# # #         sc.blit(player_img, player)
# # #         sc.blit(enemy_img, enemy)

# # #     pygame.display.update()
# # #     clock.tick(60)


# # # # class Rect:
# # # #     def  __init__(self,width,height):
# # # #         self.width = width
# # # #         self.height = height
         
# # # #     def get_area(self):
# # # #         return self.width * self.height
    
# # # #     def get_perimeter(self):
# # # #         return 2 * self.width + 2 * self.height
    

# # # # rect = Rect(10,10)
# # # # print(rect.get_area())

# # # # class Car:
# # # #     def __init__(self,model,speed,colour,price,mileage):
# # # #         self.model = model
# # # #         self.speed = speed
# # # #         self.colour = colour
# # # #         self.price = price
# # # #         self.meleage = mileage
        
# # # #     def discont(self):
# # # #         discount = self.mileage * 0.3 / 100
# # # # car1 = Car("bmw",60,"black",50000,100000)



# # # # from math import radians, sin, cos, acos


# # # # class Point:
# # # #    def __init__(self, lat, lon):
# # # #        self.lat = lat
# # # #        self.lon = lon


# # # #    def distance(self, other):
# # # #        cos_d = sin(self.lat) * sin(other.lat) + cos(self.lat) * cos(other.lat) * cos(self.lon - other.lon)
# # # #        return 6371 * acos(cos_d)
      
# # # # class City:
# # # #    def __init__(self, name, location, population):
# # # #        self.name = name
# # # #        self.location = location
# # # #        self.population = population
    

# # # #    def distance(self, distance):
# # # #        distance = self.city1(distance) - self.city2(distance)


# # # # city1 = City(55.755864, 37.617698, 'Москва', 12600000)
# # # # city2 = City(56.876349, 47.129436,"Пермь", 2000000)

# # # class item:
# # #     def __init__(self,id,name,description,price):
# # #         self.id = id
# # #         self.name = name
# # #         self.description = description
# # #         self.price = price


# # # class user:
# # #     def __init__(self,id,name,balance,basket)
# # #         self.id = id
# # #         self.name = name
# # #         self.balance = balance
# # #         self.basket = basket


# # #     def buy(balance):
# # #         buy = balance



# # # import pygame
# # # import sys
# # # from random import*

# # # pygame.init()

# # # WIDTH = 500
# # # HEIGHT = 500
# # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # clock = pygame.time.Clock()





# # # font = pygame.font.SysFont('Arial',30)
# # # start_text_1 = font.render('Добро пожаловать!',False,(225, 0, 0))
# # # start_text_2 = font.render('Нажмите пробел,чтобы начать',False,(225, 0, 0))

# # # end_text_1 = font.render("Вы прошли игру! Нажмите пробел,", False,(0,255,0))
# # # end_text_2 = font.render("чтобы начать заново", False,(0,255,0))


# # # class Sprite:
# # #     def __init__(self,x,y,w,h,img_path):
# # #         self.rect = pygame.Rect(x,y,w,h)
# # #         self.img_orig = pygame.image.load(img_path)
# # #         self.img = pygame.transform.scale(self.img_orig, (w,h))
# # #         self.direction = "none"

# # #     def move(self):
# # #         if self.direction == 'right':
# # #             self.rect.x += 5
# # #         elif self.direction == 'left':
# # #             self.rect.x -= 5
# # #         elif self.direction == 'up':
# # #             self.rect.y -= 5
# # #         elif self.direction == 'down':
# # #             self.rect.y += 5 

# # #     def draw(self):
# # #         screen.blit(self.img, self.rect)

# # # player = Sprite(400, 400, 50, 50, 'steve.png')
# # # enemy = Sprite(50 , 50, 30 , 30, 'creeper.png')

# # # skin1 = Sprite(100,225,50,50,'steve.png')
# # # skin2 = Sprite(225,225,50,50,'knight.png')
# # # skin3 = Sprite(350,225,50,50,'tomato.png')


# # # game_state = 0


# # # while True:
# # #     screen.fill((255,255,255))

# # #     if game_state == 0:
# # #         for e in pygame.event.get():
# # #             if e.type == pygame.QUIT:
# # #                 sys.exit()
# # #             if e.type == pygame.KEYDOWN:
# # #                 if e.key == pygame.K_SPACE:
# # #                     game_state = 3
# # #             if e.type == pygame.MOUSEBUTTONDOWN:
# # #                 x, y = e.pos
# # #                 if 10 <= x <= 40 and 10 <= y <= 40:
# # #                     sys.exit()
                        
                        
                  
# # #         screen.blit(start_text_1,(20,225))
# # #         screen.blit(start_text_2,(20,255))



# # #     if game_state == 2:
# # #         for i in pygame.event.get():
# # #             if i.type == pygame.QUIT:
# # #                sys.exit()
# # #             if i.type == pygame.KEYDOWN:
# # #                 if i.key == pygame.K_SPACE:
# # #                     player.x, player.y, player.width, player.height = 400, 400, 50, 50
# # #                     enemy.x, enemy.y = 50, 50
# # #                     player.img = pygame.transform.scale(player.img_orig,(player.width, player.height))
# # #                     game_state = 1
# # #         screen.blit(end_text_1,(20,225))
# # #         screen.blit(end_text_1,(20,255))
        
        
# # #     if game_state == 3:
# # #         for e in pygame.event.get():
# # #             if e.type == pygame.QUIT:
# # #                 sys.exit()
# # #             if e.type == pygame.MOUSEBUTTONDOWN:
# # #                 x, y = e.pos
# # #                 if skin2.rect.x <= x <= skin2.rect.right and skin2.rect.y <= y <= skin2.rect.bottom:
# # #                     player.img_orig = pygame.image.load('knight.png')
# # #                     player.img = pygame.transform.scale(player.img_orig, (player.rect.width,player.rect.height))
# # #                     game_state = 1
# # #                 if skin3.rect.x <= x <= skin3.rect.right and skin3.rect.y <= y <= skin3.rect.bottom:
# # #                     player.img_orig = pygame.image.load('tomato.png')
# # #                     player.img = pygame.transform.scale(player.img_orig, (player.rect.width,player.rect.height))
# # #                     game_state = 1
# # #                 if skin1.rect.x <= x <= skin1.rect.right and skin1.rect.y <= y <= skin1.rect.bottom:
# # #                     game_state = 1
# # #                 if 10 <= x <= 40 and 10  <= y <= 40:
# # #                     sys.exit()
                    
# # #         skin1.draw()
# # #         skin2.draw()
# # #         skin3.draw()           
        

# # #     if game_state == 1:
# # #         for e in pygame.event.get():
# # #             if e.type == pygame.QUIT:
# # #                 sys.exit()
# # #             if e.type == pygame.KEYDOWN:
# # #                 if e.key == pygame.K_LEFT:
# # #                     player.direction = 'left'
# # #                 if e.key == pygame.K_RIGHT:
# # #                     player.direction = 'right'
# # #                 if e.key == pygame.K_UP:
# # #                     player.direction = 'up'
# # #                 if e.key == pygame.K_DOWN:
# # #                     player.direction = 'down'

# # #     player.move()

# # #     if player.rect.colliderect(enemy.rect):
# # #             enemy.rect.x = randint(0, 470)
# # #             enemy.rect.y = randint(0, 470)
# # #             player.rect.width += 5
# # #             player.rect.height += 5 
# # #             player.img = pygame.transform.scale(
# # #                 player.img_orig, (player.rect.width, player.rect.height))
        

# # #     if player.rect.width >= 500:
# # #             game_state = 2

# # #     player.draw()
# # #     enemy.draw()
# # #     pygame.display.update()
# # #     clock.tick(60)   

# # # z = input('Имя')
# # # x = input('Пароль')



# # # nickname = input('Никнейм: ')
# # # password = input('Пароль: ')



# # # file = open('code.txt','r')

# # # users = file.read().split('\n')

# # # for user in users:
# # #     u = user.split('-')
# # #     if len(u) >= 2:
# # #         if u[0] == nickname and u[1] == password:
# # #             print('Добро пожаловать!')
# # #             break
# # #         elif u[0] == nickname and u[1] != password:
# # #             print('Неправильный пароль!')
# # #             break
# # #     else:
# # #         print('Пользователь не найден')

            


# # import pygame
# # import sys
# # import os
# # from random import randint

# # pygame.init()

# # WIDTH = 500
# # HEIGHT = 500
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # clock = pygame.time.Clock()

# # click = pygame.Rect(225, 225, 50, 50)
# # score = 0
# # seconds_left = 10
# # interations = 0

# # font = pygame.font.SysFont('Arial', 20)
# # left_second_text = font.render(str(seconds_left), False, (225, 0, 0))
# # score_text = font.render(str(score), False, (225, 0, 0))

# # nickname = input('Никнейм: ').lower()
# # prev_record = -1
# # if os.path.exists(f'{nickname}.txt'):
# #     file = open(f'{nickname}.txt', 'r')
# #     prev_record = file.read()
# #     file.close()
    
# # record_text = font.render(f'Рекорд пред: {prev_record}',False, (225,0,0))


# # while True:
# #     screen.fill((255,255,255))
# #     for e in pygame.event.get():
# #         if e.type == pygame.QUIT:
# #             sys.exit()
# #         if e.type == pygame.MOUSEBUTTONDOWN:
# #             if click.collidepoint(e.pos[0], e.pos[1]):
# #                 score += 1
# #                 score_text = font.render(str(score),False, (225,0,0))
# #                 click.x = randint(0,450)
# #                 click.y = randint(0,450)

# #     pygame.draw.rect(screen,(0,0,0), click)
# #     screen.blit(left_second_text, (10,10))
# #     screen.blit(score_text, (480,10))
# #     if prev_record != -1:
# #         screen.blit(record_text, (10, 480))
        
# #     interations += 1
# #     if interations == 60:
# #         seconds_left -= 1
# #         interations = 0
# #         left_second_text = font.render(str(seconds_left),False,(225,0,0))
        
        
# #     if seconds_left == -1:
# #         file = open(f'{nickname}.txt', 'w')
# #         file.write(str(score))
# #         file.close()
# #         sys.exit()
        
# #     pygame.display.update()
# #     clock.tick(60)



# import pygame
# import random
# import sys
# import math

# pygame.init()

# W, H = 500, 500

# screen = pygame.display.set_mode((W, H))
# clock = pygame.time.Clock()

# class Bullet:
#     def __init__(self,x,y,w,h,img_path,mouse):
#         self.rect = pygame.Rect(x,y,w,h)
#         self.img_orig = pygame.image.load(img_path)
#         self.img_orig = pygame.transform.scale(self.img_orig,(w,h))
#         self.img = pygame.transform.scale(self.img_orig,(w,h))
#         self.x_speed = 0
#         self.y_speed = 0
#         self.default_speed = 3
#         self.mouse = mouse
#         self.float_x = x
#         self.flost_y = y
#         self.set_speed(mouse)
        
        
#     def set_speed(self,to_point):
#         x_from,y_from = self.rect.centerx, self.rect.centery
        
        
#         x_to, y_to = to_point
#         dx = x_to - x_from
#         dy = y_to - y_from
#         x_speed = round(abs((self.default_speed * dx) / math.sqrt(dx**2 + dy**2)),3)
#         y_speed = round(abs((x_speed * dy) / dx), 3)
#         if x_to < x_from:
#             x_speed *= -1
#         if y_to < y_from:
#             y_speed *= -1
            
#         self.x_speed = x_speed
#         self.y_speed = y_speed
#         self.rotate_to_point(self.mouse)
        
        
        
#     def move(self):
#         self.float_x += self.x_speed
#         self.float_y += self.y_speed
#         self.rect.x = round(self.float_x)
#         self.rect_y = round(self.float_y)
        
    
#     def draw(self):
#         screen.blit(self.img,self.rect)
        
    
#     def rotate_to_point(self, mouse):
#         dx, dy = mouse[0] - self.rect.centerx, mouse[1] - self.rect.centery
#         angle = math.degrees(math.atan2(-dy, dx)) - 90
#         self.img = pygame.transform.rotate(self.img_orig, angle)
#         self.rect = self.img.get_rect(center=self.rect.center)
#         self.float_x = self.rect.x
#         self.float_y = self.rect.y
        
        
#     def collide(self,obj):
#         return self.rect.colliderect(obj.rect)

# class Wall: 
#     def __init__(self,x,y,w,h, img_path):
#         self.rect = pygame.Rect(x,y,w,h)
#         self.img = pygame.image.load(img_path)
#         self.img = pygame.transform.scale(self.img, (w, h))
        
#     def draw(self):
#         screen.blit(self.img, (self.rect.x, self.rect.y)) 
        
        
        
# class Player:
#     def __init__(self,x,y,w,h,img_path, walls):
#         self.rect = pygame.Rect(x,y,w,h)
#         self.img = pygame.image.load(img_path)
#         self.img = pygame.transform.scale(self.img,(w,h))
#         self.x_speed = 0
#         self.y_speed = 0
#         self.walls = walls  
    
#     def move(self):
#         self.rect.x += self.x_speed
#         for wall in self.walls:
#             if self.collide(wall):
#                 self.rect.x -= self.x_speed
#         self.rect.y += self.y_speed
#         for wall in self.walls:
#             if self.collide(wall):
#                 self.rect.y -= self.y_speed
                
#     def collide(self, obj):
#         return self.rect.colliderect(obj.rect) 

#     def draw(self):
#         screen.blit(self.img, (self.rect.x, self.rect.y)) 
        
        
# class Enemy:
#     def __init__(self,x,y,w,h,img_path,speed,p1,p2,orient):
#         self.rect = pygame.Rect(x,y,w,h)
#         self.img = pygame.transform.scale(pygame.image.load(img_path),(w,h))
#         self.speed = speed
#         self.p1 = p1
#         self.p2 = p2
#         self.orient = orient
        
        
#     def move(self):
#         if self.orient == 'h':
#             self.rect.x += self.speed
#             if self.rect.x >= self.p2 or self.rect.x <= self.p1:
#                 self.speed *= -1
#             else:
#                 self.rect.y += self.speed
#                 if self.rect.y >= self.p2 or self.rect.y <= self.p1:
#                     self.speed *= -1
                
#     def draw(self):
#         screen.blit(self.img, (self.rect.x, self.rect.y))
        
# lvl1walls = []
# lvl2walls = []
# lvl3walls = []

# with open('map1.txt', 'r') as map:
#     row, col = 0, 0
#     for line in map.read().split('\n'):
#         x = list(line)
#         col = 0
#         for i in x:
#             if i == '1':
#                 lvl1walls.append(Wall(col*20,row*20, 20, 20, 'wall.png'))
#             col += 1
#         row+= 1
        
# with open('map2.txt', 'r') as map:
#     row, col = 0, 0
#     for line in map.read().split('\n'):
#         x = list(line)
#         col = 0
#         for i in x:
#             if i == '1':
#                 lvl2walls.append(Wall(col*20,row*20, 20, 20, 'wall.png'))
#             col += 1
#         row+= 1
        
# with open('map3.txt', 'r') as map:
#     row, col = 0, 0
#     for line in map.read().split('\n'):
#         x = list(line)
#         col = 0
#         for i in x:
#             if i == '1':
#                 lvl3walls.append(Wall(col*20,row*20, 20, 20, 'wall.png'))
#             col += 1
#         row+= 1
        
# player = Player(30,30,30,30, 'knight.png',lvl1walls)  

# lvl1enemy = [
#     Enemy(30,80,25,25, 'creeper.png',3,30,200,'h'),
#     Enemy(420,40,25,25, 'creeper.png',5,50,400,'v')
# ]   

# lvl2enemy = []  
# lvl3enemy = []

# bullets = []


# level = 1
# while True:
#     screen.fill((255, 255,255))
    
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             sys.exit()
#         elif e.type == pygame.KEYDOWN:
#             if e.key == pygame.K_LEFT:
#                 player.x_speed = -5
#             elif e.key == pygame.K_RIGHT:
#                 player.x_speed = 5
#             elif e.key == pygame.K_UP:
#                 player.y_speed = -5
#             elif e.key == pygame.K_DOWN:
#                 player.y_speed = 5
#         elif e.type == pygame.KEYUP:
#             if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
#                 player.x_speed = 0
#             elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
#                 player.y_speed = 0
#         elif e.type == pygame.MOUSEBUTTONDOWN:
#             bullet = Bullet(player.rect.centerx, player.rect.centery,15,15, 'creeper.png', e.pos)
#             bullets.append(bullet)
                    
#     player.move()
    
#     if level == 1:
#         for enemy in lvl1enemy:
#             enemy.move()
            
#         for enemy in lvl1enemy:
#             enemy.draw()
            
#         for enemy in lvl1enemy:
#             if player.collide(enemy):
#                 player.rect.x = 30
#                 player.rect.y = 30
                
#         for wall in player.walls:
#             wall.draw()
            
#         if player.rect.x >= 500:
#             level += 1
#             player.walls = lvl2walls
#             player.rect.x = 30
#             player.rect.y = 30
        
#         for bullet in bullets:
#             if bullet.rect.x > 500 or bullet.rect.x <= -bullet.rect.width or bullet.rect.y >= 500 or bullet.rect.y <= -bullet.rect.height:
#                 bullets.remove(bullet)
#                 break
            
#     if level == 2:
#         for enemy in lvl2enemy:
#             enemy.move()
            
#         for enemy in lvl2enemy:
#             enemy.draw()
            
#         for enemy in lvl2enemy:
#             if player.collide(enemy):
#                 player.rect.x = 30
#                 player.rect.y = 30
                
#         for wall in player.walls:
#             wall.draw()
            
#         if player.rect.x >= 500:
#             level += 1
#             player.walls = lvl3walls
#             player.rect.x = 30
#             player.rect.y = 30
            
#         for bullet in bullets:
#             if bullet.rect.x > 500 or bullet.rect.x <= -bullet.rect.width or bullet.rect.y >= 500 or bullet.rect.y <= -bullet.rect.height:
#                 bullets.remove(bullet)
#                 break
            
#     if level == 3:
#         for enemy in lvl3enemy:
#             enemy.move()
            
#         for enemy in lvl3enemy:
#             flag = False
#             for bullet in bullets:
#                 if bullet.collide(enemy):
#                     bullets.remove(bullet)
#                     flag = True
#                     break 
        
#         for bullet in bullets:
#             if bullet.rect.x > 500 or bullet.rect.x <= -bullet.rect.width or bullet.rect.y >= 500 or bullet.rect.y <= -bullet.rect.height:
#                 bullets.remove(bullet)
#                 break
                
                
#     for bullet in bullets:
#             bullet.draw()
#             bullet.move()
            
            
            
        
#     player.draw()    
    
#     pygame.display.update()
#     clock.tick(60)

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 700
dis_height = 500
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Игра змейка')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def game():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("Ты проиграл!! Нажми на c-играть ещё раз или q-выход", red)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
game() 