# name of student: Robin Vervoorn
# number of student: 99066333
# purpose of program: wisselgeld teruggeven
# function of program: wisselgeld berekenen en bepalen welke munten er terug moeten gegeven worden
# structure of program: while, if/elif/else, input, print, operators:  //  >  -  +  *  ==
coin500 = 0
coin300 = 0
coin200 = 0
coin50 = 0
coin20 = 0
coin10 = 0
coin5 = 0
coin2 = 0

toPay = int(float(input('Amount to pay: '))* 100) # hoeveel je moet betalen in euro's. Dat wordt later omgezet in centen.
paid = int(float(input('Paid amount: ')) * 100) # hoeveel je heb betaald in euro's. Dat wordt later omgezet in centen
change = paid - toPay # het wisselgeld = het aantal wat je heb betaald - het aantal dat je moet betalen

if change > 0: # als het aantal wisselgeld groter is dan 0,
  coinValue = 500 # dan wordt de muntwaarde 50
  
  while change > 0 and coinValue > 0: # terwijl het aantal wisselgeld en muntwaarde groter zijn dan 0,
    nrCoins = change // coinValue # aantal munten = wisselgeld (worteltrekken van) de muntwaarde

    if nrCoins > 0: # als het aantal munten groter is dan 0,
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # dan print "geef terug maximaal (aantal munten) munten van (muntwaarde) centen!"
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # de variabel nrCoinsReturned staat voor het aantal munten teruggegeven. die variabel staat vast aan de vraag: Hoeveel munten van (muntwaarde) centen heeft u teruggegeven?
      change -= nrCoinsReturned * coinValue # het wisselgeld = wisselgeld - aantal munten terugegeven * muntwaarde

# comment on code below: 
    if coinValue == 500:
      coinValue = 300
      coin500 = coin500 + nrCoinsReturned
    elif coinValue == 300:
      coinValue = 200
      coin300 = coin300 + nrCoinsReturned
    elif coinValue == 200:
      coinValue = 50
      coin200 = coin200 + nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      coin50 = coin50 + nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      coin20 = coin20 + nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      coin10 = coin10 + nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      coin5 = coin5 + nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      coin2 = coin2 + nrCoinsReturned
    else:
      coinValue = 0

if change > 0: # als het nog steeds groter is dan 0, dan word er geprint: "wisselgeld niet teruggegeven: (string(wisselgeld)) cent." om aan te geven dat er wisselgeld nog is dat niet terugbetaald kon worden met munten en anders print die: "klaar"
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done, you recieved: ' + str(coin500) + ' coins of 5 euro, ' + str(coin300) + ' coins of 3 euro, ' + str(coin200) + ' coins of 2 euro, ' + str(coin50) + ' coins of 50 cents, ' + str(coin20) + ' coins of 20 cents, ' + str(coin10) + ' coins of 10 cents, ' + str(coin5) + ' coins of 5 cents, ' + str(coin2) + ' coins of 2 cents.')
