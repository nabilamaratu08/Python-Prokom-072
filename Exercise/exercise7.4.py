prompt = "\nEnter a pizza topping (or 'quit' to finish): "
 
topping = input(prompt)
 
while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input(prompt)