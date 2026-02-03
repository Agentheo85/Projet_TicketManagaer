const url = new URL(window.location.href) // on prend 
const mySearchParams = new URLSearchParams(url.search); // celui ci va prendre les parametres que le form a envoyer sous type d'url ( ?param1=caca&param2=arg)


console.log(url.search)
for (const [key, value] of mySearchParams) {
    console.log(key,value)
}



const convertDateToEuropean = (date) => {
    const dateArray = date.split('-')


    return `${dateArray[2]}/${dateArray[1]}/${dateArray[0]}`


}

/**
 * Function Init des qu'on est sur la page/charge .
 */
const initNotify = () => {
    const description = document.querySelector("#description")
    description.textContent = `Au nom de ${mySearchParams.get("last-name")} ${mySearchParams.get("first-name")}` // change le content de description et prend les params de l'url envoyer par le form
    const descriptionBirth = document.querySelector("#descriptionbirth")
    descriptionBirth.textContent = `Née le ${convertDateToEuropean(mySearchParams.get("birthday"))}` // la meme chose
}

initNotify()