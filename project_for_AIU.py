from pyfiglet import *
from termcolor import *

def converter(text_for_convert):
    print("=" * 50)
    f = Figlet(font=style_for_text)
    print(colored(f.renderText(text_for_convert), collor_for_text))
    print("=" * 50)
    
title = figlet_format("ASCII STUDIO", font="sub-zero")
print(title)
print("ASCII Studio — это простое и удобное приложение для создания ASCII-арта из обычного текста.\nВам больше не нужно вручную подбирать символы или разбираться со сложными настройками.\nПросто введите любую фразу, выберите понравившийся шрифт из огромной встроенной коллекции — и программа мгновенно превратит её в эффектную текстовую графику.")
print("несколько правил для использования ASCII Studio:\n1. Только английский алфавит.\n2. Все вводить корректно.\n3. Вводить все в своем поле \n4. Нажимайте кнопку 'Преобразовать' и наслаждайтесь результатом! ASCII Studio мгновенно превратит ваш текст в потрясающий ASCII-арт.")
for_cycle_repeating = True
while for_cycle_repeating:
    text_for_covert = input("Введите текст для создания ASCII-арта: ")
    collor_for_text = input('Выберите цвет для текста (например, "red", "green", "blue"): ').lower()
    style_for_text = input('Выберите стиль для текста (например, "sub-zero", "slant", "larry3d", "isometric1", "epic", "digital", "block", "bubble", "standard"): ').lower()
    try:
        print(converter(text_for_covert))
    except:
        print(colored("Упс! Произошла ошибка при создании ASCII-арта. Похоже что то введено не правильно. Пожалуйста, проверьте свои вводные данные и попробуйте снова.", "red"))
    repeat = input("Хотите создать еще один ASCII-арт? (да/нет): ").lower()
    if repeat != "да":
        for_cycle_repeating = False
print("Спасибо за использование ASCII Studio! До новых встреч!")