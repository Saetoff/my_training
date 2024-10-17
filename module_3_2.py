def send_email(message, recipient, sender = "university.help@gmail.com"): #Сообщение, получатель, отправитель
    if '@' not in recipient or '@' not in sender:
        print(f'Не возможно отправить письмо с адреса {sender} на адресс {recipient}')
    elif not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net'):
        print(f'Не возможно отправить письмо с адреса {sender} на адресс {recipient}')
    elif not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'):
        print(f'Не возможно отправить письмо с адреса {sender} на адресс {recipient}')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


i = send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print(i)
i = send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print(i)
i = send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print(i)
i = send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print(i)