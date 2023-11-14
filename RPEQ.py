import customtkinter as ctk
from CTkMessagebox import CTkMessagebox as msb
import webbrowser
import os

# DEFAULT
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("harlequin.json")
root = ctk.CTk()
rpeq_width = 700
rpeq_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
main_x = (screen_width/2) - (rpeq_width/2)
main_y = (screen_height/2) - (rpeq_height/2)
root.geometry(f"{rpeq_width}x{rpeq_height}+{int(main_x)}+{int(main_y)}")
root.title("Ren'Py Easy Quotes by wiwts")
root.after(201, lambda: root.iconbitmap("favicon.ico"))
root.resizable(False, False)

# DEFINE
frame = ctk.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both", expand=True)
is_custom_path = ctk.StringVar(value="false")

# FUNCTIONS

def rpeq(event=None): # PLACING QUOTES

    if nameF_input.get() == '':
        if language_choice.get() == "Russian":
            msb(title="Ошибка",
                message="Введите название файла!",
                icon='cancel',
                option_1="Закрыть")
            return
        elif language_choice.get() == "English":
            msb(title="Error",
                message="Enter the file name!",
                icon='cancel',
                option_1="Close")
            return

    nameF = nameF_input.get()

    if not os.path.exists(f'{nameF}.rpy'):
        if language_choice.get() == "Russian":
            msb(title="Ошибка",
                message=f"Файл \"{nameF}.rpy\" не найден!\nФайл должен быть в одной папке с программой и иметь разрешение .rpy",
                icon='cancel',
                option_1="Закрыть")
            return
        elif language_choice.get() == "English":
            msb(title="Error",
                message=f"The \"{nameF}.rpy\" file was not found!\nThe file must be in the same folder with the program and have the permission .rpy",
                icon='cancel',
                option_1="Close")
            return

    char = char_input.get()

    characters = char.split()
    if characters != []:
        characters_there_are = True
    else:
        characters_there_are = False

    badwords = ['label', '$', 'show', 'call', 'jump', 'scene', 'stop', 'play', 'python:', 'menu:', 'init:', 'init', '"',
                '\'', 'pause', 'zoom', 'align', 'xalign', 'yalign', 'xpos', 'ypos', 'linear', 'transform']
    sp_lst = []
    num = 0

    if is_custom_path.get() == "false" or path_input.get() == '':
        newdir = os.path.dirname(f'RPEQ/{nameF}0.rpy')
        curdir = 'RPEQ'
    else:
        newdir = os.path.dirname(f'{path_input.get()}\\{nameF}0.rpy')
        curdir = f'{path_input.get()}'
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
        # print(sp_lst)

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

                    # print("1")

                else:
                    with open(f'{curdir}\\{nameF}0.rpy', f"{type1}", encoding='utf-8') as q2:
                        type1 = "a"
                        mm2 = ' '.join(sp_lst[i])
                        q2.write(f'{mm2}\n')

                    # print("0")

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

    if language_choice.get() == "Russian":
        msb(title="Информация",
            message="Готово!\nМожно закрыть программу.",
            icon='info',
            option_1="Закрыть")
    elif language_choice.get() == "English":
        msb(title="Info",
            message="Done! You can close the program.",
            icon='info',
            option_1="Close")

def users_path(): # OPTIONAL

    if is_custom_path.get() == "false":
        path_input.configure(state="disabled", placeholder_text="", fg_color="#87919a")
    elif is_custom_path.get() == "true":
        path_input.configure(state="normal", placeholder_text="C:\\Program Files\\renpy projects\\my novell", fg_color="#a9b8c4")

