import tkinter
from tkinter import filedialog, Text

def exit_program():
    """Закрывает приложение."""
    window.quit()  # Завершает основной цикл приложения и закрывает окно


def open_file_in_window():# Обработчмк события File - Open
    global current_file  # Объявляем переменную как глобальную
    current_file = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*')))
    if current_file:  # Если файл был выбран
        with open(current_file, 'r', encoding='utf-8') as file:  # Открываем файл в режиме чтения
            content = file.read()  # Читаем содержимое файла
            text_area.delete(1.0, tkinter.END)  # Очищаем текстовое поле
            text_area.insert(tkinter.END, content)  # Вставляем содержимое файла в текстовое поле


def save_file_in_window():# Обработчмк события File - Save
    if current_file:  # Если файл был загружен
        with open(current_file, 'w', encoding='utf-8') as file:  # Открываем файл в режиме записи
            content = text_area.get(1.0, tkinter.END)  # Получаем содержимое текстового поля
            file.write(content)  # Записываем содержимое в файл
    else:
        save_as()  # Если файл не был загружен, вызываем save_as()


def save_as():  #
    current_file = filedialog.asksaveasfilename(defaultextension='.txt',
                                                  filetypes=(('Текстовый файл', '*.txt'),
                                                             ('Все файлы', '*.*')))
    if current_file:  # Если имя файла было выбрано
        save_file_in_window()  # Сохраняем содержимое


def close_file_in_window():
    text_area.delete(1.0, tkinter.END)  # Очищаем текстовое поле

def help_program():#бработчмк события Help - Help
    with open('test.txt', 'r', encoding='utf-8') as file:  # Открываем файл в режиме чтения
        content = file.read()  # Читаем содержимое файла
        open_text_window(content) #Создает модальное окно для чтения текста и загрузка контента

def open_text_window(content):
    """Создает модальное окно для чтения текста."""
    text_window = tkinter.Toplevel(window)
    text_window.title("Help")
    text_window.geometry("400x300")
    text_window.resizable(False, False)  # Запрещаем изменение размера окна

    # Создаем текстовое поле для чтения
    text_area = Text(text_window, wrap='word', bg='light gray', state='normal')
    text_area.pack(expand=True, fill='both')
    text_area.insert(tkinter.END, content)  # Вставляем содержимое файла в текстовое поле
    text_area.config(state='disabled')  # Делаем текстовое поле только для чтения


def info_program():#бработчмк события Help - Info
    with open('test1.txt', 'r', encoding='utf-8') as file:  # Открываем файл в режиме чтения
        content = file.read()  # Читаем содержимое файла
        open_text_window(content) #Создает модальное окно для чтения текста и загрузка контента


#Основное окно
window = tkinter.Tk()

window.title('Блокнот')  # Устанавливаем заголовок окна
window.geometry('350x350') # Устанавливаем размеры окна
window.configure(bg='white') # Устанавливаем цвет фона
#window.resizable(False, False) # Запрещаем изменение размера окна

# Создание меню шбщее
menu = tkinter.Menu(window)  # Создаем объект меню
window.config(menu=menu) # Устанавливаем меню для окна

# Создание пункт меню "File"
file_menu = tkinter.Menu(menu, tearoff=0) # Создаем пунк меню "Файл"
menu.add_cascade(label='File', menu=file_menu) # Добавляем пунк меню в главное меню
# Добавление команды "Open" в пунк меню "Файл"
file_menu.add_cascade(label='Open', command=open_file_in_window) # add command open
# Добавление команды "Save" в пунк меню "File"
file_menu.add_cascade(label='Save', command=save_file_in_window) # add command open
# Добавление команды "Close" в пунк меню "File"
file_menu.add_cascade(label='Close', command=close_file_in_window) # add command open
# Добавление команды "Exit" в пунк меню "Файл"
file_menu.add_command(label='Exit', command=exit_program) # add command Exit

# Создание пунк меню "Halp"
help_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=help_menu)
# Добавление команды "Help" в пунк меню "Help"
help_menu.add_command(label='Help', command=help_program) # add command Help
# Добавление команды "Info" в пунк меню "Help"
help_menu.add_command(label='Info', command=info_program) # add command Info

# Создание текстового поля для редактирования
text_area = Text(window, wrap='word', bg='light gray')  # Создаем текстовое поле
text_area.pack(expand=True, fill='both')  # Позволяем текстовому полю заполнять окно

window.mainloop()