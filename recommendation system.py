items = {
    "movies": {
        "avengers": "action",
        "titanic": "romance",
        "inception": "sci-fi",
        "the godfather": "crime"
    },
    "books": {
        "harry potter": "fantasy",
        "the great gatsby": "classic",
        "to kill a mockingbird": "historical fiction",
        "1984": "dystopian"
    },
    "products": {
        "iphone": "electronics",
        "nike shoes": "footwear",
        "samsung tv": "electronics",
        "adidas hoodie": "clothing"
    }
}

while True:
    print("\nCategories: movies, books, products")
    category = input("Enter a category (or 'exit' to quit): ").strip().lower()

    if category == "exit":
        print("Thank you for using our service! Goodbye!")
        break

    if category not in items:
        print("Invalid category. Please try again.")
        continue

    print("Available types:")
    types = set(items[category].values())
    for t in types:
        print("- " + t)

    preference = input("Enter a type to filter by (or 'all' to see all items): ").strip().lower()

    print("Recommended items:")
    found = False

    for item, item_type in items[category].items():
        if preference == "all" or item_type.lower() == preference:
            print("- " + item)
            found = True

    if not found:
        print("No items found for the selected type.")

    again = input("Do you want to try again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for using our service! Goodbye!")
        break
