def make_sandwich(*items):
    """Summarize the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
 
 
make_sandwich('ham')
make_sandwich('tuna', 'lettuce', 'tomato')
make_sandwich('chicken', 'cheese', 'onion', 'mayo')