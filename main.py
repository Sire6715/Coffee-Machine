MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



#TODO prompt user.
machine_on = True

water = resources["water"] 
milk = resources["milk"] 
coffee = resources["coffee"] 



while machine_on:
    user_input =  input("What would you like? (espresso/Latte/Capaccino)").lower()
                
    if user_input == "off":
        exit()
        machine_on = False
        
    elif user_input == "report":
        for x in resources:
            print(f"{x}: {resources[x]}")
    elif user_input in MENU:
        drink_ingredients = MENU[user_input]["ingredients"]  
        
        if drink_ingredients.get("water", 0) < water:
            print("Sorry there is not enough water.")
        elif drink_ingredients.get("milk", 0) < milk:
            print("Sorry there is not enough milk.")
        elif drink_ingredients.get("coffee", 0) < coffee:
            print("sorry there is not enough coffee")     
        else:
            for item in drink_ingredients:
                resources[item] -= drink_ingredients[item]
                print(f"Here is your {user_input}. Enjoy! ☕")
                                                            
      
