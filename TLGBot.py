import telebot

bot = telebot.TeleBot('936648651:AAGRqcs_gqzqsEb9M-545UaX0L643_wkcQg')
lessons = {
    "411": {
        "Понеділок": 'Фізика/nФізика/nАлгебра/nАлгебра/nУкраїнська література/nУкраїнська література/nБіологія',
        "Вівторок": 'Геометрія/nГеометрія/nБіологія/nІсторія/nУкраїнська мова/nУкраїнська мова/nІсторія/nФізкультура',
        "Середа": 'Англійська мова/nАнглійська мова/nФізика/nФізика/nАлгебра/nАлгебра/nІсторія/nКреслення/Додому',
        "Четвер": 'Хімія/nПочаткова військова підготовка/nАлгебра/nАлгебра/nФізика/nФізика/nДодому/Хімія',
        "П'ятниця": 'Географія/nРосійська/nІнформатика/nГеометрія/nФізкультура/nФізкультура/nЗарубіжна література',
    },
    "412": {
        "Понеділок": 'Алгебра/nАлгебра/nФізика/nФізика/nУкраїнська література/nУкраїнська література/nБіологія',
        "Вівторок": 'Англійська мова/nАнглійська мова/nБіологія/nІсторія/nГеометрія/nГеометрія/nІсторія/nФізкультура',
        "Середа": 'Українська мова/nУкраїнська мова/nАлгебра/nАлгебра/nФізика/nФізика/nІсторія',
        "Четвер": 'Хімія/nПочаткова військова підготовка/nФізика/nФізика/nАлгебра/nАлгебра/nКреслення/Хімія',
        "П'ятниця": 'Географія/nРосійська мова/nГеометрія/nІнформатика/nФізкультура/nФізкультура/nЗарубіжна література',
    },
}


@bot.message_handler(commands=['start'])
def starting_user(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Я готов подсказать ваше расписание. Пожалуйста, выберите '
                                      'необходимый вам класс из ниже предложенных.')


@bot.message_handler(type=['text'])
def lessonses(message, group, day):
    if lessons.get(group) in message.text and lessons.get(day) in message.text:
        bot.send_message(message.chat.id, 'abcdefghij')
    else:
        bot.send_message(message.chat.id, 'POMILKA')


bot.polling()
#lessons.get(group=a, day=b)
#Четвер
