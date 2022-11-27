def string_or_not(x):
    return isinstance(x, str) and "yes" or "no"
print(string_or_not('Hexlet'))
print(string_or_not(10))
print(string_or_not(''))
print(string_or_not(


# def is_leap_year(x):
#     return x % 400 == 0 or x % 4 == 0 and not x % 100 == 0
# print(is_leap_year(2016))
# is_leap_year(2018)  # False
# is_leap_year(2017)  # False
# is_leap_year(2016)  # True


# def has_upper_case(t):
#     return t.casefold()>t
# print(has_upper_case("pYthon"))
# has_upper_case('')  # False
# has_upper_case('python')  # False
# has_upper_case('pyThon')  # True

# def is_first_letter_an_a(string):
#     first_letter = string[0]
#     return first_letter == 'a'
#
# print(is_first_letter_an_a('orange'))  # => False
# print(is_first_letter_an_a('apple'))

# def is_castle(string):
#     return string == 'Castle'
#
# print(is_castle('Sea'))


# def get_age_difference(year, year1):
#
#     return f"The age difference is {abs(year - year1)}"
# actual = get_age_difference(2001,2008)
# print(actual)
# def trim_and_repeat(text, offset=0, repetitions=1):
#     x = text[offset:]
#     y = x*repetitions
#     return y
# print(trim_and_repeat('python', offset=3, repetitions=2))
# print(trim_and_repeat('python', repetitions=3))
# print(trim_and_repeat("python"))



# def get_hidden_card(a, b=4):
#     x = a[12:]
#     y = ("*"*b)+x
#     return y
# print(get_hidden_card('9860040105765787'))

# def test(word, x):
#     which = word[:x]
#     change =which + "..."
#     return change
# print(test("it works", 4))
# print(test("salom", 2))
# def multiply(num1, num2):
#     num1 * num2
#
#
# result = multiply(2, 2)
# print(result)

# print(truncate())
# Передаём текст напрямую
# Обрезаем текст, оставляя 2 символа
# truncate('hexlet', 2)  # 'he...'

# Через переменную
# text = 'it works!'
# Обрезаем текст, оставляя 4 символа
# truncate(text, 4)  # 'it w...'