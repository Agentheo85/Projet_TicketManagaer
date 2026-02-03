let dataStats = undefined


const totalIncome = () => {
    return dataStats.Purchased_Tickets * dataStats.Ticket_Price
}

const RemainingTicket = () => {
    return dataStats.Max_Tickets -  dataStats.Purchased_Tickets 
}

const Init = () => {
    console.log(dataStats)
    const CardRemaining = document.querySelector("#Remaining_Place")
    CardRemaining.getElementsByTagName('h2')[0].textContent = RemainingTicket()
    const CardPurchased = document.querySelector("#Purchased_Place")
    CardPurchased.getElementsByTagName('h2')[0].textContent = dataStats.Purchased_Tickets
    const CardTotalIncome = document.querySelector("#Total_Income")
    CardTotalIncome.getElementsByTagName('h2')[0].textContent = totalIncome()+"€"
}


fetch("http://localhost:3000/Stats")
    .then(data=>{

      return data.json()
    })
    .then(data=>{
        dataStats = data
        Init()
    })

