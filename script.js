// ---------- Theme toggle (remembers choice) ----------
const themeBtn = document.getElementById("themeToggle");
if (localStorage.getItem("theme") === "light") document.body.classList.add("light");
themeBtn.addEventListener("click", () => {
  document.body.classList.toggle("light");
  localStorage.setItem("theme", document.body.classList.contains("light") ? "light" : "dark");
});

// ---------- Red flag spotter ----------
const flags = document.querySelectorAll(".flag");
const flagOutput = document.getElementById("flagOutput");
const flagBar = document.getElementById("flagBar");
const flagCount = document.getElementById("flagCount");
const found = new Set();

flags.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    flagOutput.textContent = btn.dataset.msg;
    btn.classList.add("found");
    found.add(i);
    flagBar.style.width = (found.size / flags.length) * 100 + "%";
    flagCount.textContent = `${found.size} of ${flags.length} red flags found`;
    if (found.size === flags.length) {
      flagCount.textContent += " - Great job, you spotted them all!";
    }
  });
});

// ---------- Quiz ----------
const questions = [
  {
    q: "You get an email from 'IT Support' asking for your password to fix your account. What do you do?",
    a: ["Reply with the password", "Ignore and report it to IT Security", "Click the link to check"],
    correct: 1,
    why: "IT will never ask for your password. Report it."
  },
  {
    q: "Which email address is most suspicious?",
    a: ["support@microsoft.com", "support@micros0ft-security.com", "noreply@microsoft.com"],
    correct: 1,
    why: "The zero in 'micros0ft' and the extra word give it away."
  },
  {
    q: "Before clicking a link in an email, you should...",
    a: ["Hover over it to preview the real address", "Click quickly before it expires", "Forward it to colleagues"],
    correct: 0,
    why: "Hovering reveals the true destination."
  }
];

let current = 0, score = 0;
const quizBox = document.getElementById("quizBox");

function showQuestion() {
  const item = questions[current];
  quizBox.innerHTML = `<p><b>Question ${current + 1}/${questions.length}</b></p><p>${item.q}</p>`;
  item.a.forEach((text, idx) => {
    const b = document.createElement("button");
    b.className = "opt";
    b.textContent = text;
    b.addEventListener("click", () => answer(idx, b));
    quizBox.appendChild(b);
  });
}

function answer(idx, btn) {
  const item = questions[current];
  const opts = quizBox.querySelectorAll(".opt");
  opts.forEach(o => (o.disabled = true));
  opts[item.correct].classList.add("right");
  if (idx === item.correct) score++; else btn.classList.add("wrong");
  const note = document.createElement("p");
  note.textContent = item.why;
  quizBox.appendChild(note);
  const next = document.createElement("button");
  next.className = "next";
  next.textContent = current < questions.length - 1 ? "Next" : "See score";
  next.addEventListener("click", () => {
    current++;
    current < questions.length ? showQuestion() : showScore();
  });
  quizBox.appendChild(next);
}

function showScore() {
  quizBox.innerHTML = `<h3>You scored ${score}/${questions.length}</h3>
    <p>${score === questions.length ? "Excellent! You're a human firewall." : "Review the tips above and try again."}</p>`;
  const again = document.createElement("button");
  again.className = "next";
  again.textContent = "Retry";
  again.addEventListener("click", () => { current = 0; score = 0; showQuestion(); });
  quizBox.appendChild(again);
}
showQuestion();

// ---------- Placement ----------
const placeOutput = document.getElementById("placeOutput");
document.querySelectorAll(".place").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".place").forEach(p => p.classList.remove("active"));
    btn.classList.add("active");
    placeOutput.textContent = btn.dataset.why;
  });
});