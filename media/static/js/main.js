let prices = document.getElementsByClassName('price');

// This code change price format.
for (let i = 0; i < prices.length; i++) {
    prices[i].textContent = new Intl.NumberFormat('ru-RU').format(Number(prices[i].innerHTML)) + ' Р';
}

function openForm() {
    document.getElementsByClassName("autorization-form")[0].style.display = "block";
}

function closeForm() {
    // getELementById is better in this part of code.
    document.getElementsByClassName("autorization-form")[0].style.display = "none";
}
