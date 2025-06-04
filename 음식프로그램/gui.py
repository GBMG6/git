import tkinter as tk
import json
import re

# 레시피 불러오기
def load_recipes():
    with open("recipes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def show_recipes_by_category(event):
    selected_index = category_listbox.curselection()
    if not selected_index:
        return
    category = categories[selected_index[0]]
    filtered = [r for r in recipes if r["category"] == category]
    update_recipe_list(filtered)

def update_recipe_list(filtered_recipes):
    global current_recipes
    current_recipes = filtered_recipes
    recipe_listbox.delete(0, tk.END)
    for r in filtered_recipes:
        recipe_listbox.insert(tk.END, r["title"])

def show_recipe(event):
    selected_index = recipe_listbox.curselection()
    if not selected_index:
        return
    recipe = current_recipes[selected_index[0]]
    title_var.set(recipe["title"])
    category_var.set(f"({recipe['category']})")
    ingredients_text.delete("1.0", tk.END)
    instructions_text.delete("1.0", tk.END)
    ingredients_text.insert(tk.END, "\n".join(recipe["ingredients"]))

    formatted_instructions = re.sub(r"\s*(\d+\.)", r"\n\n\1", recipe["instructions"])
    instructions_text.insert(tk.END, formatted_instructions.strip())

# 창 초기 설정
root = tk.Tk()
root.title("레시피북")
root.geometry("870x780")
root.resizable(False,False)

recipes = load_recipes()
categories = sorted(set(r["category"] for r in recipes))
current_recipes = []

# ▶ 좌측: 카테고리 목록
tk.Label(root, text="카테고리", font=("Arial", 20)).place(x=20, y=24)
category_listbox = tk.Listbox(root, height=6, width=20, font=("Arial", 18))
category_listbox.place(x=20, y=60)
for c in categories:
    category_listbox.insert(tk.END, c)
category_listbox.bind("<<ListboxSelect>>", show_recipes_by_category)

# ▶ 음식 목록 + 스크롤
tk.Label(root, text="음식 목록", font=("Arial", 20)).place(x=20, y=220)
recipe_listbox = tk.Listbox(root, height=21, width=20, font=("Arial", 18))
recipe_listbox.place(x=20, y=260)
recipe_scrollbar = tk.Scrollbar(root)
recipe_scrollbar.place(x=245, y=260, height=460)
recipe_listbox.config(yscrollcommand=recipe_scrollbar.set)
recipe_scrollbar.config(command=recipe_listbox.yview)
recipe_listbox.bind("<<ListboxSelect>>", show_recipe)

# ▶ 제목 + 카테고리
title_var = tk.StringVar()
category_var = tk.StringVar()
tk.Label(root, textvariable=title_var, font=("Arial", 28, "bold")).place(x=300, y=17)
tk.Label(root, textvariable=category_var, font=("Arial", 18)).place(x=300, y=52)

# ▶ 재료 + 스크롤바
tk.Label(root, text="재료", font=("Arial", 20)).place(x=300, y=80)
ingredients_text = tk.Text(root, height=11, width=45, font=("Arial", 16))
ingredients_text.place(x=300, y=110)
ingredients_scrollbar = tk.Scrollbar(root)
ingredients_scrollbar.place(x=710, y=115, height=195)
ingredients_text.config(yscrollcommand=ingredients_scrollbar.set)
ingredients_scrollbar.config(command=ingredients_text.yview)

# ▶ 조리 방법 + 스크롤바
tk.Label(root, text="조리 방법", font=("Arial", 20)).place(x=300, y=320)
instructions_text = tk.Text(root, height=20, width=60, font=("Arial", 16))
instructions_text.place(x=300, y=360)
instructions_scrollbar = tk.Scrollbar(root)
instructions_scrollbar.place(x=835, y=365, height=360)
instructions_text.config(yscrollcommand=instructions_scrollbar.set)
instructions_scrollbar.config(command=instructions_text.yview)

# 실행
root.mainloop()