menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 230,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
def make_coffee(choice,ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"here is you {choice}..enjoy")
def ispayment_success(money_received,cost):
  if money_received >= cost:
      global profit
      profit+=cost
      change=money_received-cost
      print(f"here is the change: {change}")
      return True
  else:
      print("there is no enough money.momey is refunded")
      return False
def check_resoures(ingredients):
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"sorry, there is not enough {item} ")
            return False
        else:
            return True
def process_coins():
    print("please insert coins")
    total=0
    coins_5=int(input("please insert how many 5:"))
    coins_10=int(input("please insert how many 10:"))
    coins_20=int(input("please insert how many 20:"))
    total+=coins_5*5
    total+=coins_10*10
    total+=coins_20*20
    return total
should_continue = True
while should_continue:
    choice = input("What would you like to have?(latte/espresso/cappuccino): ").lower()
    if choice=='off':
        should_continue = False
    elif choice=='report':
        print(f"water={resources['water']}mg,\nmilk={resources['milk']}ml,\ncoffee= {resources['coffee']}g\nmoney=Rs.{profit}")
    else:
        coffee_type=menu[choice]
        print(coffee_type)
        if check_resoures(coffee_type['ingredients']):
           payment=process_coins()
           if ispayment_success(payment,coffee_type['cost']):
               make_coffee(choice,coffee_type['ingredients'])
