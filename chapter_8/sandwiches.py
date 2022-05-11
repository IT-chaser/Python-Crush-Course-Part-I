def sandwiches(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
sandwiches('cheese')
sandwiches('beef', 'honey', 'eggs')
