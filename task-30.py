
# Напишите программу для подсчета количества гласных и согласных букв в введенной
# пользователем строке.

def letter_count(str):
    vowels_count = 0
    consonants_count = 0

    vowels = "аеёиоуыэюя"

    for index in str:
        if index.lower() in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    return [print("гласные", vowels_count), print("согласные", consonants_count)]


print(letter_count('котятки ребятки когда нам поставят пятерки'))