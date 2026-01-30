const SubmitBut = document.getElementsByTagName("form")[0]

function Prompted(event) {
console.log(`Form Submitted! Timestamp: ${event.timeStamp}`)
window.location.replace("../pages/purchased_sucessfull.html");

      event.preventDefault();
}

SubmitBut.addEventListener("submit", Prompted);