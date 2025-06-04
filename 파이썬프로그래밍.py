import requests
from urllib.parse import quote
from tkinter import *

def fetch_recipe_from_api(recipe_name):
    encoded_name = quote(recipe_name)
    url = f"http://openapi.foodsafetykorea.go.kr/api/sample/COOKRCP01/json/1/5/RCP_NM={encoded_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rows = data.get('COOKRCP01', {}).get('row', [])

        if not rows:
            return ["❌ 해당 요리를 찾을 수 없습니다."]

        results = []
        for r in rows:
            name = r.get('RCP_NM', '이름 없음')
            parts = r.get('RCP_PARTS_DTLS', '재료 정보 없음')
            manual = [r.get(f'MANUAL{str(i).zfill(2)}', '') for i in range(1, 21)]
            manual = [step.strip() for step in manual if step.strip()]
            manual_text = "\n".join([f"{idx+1}. {step}" for idx, step in enumerate(manual)])
            result = f"🍽️ {name}\n\n🛒 재료:\n{parts}\n\n👩‍🍳 조리법:\n{manual_text}"
            results.append(result)

        return results

    except requests.RequestException as e:
        return [f"🚨 API 요청 중 오류 발생: {e}"]

def search_and_display():
    recipe_name = entry.get()
    output.delete(1.0, END)
    if not recipe_name.strip():
        output.insert(END, "⚠️ 검색어를 입력하세요.")
        return
    result = fetch_recipe_from_api(recipe_name)
    for r in result:
        output.insert(END, r + "\n\n" + "-"*50 + "\n\n")

# GUI 구성
root = Tk()
root.title("🍜 한식 레시피 검색기")
root.geometry("650x700")

label = Label(root, text="찾고 싶은 요리명을 입력하세요:", font=("Arial", 12))
label.pack(pady=10)

entry = Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

search_btn = Button(root, text="레시피 검색", command=search_and_display, font=("Arial", 12))
search_btn.pack(pady=5)

output = Text(root, width=80, height=30, font=("Arial", 11))
output.pack(pady=10)

root.mainloop()
