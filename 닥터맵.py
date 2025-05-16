import requests
# 증상 → 진료과 매핑
symptom_to_department = {
    "두통": "신경과",
    "복통": "내과",
    "피부 발진": "피부과",
    "관절 통증": "정형외과",
    "눈 충혈": "안과",
    "치통": "치과",
    "기침": "호흡기내과"
}

# 위치 자동 감지
def get_user_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        lat, lon = data['loc'].split(",")
        print(f"[] 현재 위치: 위도 {lat}, 경도 {lon}")
        return lat, lon
    except Exception as e:
        print("위치 정보를 가져올 수 없습니다.", e)
        return None, None

# 주변 병원 검색
def find_hospitals(lat, lon, department):
    API_KEY = "YOUR_GOOGLE_API_KEY"  # <-- 여기에 본인 Google Maps API 키 입력
    search_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lon}",
        "radius": 30000,  # 3km 반경
        "keyword": department,
        "type": "hospital",
        "key": API_KEY
    }

    try:
        res = requests.get(search_url, params=params)
        places = res.json().get("results", [])

        if not places:
            print("근처에 해당 진료과 병원이 없습니다.")
            return

        print(f"\n 근처 {department} 병원 목록:")
        for place in places[:5]:
            name = place.get("name")
            address = place.get("vicinity")
            rating = place.get("rating", "N/A")
            print(f"- {name} ({address}) ★ {rating}")
    except Exception as e:
        print("병원 정보를 불러올 수 없습니다.", e)

# 메인 로직
def main():
    symptom = input("어디가 아프신가요? (예: 두통, 복통, 피부 발진): ").strip()

    department = symptom_to_department.get(symptom)
    if not department:
        print("죄송합니다. 해당 증상에 대한 진료과 정보가 없습니다.")
        return

    print(f"추천 진료과: {department}")

    lat, lon = get_user_location()
    if not lat or not lon:
        return

    find_hospitals(lat, lon, department)

if __name__ == "__main__":
    main()
