import random

class User:

    def __init__(self):
        self.nickname = " "
        self.password = 0
        self.age = 0
        self.adult = False

    def __hash__(self, password):
        return hash(password)

class Video:

    def __init__(self):
        self.title = ''
        self.duration = 0
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    import random
    Users = []
    Videos = []
    Videos_chousde = []



    def __init__(self):
        UrTube.Users = []
        UrTube.Videos = []
        UrTube.Videos_chousde = []
        self.currentUser = User()


    def register(self):
        new_user = User()
        new_user.nickname = input('Введите имя:')
        for i in range(len(self.Users)):
            if self.Users[i].nickname == new_user.nickname or new_user.nickname == 'None':
                new_user.nickname = input('Это имя занято. Введите новое имя:')
                i = 0
        new_user.age = int(input('Введите возраст:'))
        if (new_user.age > 17):
            new_user.adult = True
        new_user.password = input('Введите пароль:')
        new_user.password = new_user.__hash__(new_user.password)
        self.Users.append(new_user)

    def log_in(self):
        name = input('Введите имя:')
        correct_name = False
        for i in range(len(self.Users)):
            if self.Users[i].nickname == name:
                password = input('Введите пароль:')
                password = self.Users[i].__hash__(password)
                if self.Users[i].password == password:
                    self.currentUser.nickname = self.Users[i].nickname
                    self.currentUser.password = self.Users[i].password
                    self.currentUser.age = self.Users[i].age
                    self.currentUser.adult = self.Users[i].adult
                    correct_name = True
                else:
                    print('Неверный пароль')
                correct_name = True
        if correct_name == False:
            print('Неверное имя')


    def log_out(self):
        self.currentUser.nickname = 'None'
        self.currentUser.password = ' '
        self.currentUser.age = 0
        self.currentUser.adult = False

    def add_videos(self):
        video_age = 0
        age_choose = False
        new_video = Video()
        new_video.title = input('Введите название:')
        for i in range(len(self.Videos)):
            if self.Videos[i].title == new_video.title:
                new_video.title = input('Это название занято. Введите новое название:')
                i = 0
        while age_choose != True:
            try:
                video_age = int(input ('Введите есть ли возрастное ограничение Да(1)/Нет(0):'))
                if video_age == 0 or video_age == 1:
                    age_choose = True
                else:
                    print('Вы ввели не правильный символ')
            except:
                print('Вы ввели не правильный символ')
        if video_age == 1:
            new_video.adult_mode = True
        new_video.duration = random.randint(10, 20)
        self.Videos.append(new_video)


    def get_videos(self):
        self.Videos_choosde = []
        n = 0
        print (len(self.Videos))
        name = input('Введите запрос:')
        for i in range(len(self.Videos)):
            for j in range(len(self.Videos[i].title)-len(name)):
                for d in range(len(name)):
                    print (d)
                    if self.Videos[i].title[j+d] == name[d].upper() or self.Videos[i].title[j+d] == name[d].lower():
                        n += 1
            if n >= len(name):
                self.Videos_choosde.append(self.Videos[i])
                n = 0
        print ('Найдено:')
        for i in range(len(self.Videos_choosde)):
            print ('Название:', self.Videos_choosde[i].title, 'Длительность:', self.Videos_choosde[i].duration,'Возрастные ограничения:', self.Videos_choosde[i].adult_mode)

    def watch_video(self):
        for i in range(len(self.Videos_choosde)):
            print (i+1, 'Название:', self.Videos_choosde[i].title,'Длительность:', self.Videos_choosde[i].duration, 'Возрастные ограничения:', self.Videos_choosde[i].adult_mode)
        print (' ')
        print (' ')
        choose = int(input('Введите номер ролика:')) - 1
        if (self.currentUser.adult == self.Videos_choosde[choose].adult_mode or self.currentUser.adult == True):
            for i in range(self.Videos_choosde[choose].duration):
                print ('Секунда видео:', i+1)
        else:
            print ('неверная возростная категория')


UrTube_v1 = UrTube()
currentUser = User()

button = 0

#UrTube.register(UrTube_v1)
#UrTube.log_in(UrTube_v1)
#UrTube.log_out(UrTube_v1)
#UrTube.add_videos(UrTube_v1)
#UrTube.get_videos(UrTube_v1)
#UrTube.watch_video(UrTube_v1)

def menu_creator():
    print('Приветствуем вас в UrTube')
    print(' ')
    print('Меню')
    print(' ')
    print('1. Регистрация')
    print('2. Вход')
    print('3. Выход')
    print('4. Добавить видео')
    print('5. Поиск видео')
    print('6. Запуск видео')
    print('7. Закрыть приложение')
    print(' ')
    print('Сейчас залогинени', UrTube_v1.currentUser.nickname, ' Всего пользователей', len(UrTube_v1.Users), ' Всего видео', len(UrTube_v1.Videos))

while button != 7:
    menu_creator()
    try:
        button = int(input('Выбирите действие:'))
    except:
        print ('Вы ввели не правильный символ')
    if button == 1:
        UrTube.register(UrTube_v1)
    if button == 2:
        UrTube.log_in(UrTube_v1)
    if button == 3:
        if (UrTube_v1.currentUser.nickname == 'None'):
            print ('На данный момент ни кто не защел на платформу')
        else:
            UrTube.log_out(UrTube_v1)
    if button == 4:
        UrTube.add_videos(UrTube_v1)
    if button == 5:
        if (UrTube_v1.currentUser.nickname == 'None'):
            print ('Сначала пожалуйста зарегистрируйтесь и залогиньтесь')
        else:
            if (len(UrTube_v1.Videos) <= 0):
                print ('на платформе нет залитых видео')
            else:
                UrTube.get_videos(UrTube_v1)
    if button == 6:
        if (UrTube_v1.currentUser.nickname == 'None'):
            print ('Сначала пожалуйста зарегистрируйтесь и залогиньтесь')
        else:
            if (len(UrTube_v1.Videos_chousde) <= 0):
                print ('Сначала произведеите поис видео')
            else:
                UrTube.watch_video(UrTube_v1)

    #if button == 10:
    #    for i in range (len(UrTube_v1.Users)):
    #        print ('Имя: ', UrTube_v1.Users[i].nickname, 'Возраст: ', UrTube_v1.Users[i].age, 'Возрастная категория: ', UrTube_v1.Users[i].adult)
    button = 0
