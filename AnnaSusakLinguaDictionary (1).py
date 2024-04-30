from tkinter import *
import tkinter as tk
import random

missedLetters = []  # пропущенные буквы
correctLetters = []  # правильные буквы
secretWord = ""  # секретное слово
letter = ""  # введенная буква
letterIsCorrect = False
level = 1
levelUpgrade = 4
letterIsCorrect = False
buttonIsClicked = False
# кол-во слов, которые нужно отгадать, чтобы пройти уровень
# допустимое кол-во ошибок на одном слове для данного уровня
isDone = False
# пройденные слова
compleatWords = ["done"]
# перевод слов 1 уровень
words1Translations = ["солнце", "возраст", "кровать", "машина", "день", "конец", "работа", "масло", "крыса"]
# перевод слов 2 уровень
words2Translations = ["книга", "хвост", "ребенок", "выход", "девочка", "золото", "дом", "шея", "снег", "обзор",
                      "прогулка", "жена", "двор", "год", "лагерь",
                      "ступня", "король", "леди", "мясо"]
# перевод слов 3 уровень
words3Translations = ["действие", "остров", "нож", "уровень", "ночь", "порядок", "вечеринка", "радио", "стол", "голос",
                      "вода", "мир", "актер", "взрослый", "ввод",
                      "сок", "смех", "модель", "роман", "медсестра", "мир"]
# перевод слов 4 уровень
words4Translations = ["булочная", "свеча", "апельсин", "карандаш", "квадрат", "окно", "шанс", "доллар", "отец",
                      "рейс на самолет", "куртка", "память", "офис", "человек",
                      "причина", "экран", "горло", "центр", "семья", "момент", "родитель", "система", "джунгли",
                      "природа", "племянник", "попугай", "патруль"]
# перевод слов 5 уровень
words5Translations = ["шарик", "библиотека", "сотня", "муж", "кухня", "машина", "сервис", "сообщение", "счет, учет",
                      "мнение", "радуга", "вопрос", "язык", "база данных",
                      "грамматика", "история", "доброта", "пальто"]
# перевод слов 6 уровень
words6Translations = ["информация", "плечо", "телефон", "государство", "отношения", "каталог, папка", "образование",
                      "установка"]

# слова для первого уровня, из 3 букв, 9 слов
words1 = ["sun", "age", "bed", "car", "day", "end", "job", "oil", "rat"]
# слова для второго уровня, из 4 букв,  19 слов
words2 = ["book", "tail", "baby", "exit", "girl", "gold", "home", "neck", "snow", "view", "walk", "wife", "yard",
          "year", "camp", "foot", "king", "lady", "meat"]
# слова для третьего уровня, из 5 букв,  21 слов
words3 = ["action", "island", "knife", "level", "night", "order", "party", "radio", "table", "voice", "water", "world",
          "actor", "adult", "input",
          "juice", "laugh", "model", "novel", "nurse", "peace"]
# слова для четвертого уровня, из 6 букв,  27 слов
words4 = ["bakery", "candle", "orange", "pencil", "square", "window", "chance", "dollar", "father", "flight", "jacket",
          "memory", "office", "person", "reason",
          "screen", "throat", "centre", "family", "moment", "parent", "system", "jungle", "nature", "nephew", "parrot",
          "patrol"]
# слова для пятого уровня, из 7-8 букв,  18 слов
words5 = ["balloon", "library", "hundred", "husband", "kitchen", "machine", "service", "message", "account", "opinion",
          "rainbow", "question", "language", "database",
          "grammar", "history", "kindness", "overcoat"]
# слова для шестого уровня, из 9-12 букв,  8 слов
words6 = ["information", "shoulder", "telephone", "government", "relationship", "directory", "education",
          "installation"]

