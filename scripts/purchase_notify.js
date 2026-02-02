const url = new URL(window.location.href) // on prend 
const mySearchParams = new URLSearchParams(url.search); // celui ci va prendre les parametres que le form a envoyer sous type d'url ( ?param1=caca&param2=arg)


console.log(url.search)
for (const [key, value] of mySearchParams) {
    console.log(key,value)
}

const description = document.querySelector("#description")
description.textContent = `Au nom de ${mySearchParams.get("last-name")} ${mySearchParams.get("first-name")}`
const descriptionBirth = document.querySelector("#descriptionbirth")

const convertDateToEuropean = (date) => {
    const dateArray = date.split('-')


    return `${dateArray[2]}/${dateArray[1]}/${dateArray[0]}`


}

descriptionBirth.textContent = `Née le ${convertDateToEuropean(mySearchParams.get("birthday"))}`