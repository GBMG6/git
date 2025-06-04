import json

def load_recipes():
    with open("C:/Users/USER/Desktop/파이썬/음식프로그램/recipes.json", "r", encoding="utf-8-sig") as f:

        return json.load(f)

def print_recipes(recipes):
    for recipe in recipes:
        print(f"\n▶ {recipe['title']} ({recipe['category']})")
        print("재료:", ", ".join(recipe["ingredients"]))
        print("방법:", recipe["instructions"])

# 실행 부분
if __name__ == "__main__":
    recipes = load_recipes()
    print_recipes(recipes)