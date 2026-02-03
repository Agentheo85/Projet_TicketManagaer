const SubmitBut = document.querySelector("form")

const Topage = (arg) => {
window.location.replace(`../pages/${arg}.html`);

}
function Prompted(event) {

  const dateValue = document.querySelector('#birthday').value
  const firstnameValue = document.querySelector('#first-name').value
  const lastnameValue = document.querySelector('#last-name').value

  let DateArrar = dateValue.split("-");
  if (DateArrar[0] <= 1950 || DateArrar[0] > 2008){
    alert(`tu t'appelles ${firstnameValue} oh le prenom de zgeg `+"ouai ya un bleme mon frero la ta meme pas 18 ans ou t trop vieux en sah");
      event.preventDefault();

    return 
  }


fetch("http://localhost:3000/Clients",{    
    method: "POST",
    body: JSON.stringify({"first-name":firstnameValue,"last-name":lastnameValue,"Created-at":Date.now(),"birthday":dateValue,"TicketId":"ddd"}),
    headers: {
      "Content-Type": "application/json",
    }
  })
console.log(dateValue)


}

SubmitBut.addEventListener("submit", Prompted);