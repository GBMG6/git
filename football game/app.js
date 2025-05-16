const teams = [
  { name: "맨체스터 시티", strength: 190 },
  { name: "맨체스터 유나이티트", strength: 120 },
  { name: "아스날", strength: 190 },
  { name: "토트넘", strength: 120 },
  { name: "리버풀", strength: 190 },
  { name: "첼시", strength: 160 },
  { name: "뉴캐슬", strength: 140 },
  { name: "아스톤 빌라", strength: 135 },
  { name: "노팅엄 포레스트", strength: 130 },
  { name: "브렌드포드", strength: 90 },
  { name: "입스위치 타운", strength: 30 },
  { name: "레스터 시티", strength: 40 },
  { name: "풀럼", strength: 80 },
  { name: "애버튼", strength: 70 },
  { name: "울버햄튼", strength: 60 },
  { name: "웨스트햄", strength: 70 },
  { name: "사우스햄튼", strength: 20 },
  { name: "본머스", strength: 85 },
  { name: "브라이튼", strength: 95 },
  { name: "크리스탈 팰리스", strength: 90 },
];

let gameMinute = 0;
let money = 1000;
let currentMatch = null;
let userBet = null;
let score1 = 0;
let score2 = 0;

const commentaryLines = [
  "{team}이(가) 중원에서 전개합니다.",
  "{team}이(가) 슈팅! 수비 맞고 나갑니다.",
  "{team}이(가) 크로스! 위협적입니다.",
  "{team}이(가) 압박합니다.",
  "{team}이(가) 드리블 돌파!"
];

function updateTimeline(minute) {
  document.getElementById("timeline-time").innerText = `${minute}'`;
  const percent = Math.floor((minute / 90) * 100);
  document.getElementById("timeline-progress").style.width = `${percent}%`;
}

function updateMoneyDisplay() {
  document.getElementById("money").innerText = money;
}

function getOdds(team1, team2) {
  const total = team1.strength + team2.strength;
  const odds1 = (total / team1.strength).toFixed(2);
  const odds2 = (total / team2.strength).toFixed(2);
  return [parseFloat(odds1), parseFloat(odds2)];
}

function prepareMatch() {
  const team1 = teams[Math.floor(Math.random() * teams.length)];
  let team2;
  do {
    team2 = teams[Math.floor(Math.random() * teams.length)];
  } while (team1.name === team2.name);

  const [odds1, odds2] = getOdds(team1, team2);
  currentMatch = { team1, team2, odds: [odds1, odds2] };

  document.getElementById("matchup").innerText = `${team1.name} vs ${team2.name}`;
  document.getElementById("odds").innerText = `${team1.name}: ${odds1} / ${team2.name}: ${odds2}`;
  document.getElementById("scoreboard").innerText = "0 : 0";
  document.getElementById("betting-status").innerText = '';
  document.getElementById("result").innerText = '';
  document.getElementById("commentary-log").innerText = '';

  const select = document.getElementById("bet-team");
  select.innerHTML = `
    <option value="${team1.name}">${team1.name}</option>
    <option value="${team2.name}">${team2.name}</option>
  `;

  score1 = 0;
  score2 = 0;
}

function placeBet() {
  const amount = parseInt(document.getElementById("bet-amount").value);
  const team = document.getElementById("bet-team").value;

  if (isNaN(amount) || amount <= 0 || amount > money) {
    document.getElementById("betting-status").innerText = "금액이 잘못됐습니다.";
    return;
  }

  userBet = { amount, team };
  document.getElementById("betting-status").innerText = `${team}팀에 ${amount}원 배팅 완료!`;
  simulateMatch();
}

function simulateMatch() {
  const team1 = currentMatch.team1;
  const team2 = currentMatch.team2;

  score1 = 0;
  score2 = 0;
  updateScoreboard();
  document.getElementById("result").innerText = '';
  document.getElementById("commentary-log").innerText = '';
  gameMinute = 0;
  updateTimeline(gameMinute);

  let seconds = 0;
  const maxSeconds = 10;

  const interval = setInterval(() => {
    if (seconds >= maxSeconds) {
      clearInterval(interval);

      const log = document.getElementById("commentary-log");
      const end = document.createElement("p");
      end.innerText = "🔚 경기 종료!";
      end.style.color = "gray";
      log.appendChild(end);

      let result;
      if (score1 > score2) result = team1.name;
      else if (score2 > score1) result = team2.name;
      else result = "무승부";

      document.getElementById("result").innerText = `결과: ${result}`;
      settleBet(result);
      return;
    }

    gameMinute += 9;
    updateTimeline(gameMinute);

    const randTeam = Math.random() < 0.5 ? team1 : team2;
    const chance = Math.random();

    if (chance < 0.2) {
      generateGoalCommentary(randTeam);
      if (randTeam === team1) score1++;
      else score2++;
      updateScoreboard();
    } else {
      generateCommentary(team1, team2);
    }

    moveBallRandomly();
    seconds++;
  }, 1000);
}

function generateCommentary(team1, team2) {
  const log = document.getElementById("commentary-log");
  const team = Math.random() < 0.5 ? team1.name : team2.name;
  const line = commentaryLines[Math.floor(Math.random() * commentaryLines.length)].replace("{team}", team);
  const p = document.createElement("p");
  p.innerText = `⏱️ ${gameMinute}' - ${line}`;
  log.appendChild(p);
  log.scrollTop = log.scrollHeight;
}

function generateGoalCommentary(team) {
  const log = document.getElementById("commentary-log");
  const p = document.createElement("p");
  p.innerText = `⚽ ${gameMinute}' - ${team.name} 골입니다!!!`;
  p.style.color = "gold";
  p.style.fontWeight = "bold";
  log.appendChild(p);
  log.scrollTop = log.scrollHeight;
}

function updateScoreboard() {
  document.getElementById("scoreboard").innerText = `${score1} : ${score2}`;
}

function moveBallRandomly() {
  const ball = document.getElementById("ball");
  const randomPercent = Math.floor(Math.random() * 80) + 10;
  ball.style.left = `${randomPercent}%`;
}

function settleBet(winner) {
  if (!userBet) return;
  if (winner === "무승부") {
    alert("무승부로 환급됩니다.");
    return;
  }

  const winnerIndex = currentMatch.team1.name === winner ? 0 : 1;
  const odds = currentMatch.odds[winnerIndex];

  if (userBet.team === winner) {
    const winAmount = Math.floor(userBet.amount * odds);
    money += winAmount;
    alert(`${userBet.team}이 승리! ${winAmount}원 획득!`);
  } else {
    money -= userBet.amount;
    alert(`${userBet.team}이 패배. ${userBet.amount}원 손실.`);
  }

  updateMoneyDisplay();
  userBet = null;
  setTimeout(prepareMatch, 3000);
}

// 초기화
updateMoneyDisplay();
prepareMatch();
