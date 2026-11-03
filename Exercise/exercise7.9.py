sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ham',
                   'veggie', 'pastrami']
finished_sandwiches = []
 
print("Sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
 
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
 
print("\nAll sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")