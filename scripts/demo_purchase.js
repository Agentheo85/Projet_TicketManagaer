const SubmitBut = document.querySelector("form")

const Topage = (arg) => {
window.location.replace(`../pages/${arg}.html`);

}
function Prompted(event) {

  const dateValue = document.querySelector('#birthday').value
  const firstnameValue = document.querySelector('#first-name').value
  let DateArrar = dateValue.split("-");
  if (DateArrar[0] <= 1950 || DateArrar[0] > 2008){
    alert(`tu t'appelles ${firstnameValue} oh le prenom de zgeg `+"ouai ya un bleme mon frero la ta meme pas 18 ans ou t trop vieux en sah");
      event.preventDefault();

    return 
  }


console.log(dateValue)


}

SubmitBut.addEventListener("submit", Prompted);