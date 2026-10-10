import random
choices = ["камень","ножницы","бумага"]
computer = random.choice(choices)
max_score = 3
player_score = 0
computer_score = 0
while True:
    player = input("Камень, ножницы или бумага? (выход - закончить): ").lower().strip()

    if player == "выход":
        break

    if player not in choices:
        print("Выбери камень, ножницы или бумагу")
        continue

    computer = random.choice(choices)
    print("Компьютер выбрал:", computer)

    if computer == player:
        print("ничья")

    elif (player == "камень" and computer == "ножницы") or (player == "ножницы" and computer == "бумага") or (player == "бумага" and computer == "камень"):
        player_score += 1
        print("игрок: ", player_score, ":", "комп: ", computer_score)
    elif (computer == "камень" and player == "ножницы") or (computer == "ножницы" and player == "бумага") or (computer == "бумага" and player == "камень"):
        computer_score += 1
        print("игрок: ", player_score, ":", "комп: ", computer_score)
    if player_score == max_score:
        print("Ты выиграл матч!")
        break
    if computer_score == max_score:
        print("Компьютер выиграл матч")
        break
print("Итоговый счёт:", player_score, ":", computer_score)