def contacts(): # FEEDBACK & CONTACTS

    contacts_window = ctk.CTkToplevel()
    contacts_window.attributes('-topmost', 'true')
    contacts_window.grab_set()
    contacts_width = 300
    contacts_height = 300
    contacts_x = (screen_width/2) - (contacts_width/2)
    contacts_y = (screen_height/2) - (contacts_height/2)
    contacts_window.geometry(f"{contacts_width}x{contacts_height}+{int(contacts_x)}+{int(contacts_y)}")
    contacts_window.title("Обратная связь")
    contacts_window.after(250, lambda: root.iconbitmap("favicon.ico"))
    contacts_window.resizable(False, False)
    contacts_frame = ctk.CTkFrame(contacts_window)
    contacts_frame.pack(padx=30, pady=20, fill="both", expand=True)

    if language_choice.get() == "English":
        link1 = ctk.CTkLabel(contacts_frame,
                             text="My VK group",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link1.pack(padx=20, pady=10)
        link1.bind("<Button-1>", lambda e: callback("https://vk.com/ovanfor"))

        link2 = ctk.CTkLabel(contacts_frame,
                             text="My VK page",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link2.pack(padx=20, pady=10)
        link2.bind("<Button-1>", lambda e: callback("https://vk.com/da_wiwts"))

        link3 = ctk.CTkLabel(contacts_frame,
                             text="My Telegram",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link3.pack(padx=20, pady=10)
        link3.bind("<Button-1>", lambda e: callback("https://t.me/ruslanwiwts"))

        link4 = ctk.CTkLabel(contacts_frame,
                             text="My YouTube channel",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link4.pack(padx=20, pady=10)
        link4.bind("<Button-1>", lambda e: callback("https://www.youtube.com/channel/UCX99TT0Qb0ca6sRglmcNkxw"))

        link5 = ctk.CTkLabel(contacts_frame, text="My Discord:")
        link5.pack()
        link6 = ctk.CTkEntry(contacts_frame,
                             placeholder_text=".cofta (677557278555111454)",
                             fg_color="#020202",
                             placeholder_text_color="#FFFFFF",
                             width=190,
                             height=20)
        link6.pack()
        link6.configure(placeholder_text=".cofta (677557278555111454)", state="readonly")

    elif language_choice.get() == "Russian":

        link1 = ctk.CTkLabel(contacts_frame,
                             text="Мой паблик ВК",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link1.pack(padx=20, pady=10)
        link1.bind("<Button-1>", lambda e: callback("https://vk.com/ovanfor"))

        link2 = ctk.CTkLabel(contacts_frame,
                             text="Моя страница ВК",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link2.pack(padx=20, pady=10)
        link2.bind("<Button-1>", lambda e: callback("https://vk.com/da_wiwts"))

        link3 = ctk.CTkLabel(contacts_frame,
                             text="Мой ТГ",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link3.pack(padx=20, pady=10)
        link3.bind("<Button-1>", lambda e: callback("https://t.me/ruslanwiwts"))

        link4 = ctk.CTkLabel(contacts_frame,
                             text="Мой канал на YouTube",
                             text_color="#ffa3f0",
                             cursor="hand2")
        link4.pack(padx=20, pady=10)
        link4.bind("<Button-1>", lambda e: callback("https://www.youtube.com/channel/UCX99TT0Qb0ca6sRglmcNkxw"))

        link5 = ctk.CTkLabel(contacts_frame, text="Мой аккаунт Discord:")
        link5.pack()
        link6 = ctk.CTkEntry(contacts_frame,
                             placeholder_text=".cofta (677557278555111454)",
                             fg_color="#020202",
                             placeholder_text_color="#FFFFFF",
                             width=190,
                             height=20)
        link6.pack()
        link6.configure(placeholder_text=".cofta (677557278555111454)", state="readonly")

    contacts_window.mainloop()

def callback(url): # WEB
   webbrowser.open_new_tab(url)

def lang_picker(choice):
    if choice == "Russian":
        nameF_label.configure(text="Введите название файла (без разрешения)")
        char_label.configure(text="Введите переменные персонажей через пробел,\nесли их нет, то оставьте поле пустым")
        output_dir_choice.configure(text="Свой путь для измененного файла")
        OK_button.configure(text="Выполнить")
        link_label.configure(text="Обратная связь")

    elif choice == "English":
        nameF_label.configure(text="Enter the file name (without permission)")
        char_label.configure(text="Enter character variables separated by a space,\nif there are none, then leave the field empty")
        output_dir_choice.configure(text="Your path for the modified file")
        OK_button.configure(text="OK")
        link_label.configure(text="Feedback")

# UI

root.bind('<Return>', rpeq)

nameF_label = ctk.CTkLabel(frame,
                           text="Введите название файла (без разрешения)",
                           font=("Segoi", 16),
                           justify="left",
                           anchor="w")
nameF_label.pack(padx=30, pady=10, anchor="w")

nameF_input = ctk.CTkEntry(frame,
                           placeholder_text="script",
                           width=500,
                           height=40)
nameF_input.pack(padx=25, pady=10, anchor="w")

char_label = ctk.CTkLabel(frame,
                          text="Введите переменные персонажей через пробел,\nесли их нет, то оставьте поле пустым",
                          font=("Segoi", 16),
                          justify="left",
                          anchor="w")
char_label.pack(padx=30, pady=10, anchor="w")

char_input = ctk.CTkEntry(frame,
                          placeholder_text="eileen",
                          width=500,
                          height=40)
char_input.pack(padx=25, pady=10, anchor="w")

output_dir_choice = ctk.CTkCheckBox(frame,
                                    text="Свой путь для измененного файла",
                                    command=users_path,
                                    variable=is_custom_path,
                                    onvalue="true",
                                    offvalue="false",
                                    corner_radius=30)
output_dir_choice.pack(pady=20)

path_input = ctk.CTkEntry(frame,
                          width=500,
                          height=40,
                          state="disabled",
                          fg_color="#87919a")
path_input.pack(padx=25, pady=10, anchor="w")

OK_button = ctk.CTkButton(frame,
                          text="Выполнить",
                          fg_color="transparent",
                          command=rpeq)
OK_button.pack(pady=20)

link_label = ctk.CTkButton(root,
                           text="Обратная связь",
                           command=contacts)
link_label.pack(pady=10)

langs_allowed = ["Russian", "English"]
language_choice = ctk.CTkComboBox(root,
                                  values=langs_allowed,
                                  command=lang_picker)
language_choice.pack()

version_label = ctk.CTkLabel(root,
    text="Версия 3.0",
    font=("Segoi", 12),
    justify="left",
    anchor="w")
version_label.pack(padx=10, pady=10, anchor="w")


root.mainloop()
