fruits = {'apple': 130, 'avocado': 50, 'banana': 110, 'grapefruit': 50, 'grapes': 60, 'honeydew': 90, 'kiwifruit': 90, 'lemon': 90, 'lime': 15, 'nectarine': 20, 'orange': 60, 'peach': 80, 'pear': 100, 'pineapple': 100, 'plums': 50, 'strawberries': 70, 'sweet cherries': 100, 'tangerine': 100, 'watermelon': 50}

frt = input("Item: ").strip().lower()

if frt in fruits.keys():
    print("Calories:", fruits[frt])
