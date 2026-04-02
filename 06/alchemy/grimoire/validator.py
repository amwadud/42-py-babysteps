def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    for element in valid:
        if element in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
