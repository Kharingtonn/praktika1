import datetime
import calendar

# Функция для определения дня недели на русском языке
def get_weekday(day: int, month: int, year: int) -> str:
    weekdays = [
        "понедельник", "вторник", "среда",
        "четверг", "пятница", "суббота", "воскресенье"
    ]
    date = datetime.date(year, month, day)
    # weekday(): понедельник=0, воскресенье=6
    return weekdays[date.weekday()]

# Функция для проверки високосного года
def is_leap(year: int) -> bool:
    return calendar.isleap(year)

# Функция для вычисления текущего возраста
def calculate_age(day: int, month: int, year: int) -> int:
    today = datetime.date.today()
    birth = datetime.date(year, month, day)
    # Вычитаем 1, если день/месяц рождения ещё не наступили в текущем году
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

# Словарь 7x5 для отображения цифр "семисегментным" стилем из звёздочек
STYLIZED_DIGITS = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        " *** "
    ],
    '2': [
        " *** ",
        "*   *",
        "   * ",
        "  *  ",
        "*****"
    ],
    '3': [
        " *** ",
        "    *",
        "  ** ",
        "    *",
        " *** "
    ],
    '4': [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *"
    ],
    '5': [
        "*****",
        "*    ",
        "**** ",
        "    *",
        "**** "
    ],
    '6': [
        " ****",
        "*    ",
        "**** ",
        "*   *",
        " ****"
    ],
    '7': [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   "
    ],
    '8': [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** "
    ],
    '9': [
        " ****",
        "*   *",
        " ****",
        "    *",
        "**** "
    ],
    ' ': [  # пробел для разделения блоков
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]
}

# Функция для печати даты в стилизованном виде
def print_stylized_date(day: int, month: int, year: int) -> None:
    s = f"{day:02d} {month:02d} {year:04d}"
    # Разбиваем на символы и строим строки результата
    rows = [""] * 5
    for char in s:
        pattern = STYLIZED_DIGITS.get(char, STYLIZED_DIGITS[' '])
        for i in range(5):
            rows[i] += pattern[i] + "  "  # два пробела между блоками
    # Выводим все пять строк
    for row in rows:
        print(row)

def main():
    # Ввод данных пользователя
    day = int(input("Введите день рождения (1-31): "))
    month = int(input("Введите месяц рождения (1-12): "))
    year = int(input("Введите год рождения (например, 1985): "))

    # Определяем день недели
    weekday = get_weekday(day, month, year)
    print(f"\nВы родились в {weekday}.")

    # Проверяем високосность года
    leap = is_leap(year)
    print(f"Год {year} {'был' if leap else 'не был'} високосным.")

    # Вычисляем возраст
    age = calculate_age(day, month, year)
    print(f"Сейчас вам {age} {'год' if 11<=age%100<=14 else ['лет','год','года'][min(age%10,2)]}.")

    # Печатаем стилизованную дату
    print("\nДата вашего рождения в стилизованном виде:")
    print_stylized_date(day, month, year)

if __name__ == "__main__":
    main()