prompt = "\nEnter a pizza topping (or 'quit' to finish): "
 
# kondisi pada pernyataan while
print("--- Version 1: conditional test ---")
topping = input(prompt)
while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input(prompt)
 
# active variable
print("\n--- Version 2: active variable ---")
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")
 
# break
print("\n--- Version 3: break ---")
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")