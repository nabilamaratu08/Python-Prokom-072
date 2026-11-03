sandwich_orders = ['tuna', 'ham', 'veggie', 'chicken']
finished_sandwiches = []
 
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
 
print("\nAll sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")