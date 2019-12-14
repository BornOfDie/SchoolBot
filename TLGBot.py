import telebot, lessons

lessons = {
    "411": {
        "Понеділок": [
            'Фізика',
            'Фізика',
            'Алгебра',
            'Алгебра',
            'Українська література',
            'Українська література',
            'Біологія'
        ],
        "Вівторок": [
            'Геометрія',
            'Геометрія',
            'Біологія',
            'Історія',
            'Українська мова',
            'Українська мова',
            'Історія',
            'Фізкультура'
        ],
        "Середа": [
            'Англійська мова',
            'Англійська мова',
            'Фізика',
            'Фізика',
            'Алгебра',
            'Алгебра',
            'Історія',
            'Історія'
        ],
        "Четвер": [
            'Хімія',
            'Початкова військова підготовка',
            'Алгебра',
            'Алгебра',
            'Фізика',
            'Фізика',
            'Нічого/Хімія'
        ],
        "П'ятниця": [
            'Географія',
            'Російська',
            'Інформатика',
            'Геометрія',
            'Фізкультура',
            'Фізкультура',
            'Зарубіжна література'
        ]
    }
}
bot = telebot.TeleBot(lessons.Token)
alld = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]


@bot.message_handler(type=['text'])
def get_lessons_str(message, group, day):
    group_lessons = lessons.get(group)
    if not group_lessons:
        return None

    lessons_per_day = group_lessons.get(day)
    if not lessons_per_day:
        return None

    lesson_str = f"{day}:\n"
    for lesson in lessons_per_day:
        lesson_str += f"\t{lesson}\n"
    lesson_str += "\n"

    return lesson_str
    
    if [group, day] == message.text.split():#Вот здесь проблема с реализацией, у меня что-то не так, нужна помощь
        bot.send_message(message.chat.id, get_lessons_str(group=a[1], day=a[2]))
    else:
        pass


@bot.message_handler(commands=['start'])
def starting_user(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Я готов вам подсказать ваше расписание. Пожалуйста, выберите '
                                      'необходимый вам класс из ниже предложенных.')


bot.polling()
