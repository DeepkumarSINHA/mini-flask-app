const btn = document.getElementById("btn");
const out = document.getElementById("out");

btn.addEventListener("click", async () => {
  try {
    const res = await fetch("/api/message");
    const data = await res.json();
    out.textContent = data.msg;
  } catch (err) {
    console.error(err);
    out.textContent = "Error talking to backend";
  }
});
