import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def check_password(self, password: str) -> bool:
        return self.password == hash(password)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f'Пользователь {nickname} вошел в систему!')
                return
        print('Неверный логин или пароль')

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и вошел в систему!')

    def log_out(self):
        if self.current_user is not None:
            print(f'Пользователь {self.current_user.nickname} вышел из системы!')
            self.current_user = None
        else:
            print('Никто не вошел в систему!')

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, keyword: str):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title: str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while video.time_now < video.duration:
                    print(f'Смотрим: {video.title}, время: {video.time_now}s')
                    video.time_now += 1
                    time.sleep(1)  # пауза в 1 секунду
                print("Конец видео")
                video.time_now = 0  # Сброс текущего времени просмотра
                return
        print("Видео не найдено.")


class Video:
    def __init__(self, title: str, duration: int, adult_mode = False, time_now = 0 ):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __str__(self):
        return f'Video(title = {self.title}, duration = {self.duration}, adult_mode = {self.adult_mode})'



if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
