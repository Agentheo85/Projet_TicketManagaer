const SubmitBut = document.querySelector("form")

const Topage = (arg) => {
window.location.replace(`../pages/${arg}`);

}
function Prompted(event) {
  const dateValue = document.querySelector('#birthday').value
  let DateArrar = dateValue.split("-");
  if (DateArrar[0] >= 1950 && DateArrar[0] <= 2008){

  }


console.log(`Form Submitted! Timestamp: ${event.timeStamp}`)
console.log(date.value)
event.preventDefault();

}

SubmitBut.addEventListener("submit", Prompted);