i = 1
anwser = input("programma verlaten? voer in quit. ")
while not anwser == "quit":
    anwser = input("programma verlaten? voer in quit. ")
    if anwser == "quit":
        print()
    else:
        i= i + 1

print("Deze vraag was ", i ," keer gesteld.")