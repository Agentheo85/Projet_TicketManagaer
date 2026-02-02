const SubmitBut = document.querySelector("form")

const Topage = (arg) => {
window.location.replace(`../pages/${arg}`);

}
function Prompted(event) {
    let formData = new FormData(SubmitBut);

console.log(`Form Submitted! Timestamp: ${event.timeStamp}`)
console.log()    
for(let [name, value] of formData.values()) {
  alert(`${name} = ${value}`); // key1 = value1, ensuite key2 = value2
}
  event.preventDefault();
}

SubmitBut.addEventListener("submit", Prompted);