function submitQuestion() {
  const question = document.getElementById("question").value;
  const loader = document.getElementById("loader");
  const answerDiv = document.getElementById("answer");

  loader.classList.remove("hidden");
  answerDiv.innerHTML = "";

  fetch("/ask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question: question })
  })
    .then(response => response.json())
    .then(data => {
      loader.classList.add("hidden");
      answerDiv.innerHTML = `<strong>Answer:</strong> ${data.answer}`;
    })
    .catch(error => {
      loader.classList.add("hidden");
      answerDiv.innerHTML = "Something went wrong.";
    });
}