# транскрипция слов для первого уровня,
words1tr = ["[sʌn]", "[eɪʤ]", "[bed]", "[kɑː]", "[deɪ]", "[end]", "[ʤəʊb]", "[ɔɪl]", "[ræt]"]
# транскрипция слов для второго уровня,
words2tr = ["[bʊk]", "[teɪl] ", "[ˈbeɪbɪ]", "[ˈegzɪt]", "[gɜːl] ", "[gəʊld] ", "[həʊm]", "[nek]", "[snəʊ]", "[vjuː]",
            "[wɔːk]", "[waɪf]", "[jɑːd]", "[jɪə] ", "[kæmp]",
            "[fʊt]", " [kɪŋ]", "[ˈleɪdi]", "[miːt]"]
# транскрипция слов для третьего уровня
words3tr = ["[ˈækʃn]", "[ˈaɪlənd]", "[naɪf]", "[ˈlevl]", "[naɪt]", "[ˈɔːdə(r)] ", "[ˈpɑːti]", "[ˈreɪdiəʊ]", "[ˈteɪbl]",
            "[vɔɪs]", " [ˈwɔːtə(r)]", "[wɜːld]",
            "[ˈæktə(r)]", "[ˈædʌlt]", "[ˈɪn.pʊt]", "[dʒuːs]", "[lɑːf]", "[ˈmɒdl]", "[ˈnɒvl]", "[nɜːs]", "[piːs]"]
# транскрипция слов для четвертого уровня,
words4tr = ["[ˈbeɪ.kər.i]", "[ˈkæn.dl̩]", "[ˈɒrɪnʤ] ", "[pensl]", "[skweə]", "[ˈwɪndəʊ]", "[ʧɑːns]", "[ˈdɒlə]",
            "[ˈfɑːðə]", "[flaɪt]", "[ˈʤækɪt]", "[ˈmemərɪ]",
            "[ˈɒfɪs] ", "[pɜːsn]", "[riːzn]", "[skriːn]", "[θrəʊt]", "[ˈsentə]", "[ˈfæm(ə)lɪ]", "[ˈməʊmənt]",
            "[ˈpe(ə)rənt]", "[ˈsɪstɪm]", "[ʤʌŋgl]",
            "[ˈneɪʧə]", "[ˈnɛfju] ", "[ˈpærət]", "[pəˈtrəʊl]"]
# транскрипция слов для пятого уровня
words5tr = ["[bəˈluːn]", "[ˈlaɪbrərɪ]", "[ˈhʌndrəd]", "[ˈhʌzbənd]", "[ˈkɪʧɪn]", "[məˈʃiːn]", "[ˈsɜːvɪs]", "[ˈmesɪʤ]",
            "[əˈkaʊnt]", "[əˈpɪnjən]",
            "[ˈreɪnbəʊ]", "[ˈkwesʧən]", "[ˈlæŋgwɪʤ]", "[ˈdeɪtəbeɪs] ", "[ˈgræmə]", "[ˈhɪstərɪ]", "[ˈkaɪndnɪs]",
            "[ˈəʊvəkəʊt]"]
# транскрипция слов для шестого уровня
words6tr = ["[ɪnfəˈmeɪʃn]", "[ˈʃəʊldə]", "[ˈtelɪfəʊn]", "[ˈgʌv(ə)mənt]", "[rɪˈleɪʃnʃɪp]", "[d(a)ɪˈrekt(ə)rɪ]",
            "[edjʊˈkeɪʃn]", "[ɪnstəˈleɪʃn]"]
# виджеты
root = tk.Tk()
root.title("Lingua Dictionary")
root.geometry("1800x1600")
numOfValidErrors = 1
isDone = False


def lup():
    if level == 1:
        levelUpgrade = 4
    elif level == 2:
        levelUpgrade = 5
    elif level == 3:
        levelUpgrade = 6
    elif level == 4:
        levelUpgrade = 7
    elif level == 5:
        levelUpgrade = 8
    else:
        levelUpgrade = 7


def numoferrs(d):
    if d == True:
        numOfValidErrors -= 1
        d = False
    return d


