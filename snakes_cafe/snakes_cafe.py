print('**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n**************************************\n** To quit at any time, type "quit" **\n**************************************')
print('Appetizers\n----------\nWings\nCookies\nSpring Rolls\n\nEntrees\n-------\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\n\nDesserts\n--------\nIce Cream\nCake\nPie\n\nDrinks\n------\nCoffee\nTea\nUnicorn Tears\n')


check={}
# check.append(order)


order=' '

while order !="quit":
    order=input('***********************************\n** What would you like to order? **\n***********************************\n >')

    if order in check:
      check[order]+=1
    else:
      check[order]=1

    if order=="quit":
          print('good bye ... have a nice day')
    else:

      print(f'** {check[order]} order of {order} have been added to your meal **')