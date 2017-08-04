ingredients = [
{'ingredient': 'watermelon', 'form': 'cubed', 'amount': '4 cups'},
{'ingredient': 'sugar', 'form': 'granulated', 'amount': '1/2 cup'},
{'ingredient': 'basil', 'form': 'roughly chopped', 'amount': '2 cups'},
{'ingredient': 'lemon juice', 'form': 'juice', 'amount': '1/2 cup'},
{'ingredient': 'water', 'form': 'liquid', 'amount': '1/2 cup'},
{'ingredient': 'basil', 'form': 'leaf', 'amount': '4'},
]

instructions= ['start',
'place cubed watermelon on a baking sheet and freeze',
'cook the sugar in the water in a small saucepan over medium heat, stirring occasionally until sugar is compltely melted',
'turn off heat, add chopped basil, and stir until completely wilted. cool at room temp for at least 1 hour.',
'put half of the frozen watermelon in a blender',
'strain the basil syrup into the blender, using th back of a spoon to press out all of the flavor',
'add the lemon juice into the blender and blend until its smooth.',
'add the remaining watermelon and continue to blend until smooth',
'spoon the mixture into four glasses and garnish with basil leaves'
]

for ing in ingredients:
    print(ing)
    print("NAME ", ing['ingredient'])
    print("FORM ", ing['form'])
    print("AMOUNT ", ing['amount'])

for ins in instructions:
    print("Step", ins[])