def end(wordIsGenerated, levup, up, minus, level, correctLetters, missedLetters, numOfValidErrors, compleatWords):
    if up == 1:
        if level < 6:
            level += 1
            if level == 1:
                up = 4
            elif level == 2:
                up = 5
            elif level == 3:
                up = 6
            elif level == 4:
                up = 7
            elif level == 5:
                up = 8
            else:
                up = 7
        else:
            passed = Label(text='You have passed the game!\n I hope it was interesting\nGood luck!', bg=b_colour,
                           width=50, font="Arial 20")
            passed.place(relx=.15, rely=.2, anchor="c", bordermode=OUTSIDE)
            sys.exit()
    if level == 1:
        btn_colour = "#f06071"
        b_colour = "#f7d8d9"
    elif level == 2:
        btn_colour = '#FF9F40'
        b_colour = '#FFB873'
    elif level == 3:
        btn_colour = '#4B5CD7'
        b_colour = '#717DD7'
    elif level == 4:
        btn_colour = '#5CCCCC'
        b_colour = '#33CCCC'
    elif level == 5:
        btn_colour = '#EB3B88'
        b_colour = '#EB6AA3'
    else:
        btn_colour = '#DAFB3F'
        b_colour = '#E3FB71'
    if minus == True:
        up -= 1
    win1 = Label(text='                      ' + '\n' + '\n' + '\n', bg=b_colour, width=50, font="Arial 20")
    win1.place(relx=.10, rely=.6, anchor="c", bordermode=OUTSIDE)
    # con_btn['state'] = 'disabled'
    if wordIsGenerated == False:
        secretWord = "done"
        isDone = False
        # генерация еще не пройденного слова
        if level == 1:
            num = random.randint(0, len(words1) - 1)
            secretWord = words1[num]
        elif level == 2:
            num = random.randint(0, len(words2) - 1)
            secretWord = words2[num]
            for i in range(0, len(secretWord), 1):
                correctLetters += "_"
            for i in range(0, numOfValidErrors + 1, 1):
                missedLetters += "_"
        elif level == 3:
            num = random.randint(0, len(words3) - 1)
            secretWord = words3[num]
            for i in range(0, len(secretWord), 1):
                correctLetters += "_"
            for i in range(0, numOfValidErrors + 1, 1):
                missedLetters += "_"
        elif level == 4:
            num = random.randint(0, len(words4) - 1)
            secretWord = words4[num]
            for i in range(0, len(secretWord), 1):
                correctLetters += "_"
            for i in range(0, numOfValidErrors + 1, 1):
                missedLetters += "_"
        elif level == 5:
            num = random.randint(0, len(words5) - 1)
            secretWord = words5[num]
            for i in range(0, len(secretWord), 1):
                correctLetters += "_"
            for i in range(0, numOfValidErrors + 1, 1):
                missedLetters += "_"
        else:
            num = random.randint(0, len(words6) - 1)
            secretWord = words6[num]
            for i in range(0, len(secretWord), 1):
                correctLetters += "_"
            for i in range(0, numOfValidErrors + 1, 1):
                missedLetters += "_"
        if level == 1:
            b = len(words1)
        elif level == 2:
            b = len(words2) + len(words1)
        elif level == 3:
            b = len(words3) + len(words2) + len(words1)
        elif level == 4:
            b = len(words4) + len(words3) + len(words2) + len(words1)
        elif level == 5:
            b = len(words5) + len(words4) + len(words3) + len(words2) + len(words1)
        else:
            b = len(words6) + len(words5) + len(words4) + len(words3) + len(words2) + len(words1)
        while set(secretWord).issubset(compleatWords) and len(compleatWords) < b:
            if level == 1:
                num = random.randint(0, len(words1) - 1)
                secretWord = words1[num]
            elif level == 2:
                num = random.randint(0, len(words2) - 1)
                secretWord = words2[num]
                for i in range(0, len(secretWord), 1):
                    correctLetters += "_"
                for i in range(0, numOfValidErrors + 1, 1):
                    missedLetters += "_"
            elif level == 3:
                num = random.randint(0, len(words3) - 1)
                secretWord = words3[num]
                for i in range(0, len(secretWord), 1):
                    correctLetters += "_"
                for i in range(0, numOfValidErrors + 1, 1):
                    missedLetters += "_"
            elif level == 4:
                num = random.randint(0, len(words4) - 1)
                secretWord = words4[num]
                for i in range(0, len(secretWord), 1):
                    correctLetters += "_"
                for i in range(0, numOfValidErrors + 1, 1):
                    missedLetters += "_"
            elif level == 5:
                num = random.randint(0, len(words5) - 1)
                secretWord = words5[num]
                for i in range(0, len(secretWord), 1):
                    correctLetters += "_"
                for i in range(0, numOfValidErrors + 1, 1):
                    missedLetters += "_"
            else:
                num = random.randint(0, len(words6) - 1)
                secretWord = words6[num]
                for i in range(0, len(secretWord), 1):
                    correctLetters += "_"
                for i in range(0, numOfValidErrors + 1, 1):
                    missedLetters += "_"
    buttonIsClicked = False
    # задание транскрипции и перевода
    if level == 1:
        numOfValidErrors = 1
        translation = words1Translations[num]
        transkription = words1tr[num]
    elif level == 2:
        numOfValidErrors = 2
        translation = words2Translations[num]
        transkription = words2tr[num]
    elif level == 3:
        numOfValidErrors = 3
        translation = words3Translations[num]
        transkription = words3tr[num]
    elif level == 4:
        numOfValidErrors = 4
        translation = words4Translations[num]
        transkription = words4tr[num]
    elif level == 5:
        numOfValidErrors = 5
        translation = words5Translations[num]
        transkription = words5tr[num]
    else:
        numOfValidErrors = 6
        translation = words6Translations[num]
        transkription = words6tr[num]
    wordIsGenerated = True
    correctLetters = []
    missedLetters = []
    for i in range(0, numOfValidErrors + 1, 1):
        missedLetters += "_"
    for i in range(0, len(secretWord), 1):
        correctLetters += "_"
    wrlet = "Wrong letters: "
    if missedLetters[0] == '_':
        wrlet += "All letters are right."
    else:
        for i in range(0, len(missedLetters), 1):
            if not missedLetters[i] in wrlet and missedLetters[i] != '_':
                wrlet += missedLetters[i] + ", "
    wrletLbl = Label(text=wrlet, bg=b_colour, width=60, font="Arial 20")
    wrletLbl.place(relx=.630, rely=.2, anchor="c", bordermode=OUTSIDE)
    corlet = []
    for i in range(0, len(secretWord), 1):
        corlet += correctLetters[i]
    corletLbl = Label(text=corlet, bg=b_colour, width=50, font="Arial 20")
    corletLbl.place(relx=.50, rely=.4, anchor="c", bordermode=OUTSIDE)
    # ввод и проверка
    letterIsCorrect = False
    buttonIsClicked = False
    con_btn = Button(text="Continue", font="Arial 30", background="#A1F43D",
                     command=lambda: end(False, True, up, False, level, correctLetters, missedLetters, numOfValidErrors,
                                         compleatWords))
    con_btn.place(relx=.900, rely=.87, anchor="c", height=85, width=260, bordermode=OUTSIDE)
    con_btn['state'] = 'disabled'
    trans = 'Russian translation: ' + translation
    transLbl = Label(text=trans, bg=b_colour, width=50, font="Arial 20")
    transLbl.place(relx=.15, rely=.2, anchor="c", bordermode=OUTSIDE)
    root.config(bg=b_colour)
    pressLbl = Label(text='Click the button', bg=b_colour, width=50, font="Arial 20")
    pressLbl.place(relx=.11, rely=.5, anchor="c", bordermode=OUTSIDE)
    secretWord_lbl = Label(text="Secret word: ", bg=b_colour, width=10, font="Arial 20")
    secretWord_lbl.place(relx=.50, rely=.3, anchor="c", bordermode=OUTSIDE)
    level_out = "Your level is: " + str(level)
    levelIs = Label(text=level_out, bg=b_colour, width=110, font="Arial 20")
    levelIs.place(relx=.10, rely=.1, anchor="c", bordermode=OUTSIDE)
    levelIncreate = "To increate the level, you need to win " + str(up) + " more times"
    levelIncreateLbl = Label(text=levelIncreate, bg=b_colour, width=100, font="Arial 20")
    levelIncreateLbl.place(relx=.700, rely=.1, anchor="c", bordermode=OUTSIDE)
    mistakes = "You can do a mistake " + str(numOfValidErrors)
    if numOfValidErrors == 1:
        mistakes += ' time.'
    else:
        mistakes += ' times.'
    mistake = Label(text=mistakes, bg=b_colour, width=50, font="Arial 20")
    mistake.place(relx=.16, rely=.3, anchor="c", bordermode=OUTSIDE)

    def click_a():
        isDone = False
        letter = 'a'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_a, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_b():
        isDone = False
        letter = 'b'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_b, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_c():
        isDone = False
        letter = 'c'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_c, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_d():
        isDone = False
        letter = 'd'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_d, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_e():
        isDone = False
        letter = 'e'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_e, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_f():
        isDone = False
        letter = 'f'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_f, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_g():
        isDone = False
        letter = 'g'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_g, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_q():
        isDone = False
        letter = 'q'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_q, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_r():
        isDone = False
        letter = 'r'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_r, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_s():
        isDone = False
        letter = 's'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_s, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_t():
        isDone = False
        letter = 't'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_t, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_u():
        isDone = False
        letter = 'u'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_u, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_v():
        isDone = False
        letter = 'v'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_v, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_w():
        isDone = False
        letter = 'w'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_w, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_x():
        isDone = False
        letter = 'x'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_x, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_h():
        isDone = False
        letter = 'h'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_h, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_i():
        isDone = False
        letter = 'i'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_i, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_j():
        isDone = False
        letter = 'j'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_j, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_k():
        isDone = False
        letter = 'k'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_k, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_l():
        isDone = False
        letter = 'l'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_l, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_m():
        isDone = False
        letter = 'm'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_m, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_n():
        isDone = False
        letter = 'n'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_n, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_p():
        isDone = False
        letter = 'p'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_p, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_o():
        isDone = False
        letter = 'o'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_o, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_y():
        isDone = False
        letter = 'y'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_y, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    def click_z():
        isDone = False
        letter = 'z'
        buttonIsClicked = True
        click_done(letter, secretWord, correctLetters, missedLetters, btn_z, translation, transkription, up, level,
                   numOfValidErrors, compleatWords, b_colour, con_btn)

    btn_a = Button(text="a", font="Arial 30", background=btn_colour, command=click_a)
    btn_b = Button(text="b", font="Arial 30", background=btn_colour, command=click_b)
    btn_c = Button(text="c", font="Arial 30", background=btn_colour, command=click_c)
    btn_d = Button(text="d", font="Arial 30", background=btn_colour, command=click_d)
    btn_e = Button(text="e", font="Arial 30", background=btn_colour, command=click_e)
    btn_f = Button(text="f", font="Arial 30", background=btn_colour, command=click_f)

    btn_g = Button(text="g", font="Arial 30", background=btn_colour, command=click_g)
    btn_q = Button(text="q", font="Arial 30", background=btn_colour, command=click_q)
    btn_r = Button(text="r", font="Arial 30", background=btn_colour, command=click_r)
    btn_s = Button(text="s", font="Arial 30", background=btn_colour, command=click_s)
    btn_t = Button(text="t", font="Arial 30", background=btn_colour, command=click_t)
    btn_u = Button(text="u", font="Arial 30", background=btn_colour, command=click_u)

    btn_v = Button(text="v", font="Arial 30", background=btn_colour, command=click_v)
    btn_w = Button(text="w", font="Arial 30", background=btn_colour, command=click_w)
    btn_x = Button(text="x", font="Arial 30", background=btn_colour, command=click_x)
    btn_h = Button(text="h", font="Arial 30", background=btn_colour, command=click_h)
    btn_i = Button(text="i", font="Arial 30", background=btn_colour, command=click_i)
    btn_j = Button(text="j", font="Arial 30", background=btn_colour, command=click_j)

    btn_k = Button(text="k", font="Arial 30", background=btn_colour, command=click_k)
    btn_l = Button(text="l", font="Arial 30", background=btn_colour, command=click_l)
    btn_m = Button(text="m", font="Arial 30", background=btn_colour, command=click_m)
    btn_n = Button(text="n", font="Arial 30", background=btn_colour, command=click_n)
    btn_p = Button(text="p", font="Arial 30", background=btn_colour, command=click_p)
    btn_o = Button(text="o", font="Arial 30", background=btn_colour, command=click_o)

    btn_y = Button(text="y", font="Arial 30", background=btn_colour, command=click_y)
    btn_z = Button(text="z", font="Arial 30", background=btn_colour, command=click_z)

    btn_a.place(relx=.40, rely=.47, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_b.place(relx=.45, rely=.47, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_c.place(relx=.50, rely=.47, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_d.place(relx=.55, rely=.47, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_e.place(relx=.60, rely=.47, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_f.place(relx=.65, rely=.47, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_g.place(relx=.40, rely=.57, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_q.place(relx=.45, rely=.57, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_r.place(relx=.50, rely=.57, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_s.place(relx=.55, rely=.57, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_t.place(relx=.60, rely=.57, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_u.place(relx=.65, rely=.57, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_v.place(relx=.40, rely=.67, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_w.place(relx=.45, rely=.67, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_x.place(relx=.50, rely=.67, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_h.place(relx=.55, rely=.67, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_i.place(relx=.60, rely=.67, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_j.place(relx=.65, rely=.67, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_k.place(relx=.40, rely=.77, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_l.place(relx=.45, rely=.77, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_m.place(relx=.50, rely=.77, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_n.place(relx=.55, rely=.77, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_o.place(relx=.60, rely=.77, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_p.place(relx=.65, rely=.77, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_y.place(relx=.60, rely=.87, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    btn_z.place(relx=.65, rely=.87, anchor="c", height=65, width=65, bordermode=OUTSIDE)
    isDone = numoferrs(isDone)


def click_done(l1, secretWord, correctLetters, missedLetters, button, translation, transcription, up, level,
               numOfValidErrors, compleatWords, b_colour, con_btn):
    lettersAreDifferent = False
    letterIsCorrect = False
    if level == 1:
        numOfValidErrors = 1
    elif level == 2:
        numOfValidErrors = 2
    elif level == 3:
        numOfValidErrors = 3
    elif level == 4:
        numOfValidErrors = 4
    elif level == 5:
        numOfValidErrors = 5
    else:
        numOfValidErrors = 6
    for i in range(0, len(secretWord), 1):
        if secretWord[i] == l1:
            correctLetters[i] = l1
            letterIsCorrect = True
    if letterIsCorrect == False:
        incor = Label(text="Your input is incorrect.", bg=b_colour, width=50, font="Arial 20")
        incor.place(relx=.11, rely=.5, anchor="c", bordermode=OUTSIDE)
        button['state'] = 'disabled'
        button['background'] = '#FF4940'
        con_btn['state'] = 'disabled'
        wrlet = "Wrong letters: "
        # print(missedLetters)
        schet = 0
        for i in range(0, len(missedLetters), 1):
            if missedLetters[i] == '_' and schet == 0:
                schet += 1
                missedLetters[i] = l1
        for i in range(0, len(missedLetters), 1):
            if missedLetters[i] != '_':
                wrlet += missedLetters[i] + ', '
                numOfValidErrors -= 1
        # print('m',missedLetters)
        if missedLetters[0] == '_':
            wrlet += "All letters are right."
        wrletLbl = Label(text=wrlet, bg=b_colour, width=60, font="Arial 20")
        wrletLbl.place(relx=.630, rely=.2, anchor="c", bordermode=OUTSIDE)
        # print("Your input is incorrect.")
        mistakes = "You can do a mistake " + str(numOfValidErrors)
        if numOfValidErrors == 1:
            mistakes += ' time.'
        else:
            mistakes += ' times.'
        mistake = Label(text=mistakes, bg=b_colour, width=50, font="Arial 20")
        mistake.place(relx=.16, rely=.3, anchor="c", bordermode=OUTSIDE)
        if missedLetters[len(missedLetters) - 1] != '_':
            lose = Label(text="You lose.", bg=b_colour, width=50, font="Arial 20")
            compleatWords += secretWord
            lose.place(relx=.10, rely=.5, anchor="c", bordermode=OUTSIDE)
            a = '\nSecret word is ' + secretWord + '\n        Russian translation: ' + translation + '\nTranscription is ' + transcription
            l1 = Label(text=a, bg=b_colour, width=50, font="Arial 20")
            l1.place(relx=.10, rely=.6, anchor="c", bordermode=OUTSIDE)
            root["bg"] = '#FF4040'
            con_btn = Button(text="Continue", font="Arial 30", background="#A1F43D",
                             command=lambda: end(False, True, up, False, level, correctLetters, missedLetters,
                                                 numOfValidErrors, compleatWords))
            con_btn.place(relx=.900, rely=.87, anchor="c", height=85, width=260, bordermode=OUTSIDE)
            con_btn['state'] = 'normal'
    else:
        cor = Label(text="Your input is correct.", bg=b_colour, width=50, font="Arial 20")
        con_btn = Button(text="Continue", font="Arial 30", background="#A1F43D",
                         command=lambda: end(False, True, up, False, level, correctLetters, missedLetters,
                                             numOfValidErrors, compleatWords))
        con_btn.place(relx=.900, rely=.87, anchor="c", height=85, width=260, bordermode=OUTSIDE)
        con_btn['state'] = 'disabled'
        cor.place(relx=.11, rely=.5, anchor="c", bordermode=OUTSIDE)
        button['state'] = 'disabled'
        button['background'] = '#80EA69'
        corlet = []
        for i in range(0, len(secretWord), 1):
            corlet += correctLetters[i]
            # print(correctLetters[i], end=" ")
        # print('\n')
        corletLbl = Label(text=corlet, bg=b_colour, width=50, font="Arial 20")
        corletLbl.place(relx=.50, rely=.4, anchor="c", bordermode=OUTSIDE)
        notWin = False
        for i in range(len(correctLetters)):
            if secretWord[i] != correctLetters[i]:
                notWin = True
        if notWin == False:
            win = Label(text='You won. ', bg=b_colour, width=50, font="Arial 20")
            con_btn = Button(text="Continue", font="Arial 30", background="#A1F43D",
                             command=lambda: end(False, True, up, True, level, correctLetters, missedLetters,
                                                 numOfValidErrors, compleatWords))
            con_btn.place(relx=.900, rely=.87, anchor="c", height=85, width=260, bordermode=OUTSIDE)
            win.place(relx=.10, rely=.5, anchor="c", bordermode=OUTSIDE)
            a = '\nSecret word is ' + secretWord + '\n        Russian translation: ' + translation + '\nTranscription is ' + transcription
            win1 = Label(text=a, bg=b_colour, width=50, font="Arial 20")
            win1.place(relx=.10, rely=.6, anchor="c", bordermode=OUTSIDE)
            con_btn['state'] = 'normal'
            compleatWords += secretWord
            root["bg"] = '#6FF6CA'
    isDone = True


# игра
wordIsGenerated = False
gameIsNotOver = True
while gameIsNotOver == True:
    level = 1
    lup()
    correctLetters = []
    missedLetters = []
    numOfValidErrors = 1
    compleatWords = ["done"]
    con_btn = Button(text="Continue", font="Arial 30", background="#A1F43D",
                     command=lambda: end(False, True, 4, False, level, correctLetters, missedLetters, numOfValidErrors,
                                         compleatWords))
    con_btn.place(relx=.900, rely=.87, anchor="c", height=85, width=260, bordermode=OUTSIDE)
    con_btn['state'] = 'disabled'
    win = Label(text='', bg="#f7d8d9", width=50, font="Arial 20")
    win.place(relx=.10, rely=.5, anchor="c", bordermode=OUTSIDE)
    win.place_forget()
    end(False, True, 4, False, 1, correctLetters, missedLetters, 1, compleatWords)
    root.mainloop()
