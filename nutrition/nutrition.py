user_input = input("Item: ").title()

fruit = {
    "Apple": "130",
    "Avocado": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapefruit": "60",
    "Grapes": "90",
    "Honeydew": "50",
    "Kiwifruit": "90",
    "Lemon": "15",
    "Pear": "100",
    "Sweet Cherries": "100"
    }



if user_input in fruit:
    print ("Calories:",fruit[user_input])

