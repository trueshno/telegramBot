from datetime import time

import telebot
from telebot import types
from requests import get
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6112762444:AAGIBFCKzj4ktLQnB0QJ3R2cMufYkkP0KvM')

@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Наши соцсети')
    btn2 = types.KeyboardButton('Специальности')
    btn3 = types.KeyboardButton('Часто задаваемые вопросы')
    btn4 = types.KeyboardButton('Проходные баллы')
    markup.add(btn1, btn2, btn3, btn4)
    first_mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, first_mess, parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def content(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "наши соцсети":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетите наш сайт", url="http://bru.by/"))
        markup.add(types.InlineKeyboardButton("Посетите наш TikTok", url="https://www.tiktok.com/@iefbru?_t=8c2lAB9mfNW&_r=1"))
        markup.add(types.InlineKeyboardButton("Посетите наш Instagram", url="https://www.instagram.com/ief_bru/?igshid=YmMyMTA2M2Y%3D"))
        markup.add(types.InlineKeyboardButton("Посетите наш Telegram", url="https://t.me/iefbru"))

        final_message = "Следи за нами в соцсетях"

    elif get_message_bot == "проходные баллы":
        doc = open('ball_2022_1.pdf', 'rb')
        markup = types.InlineKeyboardMarkup()
        bot.send_document(message.chat.id, doc)
        final_message = "В файле предоставлена актуальная информация о проходных баллах"

    elif get_message_bot == "специальности":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Инноватика')
        btn2 = types.KeyboardButton('Зарубежное регионоведение')
        btn3 = types.KeyboardButton('Программная инженерия')
        btn4 = types.KeyboardButton('Информатика и вычислительная техника')
        btn5 = types.KeyboardButton('Прикладная механика')
        next = types.KeyboardButton('Далее')
        menu = types.KeyboardButton('Главное меню')

        markup.add(btn1, btn2, btn3, btn4, btn5, next, menu)
        final_message = "Выбери специальность, чтобы узнать немного больше о ней:"

    elif get_message_bot == "инноватика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Инноватика - это область знаний, теория и практика организации процессов превращения научно-технических достижений, открытий и изобретений в новые конкурентные технологии, товары и услуги. \nВ современных условиях формирования в стране инновационной экономики востребованы специалисты, обладающие глубокими знаниями в области техники и экономики, нестандартным мышлением, способные к системному анализу ситуаций, умеющие решать сложные научно-технические задачи, создавать высокотехнологичные производства, управлять инновационными проектами. \nПодготовка специалистов направлена на глубокое изучение экономики, менеджмента, современных промышленных технологий, новейших методов математического анализа и компьютерных информационных технологий."

    elif get_message_bot == "зарубежное регионоведение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Подготовка бакалавров основывается на изучении целого комплекса социогуманитарных и коммуникативно-языковых дисциплин. К профильным дисциплинам социогуманитарного цикла относятся такие, как история России, история стран Западной и Восточной Европы, основы политической науки и политические системы европейских стран, основы международного и конституционного права, теория и история внешней политики России и стран европейского региона, теория и история международных отношений и др. Во время обучения студенты изучают такие коммуникативно-языковые дисциплины, как практический курс по иностранному языку (английский, немецкий), основы теории и практический курс перевода, деловая переписка на иностранных языках, риторика и искусство ведения деловых переговоров, лингвострановедение и др."

    elif get_message_bot == "программная инженерия":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Подготовка специалистов направлена на глубокое изучение языков программирования, принципов программирования, принципов и методов разработки прикладного и системного программного обеспечения.\nВ процессе обучения студенты приобретают навыки проектирования программно-информационных систем различного назначения, а также навыки работы в команде по созданию программного обеспечения."

    elif get_message_bot == "информатика и вычислительная техника":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Подготовка специалистов направлена на глубокое изучение математических методов обработки информации, языков программирования, современных сетевых технологий передачи информации. Большое внимание уделяется проектированию корпоративных баз данных."

    elif get_message_bot == "прикладная механика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Студенты получают подготовку в области:\n- технологий цифрового производства в процессе конструирования и эксплуатации промышленных систем;\n- IT технологий и языков программирования (C#, Python, SQL, Unity3D);\n- компьютерного проектирования и графического дизайна инновационной техники;\n- диагностики, сервиса и восстановления узлов машин и оборудования."

    elif get_message_bot == "далее":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn6 = types.KeyboardButton('Мехатроника и робототехника')
        btn7 = types.KeyboardButton('Биотехнические системы и технологии')
        btn8 = types.KeyboardButton('Прикладная математика')
        btn9 = types.KeyboardButton('Машиностроение')
        btn10 = types.KeyboardButton('Электроэнергетика и электротехника')
        btn11 = types.KeyboardButton('Нефтегазовое дело')
        btn12 = types.KeyboardButton('Бизнес-информатика')
        back = types.KeyboardButton('Назад')

        markup.add(btn6, btn7, btn8, btn9, btn10, btn11, btn12, back)
        final_message = "Выбери специальность, чтобы узнать немного больше о ней:"

    elif get_message_bot == "мехатроника и робототехника":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Направление объединяет две самостоятельные ранее специальности: робототехнику и мехатронику. \nМехатроника – научная сфера, занимающаяся изучением комплексных компьютерных и электротехнических компонентов, на основании которых проектируются и создаются инновационные системы и машины. \nРобототехника – научная область, нацеленная на разработку и конструирование роботов и систем, способных заменить труд человека и автоматизировать сложные технологические процессы. Студенты специальности получают фундаментальную подготовку по инженерной и компьютерной графике, теории математического управления, электронным устройствам мехатронных и робототехнических систем, деталям мехатронных модулей, микропроцессорной технике в мехатронике и робототехнике и т. д."

    elif get_message_bot == "биотехнические системы и технологии":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Основная профессиональная деятельность специалистов связана с созданием, разработкой, производством и сервисным обслуживанием медицинской техники, приборов и устройств, предназначенных для оценки и коррекции состояния человека, экологического мониторинга, а также приборов телемедицинской, фармацевтической, экологической и пищевой промышленности."

    elif get_message_bot == "прикладная математика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Подготовка бакалавров направлена на глубокое изучение математики, информационных наук и программирования.\n Классические математические дисциплины – дискретная математика, математический анализ, линейная алгебра, дифференциальные уравнения, теория вероятностей, математическая статистика, численные методы; \nПрофильные дисциплины – объектно-ориентированное программирование, практики написания программного кода, базы данных, тестирование, отладка и проектирование программного обеспечения, Web-технологии; \nДисциплины, находящиеся на стыке наук – математическое моделирование, квантовые вычисления, методы анализа больших данных, искусственный интеллект, машинное обучение, нейронные сети. \nБольшое внимание в образовательной программе уделяется изучению английского языка с любого уровня."

    elif get_message_bot == "машиностроение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Основная профессиональная деятельность связана с выполнением расчета и проектирования сварных машиностроительных конструкций в соответствии с техническими заданиями и использованием стандартных средств автоматизации проектирования, разработкой рабочей документации, проведением технико-экономического обоснования технических решений; организацией рабочих мест, их оснащением с размещением сварочного и вспомогательного оборудования, обслуживанием, проверкой технического состояния и остаточного ресурса технологического оборудования."

    elif get_message_bot == "электроэнергетика и электротехника":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Будущее автотранспортных компьютерных систем - автоматы, управляющие узлами автомобиля и автомобилем в целом без участия водителя. \nДля работы с такой техникой требуются специалисты подготовка которых проводится в университете и связана с изучением микропроцессорной техники, программирования, систем компьютерной графики, мультимедиа, методов искусственного интеллекта, технического зрения, методов и алгоритмов оптимального управления, технологии производства электронных устройств автомобилей, проектирования микропроцессорных систем управления автомобилями, технической диагностики электронных систем автомобилей, эксплуатации, ремонта и сервиса электронного и электрического оборудования автомобилей."

    elif get_message_bot == "нефтегазовое дело":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Добыча, переработка, транспортировка нефти и газа (в сферах: обеспечения выполнения работ по диагностированию, техническому обслуживанию, ремонту и эксплуатации нефтегазового оборудования; \nВыполнение работ по эксплуатации оборудования подземного хранения газа; технологического сопровождения потоков углеводородного сырья и режимов работы технологических объектов нефтегазовой отрасли;\nОбеспечение контроля и технического обслуживания линейной части магистральных газопроводов; \nВыполнение работ по эксплуатации газотранспортного оборудования; \nОбеспечение эксплуатации газораспределительных станций; организация работ по диагностике газотранспортного оборудования; \nРазработка технической и технологической документации при выполнении аварийно-восстановительных и ремонтных работ на объектах газовой отрасли; организация работ по защите от коррозии внутренних поверхностей оборудования нефтегазового комплекса; \nЭксплуатация объектов приема, хранения и отгрузки нефти и нефтепродуктов)."

    elif get_message_bot == "бизнес-информатика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu = types.KeyboardButton('Главное меню')
        markup.add(menu)
        final_message = "Бизнес-информатику как практическое направление деятельности отличает работа не только в области информационных технологий, но также в области экономических и управленческих задач. \nСпециалисты, прошедшие подготовку по данному направлению, приобретают комплексные интегрированные знания и навыки и способны разрабатывать и внедрять информационные системы в бизнес-организациях, а также принимать управленческие решения с использованием разнообразных прикладных информационных систем."

    elif get_message_bot == "назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Инноватика')
        btn2 = types.KeyboardButton('Зарубежное регионоведение')
        btn3 = types.KeyboardButton('Программная инженерия')
        btn4 = types.KeyboardButton('Информатика и вычислительная техника')
        btn5 = types.KeyboardButton('Прикладная механика')
        next = types.KeyboardButton('Далее')
        menu = types.KeyboardButton('Главное меню')

        markup.add(btn1, btn2, btn3, btn4, btn5, next, menu)
        final_message = "Выбери специальность, чтобы узнать немного больше о ней:"

    elif get_message_bot == "часто задаваемые вопросы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Какой я получу диплом?')
        btn2 = types.KeyboardButton('Предоставляется ли общежитие?')
        btn3 = types.KeyboardButton('Какой срок обучения?')
        btn4 = types.KeyboardButton('Какой размер стипендии?')
        btn5 = types.KeyboardButton('Какая стоимость обучения?')
        btn6 = types.KeyboardButton('Схема расположения корпусов')
        btn7 = types.KeyboardButton('Другой вопрос')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        final_message = "Выбери интересующий тебя вопрос:"

    elif get_message_bot == "какой я получу диплом?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Часто задаваемые вопросы')
        menu = types.KeyboardButton('Главное меню')

        markup.add(btn1, menu)
        final_message = "По окончании 4-летней программы обучения выпускникам выдается диплом государственного образца бакалавра Российской Федерации в зависимости от выбранного направления, признаваемый во многих странах."

    elif get_message_bot == "предоставляется ли общежитие?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Часто задаваемые вопросы')
        menu = types.KeyboardButton('Главное меню')

        markup.add(btn1, menu)
        final_message = "Белорусско-Российский университет располагает тремя благоустроенными общежитиями, расположенными по следующим адресам: \nобщежитие №1 – ул. Ленинская, 81; \nобщежитие №2 – ул. Космонавтов, 11; \nобщежитие №3 – ул. Ленинская, 81-а.\nМеста для заселения в общежитиях предоставляются всем иногородним студентам дневной формы обучения."

    elif get_message_bot == "какой срок обучения?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Часто задаваемые вопросы')
        menu = types.KeyboardButton('Главное меню')

        markup.add(btn1, menu)
        final_message = "С 2011 года на факультете ведется подготовка студентов по направлениям подготовки бакалавриата с 4-х летним сроком обучения."

    elif get_message_bot == "какой размер стипендии?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Часто задаваемые вопросы')
        menu = types.KeyboardButton('Главное меню')
        markup.add(btn1, menu)
        grant = open('images/grant.png', 'rb')
        bot.send_document(message.chat.id, grant)
        final_message = "Размеры стипендий для студентов, обучающихся по образовательным программам Российской Федерации (российских рублей)"

    elif get_message_bot == "какая стоимость обучения?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Часто задаваемые вопросы')
        menu = types.KeyboardButton('Главное меню')
        markup.add(btn1, menu)
        tuition_fees = open('images/tuition_fees.png', 'rb')
        final_message = 'Дополнительная информация об оплате обучения по телефону +375222713976', (bot.send_document(message.chat.id, tuition_fees))

    elif get_message_bot == "схема расположения корпусов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Часто задаваемые вопросы')
        menu = types.KeyboardButton('Главное меню')
        markup.add(btn1, menu)
        final_message = 'В настоящее время в состав Белорусско-Российский университета входят лицей, архитектурно-строительный колледж, 7 учебно-лабораторных корпуса и 4 общежития', (bot.send_document(message.chat.id, 'http://cdn.bru.by/cache/university/sheme/map_big_2019_2.jpg'))

    elif get_message_bot == "другой вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Часто задаваемые вопросы')
        menu = types.KeyboardButton('Главное меню')

        markup.add(btn1, menu)
        final_message = "Задай свой вопрос по телефону: +375(29)746-85-15"

    elif get_message_bot == "главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Наши соцсети')
        btn2 = types.KeyboardButton('Специальности')
        btn3 = types.KeyboardButton('Часто задаваемые вопросы')
        btn4 = types.KeyboardButton('Проходные баллы')

        markup.add(btn1, btn2, btn3, btn4)
        final_message = "Ты вернулся в главное меню"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Наши соцсети')
        btn2 = types.KeyboardButton('Специальности')
        btn3 = types.KeyboardButton('Часто задаваемые вопросы')
        btn4 = types.KeyboardButton('Проходные баллы')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = "Что-то не то, выбери одну из кнопок ниже:"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
