def get_recipe_price(prices,optionals=[],**ingredients_and_amounts):
    returnPrice = 0
    if not prices:
        return returnPrice
    for key in prices:
        print(key)
        if key not in optionals:
            for ingredient, amount in ingredients_and_amounts.items():
                if ingredient == key:
                    returnPrice += prices[key]*amount

    return returnPrice//100


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

print(get_recipe_price({}))