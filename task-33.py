# Создайте программу, которая принимает строку в качестве входных данных и выводит
# частоту использования каждого символа в строке.

def letter_count(str):
    result = {}
    for i in str:
        count = 0
        for j in str:
            if i == j:
                count += 1
            else:
                continue
        result[i] = count
    return result

print("Введите число, я отвечу сколько раз повторяется символ:")
letter = input()
print(letter_count(letter))