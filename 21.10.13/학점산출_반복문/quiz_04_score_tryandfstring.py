while 1:
    score = input("enter the score : ")
    try:
        score = int(score)
    except:
        score = -1
    if score < 0 or score > 100:
        print("wrong score!")
        continue
    ch = "FDCBA"
    for i in range(5):
        if score < 60 + i * 10:
            print(f"your grade is {ch[i]}")
            break
        elif score == 100:
            print(f"your grade is A")
            break
