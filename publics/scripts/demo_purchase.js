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

    return 
  }
data = {"first-name":firstnameValue,"last-name":lastnameValue,"Created-at":Date.now(),"birthday":dateValue,"TicketId":"ddd"}
fetch("http://localhost:5000/api/newticket",{    
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    }
  }).then((response) => response.json())
  .then((json) => {   console.log('reussi')

        window.location.href = `../pages/purchased_sucessfull.html?last-name=${data["last-name"]}&first-name=${data["first-name"]}&birthday=${data["birthday"]}&id=${json.id}`;
});
 
console.log(dateValue)

      event.preventDefault();

}

SubmitBut.addEventListener("submit", Prompted);