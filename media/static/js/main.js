let prices = document.getElementsByClassName('price');

// This code change price format.
for (let i = 0; i < prices.length; i++) {
    prices[i].textContent = new Intl.NumberFormat('ru-RU').format(Number(prices[i].innerHTML)) + ' Р';
}

// 
// Нужно сделать приемлемый формат числа.
// 