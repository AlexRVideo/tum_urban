def send_email(message, recipient, *, sender="immersive.theatr@yandex.ru"):
    if ("@" not in sender or not sender.endswith(".com") and not sender.endswith(".ru") and not sender.endswith(".net")) \
            or ("@" not in recipient or not recipient.endswith(".com") and not recipient.endswith(
        ".ru") and not recipient.endswith(".net")):
        print(message, f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == recipient:
        print(message, f"Нельзя отправить письмо самому себе!")

    elif sender == "immersive.theatr@yandex.ru":
        print(message, f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    else:
        print(message, f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для получение письма.', 'moskomariykalyk@gmail.com')
send_email('Вы видите это сообщение, так как это напоминание!', 'immersive.theatr.fan@mail.ru', sender='immersive.theatr@gmail.com')
send_email('Пожалуйста, срочно свяжитесь для получения подарка.', 'moskomariykalyk@mail.ru', sender='immersive.theatr@mail.co')
send_email('Напоминание самому себе.', 'immersive.theatr@mail.ru', sender='immersive.theatr@mail.ru')