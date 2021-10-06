vandaag = input("Welke dag is het vandaag? (ma,di,wo,do,vr,za,zo)")
eindreach = False

maandag = "ma"
dinsdag = "di"
woensdag = "wo"
donderdag = "do"
vrijdag = "vr"
zaterdag = "za"
zondag = "zo"

while eindreach == False:
    if vandaag == maandag:
        print(maandag)
        eindreach = True
    if vandaag == dinsdag:
        print(maandag, dinsdag)
        eindreach = True
    if vandaag == woensdag:
        print(maandag, dinsdag, woensdag)
        eindreach = True
    if vandaag == donderdag:
        print(maandag, dinsdag, woensdag, donderdag)
        eindreach = True
    if vandaag == vrijdag:
        print(maandag, dinsdag, woensdag, donderdag, vrijdag)
        eindreach = True
    if vandaag == zaterdag:
        print(maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag)
        eindreach = True
    if vandaag == zondag:
        print(maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag)
        eindreach = True
    else:
        break

# ik heb het maar op deze manier gedaan want na 2 dagen brainstormen kwam ik er nog steeds niet uit.