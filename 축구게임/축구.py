import pygame
import random
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("가상 축구 시뮬레이터")
font = pygame.font.SysFont("malgungothic", 24)
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
GREEN = (20, 120, 20)

# 팀 클래스
class Team:
    def __init__(self, name, power):
        self.name = name
        self.power = power

# 경기 결과 시뮬레이션
def simulate_match(team1, team2):
    goals1 = 0
    goals2 = 0
    events = []  # 경기 중 일어나는 이벤트 저장
    
    # 90분 동안 경기가 진행되는 동안
    for minute in range(1, 91):  # 90분 동안 경기 진행
        if random.random() < 0.01 * team1.power:  # 첫 번째 팀 골
            goals1 += 1
            events.append(f"({minute}분) {team1.name} 골!")
        if random.random() < 0.01 * team2.power:  # 두 번째 팀 골
            goals2 += 1
            events.append(f"({minute}분) {team2.name} 골!")

    return goals1, goals2, events

# 20팀 생성
teams = [
    Team("서울 FC", 0.8),
    Team("부산 다이너마이트", 0.75),
    Team("대전 유나이티드", 0.7),
    Team("인천 피닉스", 0.65),
    Team("광주 타이거즈", 0.72),
    Team("울산 호랑이", 0.77),
    Team("제주 유나이티드", 0.74),
    Team("수원 블루윙즈", 0.76),
    Team("포항 스틸러스", 0.69),
    Team("강원 FC", 0.73),
    Team("전북 현대", 0.8),
    Team("경남 FC", 0.66),
    Team("시흥시청", 0.68),
    Team("경기도 FC", 0.7),
    Team("용인 FC", 0.69),
    Team("안양 FC", 0.72),
    Team("대구 FC", 0.75),
    Team("창원 FC", 0.71),
    Team("청주 FC", 0.67)
]

# 랜덤 매칭을 위한 함수
def get_random_match():
    team1, team2 = random.sample(teams, 2)  # 2팀을 랜덤으로 뽑기
    return team1, team2

# 그리기 함수
def draw_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))

# "나가기" 버튼 클릭 이벤트 처리 함수
def draw_quit_button():
    quit_button = pygame.Rect(WIDTH - 150, HEIGHT - 50, 140, 40)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    draw_text("나가기", WIDTH - 120, HEIGHT - 40)
    return quit_button

# 메인 루프
running = True
previous_match = None  # 이전 경기 결과를 저장할 변수
next_match = None  # 다음 경기 대진을 저장할 변수
first_match = True  # 첫 번째 경기를 구분하는 변수

while running:
    screen.fill(GREEN)
    clock.tick(1)  # 1초에 한 번씩 화면을 업데이트
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 나가기 버튼 클릭 시 종료
            if quit_button.collidepoint(event.pos):
                running = False  # 게임 루프 종료

    # 랜덤으로 2팀을 매칭하여 경기 시작
    if next_match is None:
        team1, team2 = get_random_match()
    else:
        team1, team2 = next_match

    goals1, goals2, events = simulate_match(team1, team2)

    # 경기 중계 및 점수 표시
    draw_text(f"{team1.name}: {goals1} - {goals2} :{team2.name}", WIDTH // 2 - 150, 20)
    
    # 경기 중 이벤트 표시
    y_offset = 60
    for event_text in events:
        draw_text(event_text, 20, y_offset)
        y_offset += 30  # 다음 이벤트 위치

    # 이전 경기 결과와 다음 경기 대진을 카운트다운 화면에 표시
    countdown_time = 60 if not first_match else 0  # 첫 번째 경기는 1분 기다리지 않음
    first_match = False  # 첫 번째 경기 후에는 1분 대기
    
    while countdown_time > 0:
        screen.fill(GREEN)
        
        # 이전 경기 결과와 팀 이름
        if previous_match:
            team1_name, team2_name, goals1, goals2 = previous_match
            draw_text(f"이전 경기: {team1_name} {goals1} : {goals2} {team2_name}", WIDTH // 2 - 150, HEIGHT // 2 - 40)
        
        # 다음 경기 대진 표시
        draw_text(f"다음 경기: {team1.name} vs {team2.name}", WIDTH // 2 - 150, HEIGHT // 2)
        
        # 카운트다운 표시
        draw_text(f"다음 경기 시작까지: {countdown_time}초", WIDTH // 2 - 150, HEIGHT // 2 + 40)

        # 나가기 버튼 그리기
        quit_button = draw_quit_button()

        pygame.display.update()
        pygame.time.wait(1000)  # 1초 대기
        countdown_time -= 1  # 카운트 1초씩 감소

    # 이전 경기 결과 업데이트
    previous_match = (team1.name, team2.name, goals1, goals2)

    # 다음 경기 대진 랜덤 설정
    next_match = get_random_match()

    pygame.display.update()

# 게임 종료 처리
pygame.quit()
sys.exit()  # 종료 후 시스템 종료
