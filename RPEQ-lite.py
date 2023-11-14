
import os

def rpeq(): # PLACING QUOTES

    nameF = input("Введите название файла (без разрешения) ")

    if nameF == '':
        print("Введите название файла!")
        rpeq()

    if not os.path.exists(f'{nameF}.rpy'):
        print(f"Файл \"{nameF}.rpy\" не найден!\nФайл должен быть в одной папке с программой и иметь разрешение .rpy")
        rpeq()

    char = input("Введите переменные персонажей через пробел,\nесли их нет, то нажмите ENTER ")

    path_input = input("Свой путь для измененного файла (если нет, то нажмите ENTER)")

    characters = char.split()
    if characters != []:
        characters_there_are = True
    else:
        characters_there_are = False

    badwords = ['label', '$', 'show', 'call', 'jump', 'scene', 'stop', 'play', 'python:', 'menu:', 'init:', 'init', '"',
                '\'', 'pause', 'zoom', 'align', 'xalign', 'yalign', 'xpos', 'ypos', 'linear', 'transform']
    sp_lst = []
    num = 0

    if path_input == '':
        newdir = os.path.dirname(f'RPEQ/{nameF}0.rpy')
        curdir = 'RPEQ'
    else:
        newdir = os.path.dirname(f'{path_input}\\{nameF}0.rpy')
        curdir = f'{path_input}'
    type1 = 'w'
    if os.path.exists(newdir):
        pass
    else:
        os.makedirs(newdir)

    with open(f'{nameF}.rpy', "r", encoding='utf-8') as f:
        for l in f:
            sp = l.split()
            sp_lst.append(sp)
            num += 1

        for i in range(num):

            if sp_lst[i] != []:

                if sp_lst[i][0] not in badwords and '=' not in sp_lst[i] and '"' not in sp_lst[i][0]:
                    with open(f'{curdir}\\{nameF}0.rpy', f"{type1}", encoding='utf-8') as q:
                        type1 = "a"

                        if sp_lst[i][0] not in characters or characters_there_are == False:
                            mm = ' '.join(sp_lst[i])
                            q.write(f'"{mm}"\n')

                        else:
                            var = sp_lst[i][0]
                            del sp_lst[i][0]
                            mm = ' '.join(sp_lst[i])
                            q.write(var + f' "{mm}"\n')

                else:
                    with open(f'{curdir}\\{nameF}0.rpy', f"{type1}", encoding='utf-8') as q2:
                        type1 = "a"
                        mm2 = ' '.join(sp_lst[i])
                        q2.write(f'{mm2}\n')

    f.close()
    q.close()
    q2.close()

    place_tabs(nameF, curdir)

def place_tabs(nameF, curdir): # PLACING INDENTS

    if os.path.exists(f'{curdir}\\{nameF}.rpy'):
        os.remove(f'{curdir}\\{nameF}.rpy')
    with open(f'{nameF}.rpy', "r", encoding='utf-8') as f, open(f'{curdir}\\{nameF}0.rpy', "r", encoding='utf-8') as q:
        new_content = open(f'{curdir}\\{nameF}.rpy', "a+", encoding='utf-8')
        for line in f:
            if line != '\n':
                indent = len(line) - len(line.lstrip())
                content = q.readline()
                new_content.write(f'{" " * indent}{content}')
            else:
                new_content.write("\n")

        f.close()
        q.close()
        new_content.close()
        if os.path.exists(f'{curdir}\\{nameF}0.rpy'):
            os.remove(f'{curdir}\\{nameF}0.rpy')

    input("Готово!\nНажмите ENTER, чтобы закрыть программу.")

rpeq()