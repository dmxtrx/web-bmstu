let products = [];
let cart = {};

function addProduct() {
    let name = prompt('введите название:');
    let price = parseFloat(prompt('введите цену:'));
    if (name && !isNaN(price) && price > 0) {
        products.push({ name, price });
        alert('товар добавлен');
    } else {
        alert('неккоректные данные');
    }
}

function addToCart() {
    if (products.length === 0) {
        alert('нет доступных товаров');
        return;
    }
    let list = 'товары:\n';
    products.forEach((p, i) => list += `${i+1}. ${p.name} - ${p.price}\n`);
    let idx = parseInt(prompt(list + 'введите номер товара:')) - 1;
    if (idx >= 0 && idx < products.length) {
        let name = products[idx].name;
        let qty = parseInt(prompt('введите количество:'));
        if (!isNaN(qty) && qty > 0) {
            cart[name] = (cart[name] || 0) + qty;
            alert('добавлено в корзину');
        } else {
            alert('неверное количество');
        }
    } else {
        alert('неверный номер');
    }
}

function removeFromCart() {
    let items = Object.keys(cart);
    if (items.length === 0) {
        alert('корзина пуста');
        return;
    }
    let list = 'корзина:\n';
    items.forEach((name, i) => list += `${i+1}. ${name} - ${cart[name]}\n`);
    let idx = parseInt(prompt(list + 'введите номер товара для удаления:')) - 1;
    if (idx >= 0 && idx < items.length) {
        let name = items[idx];
        cart[name]--;
        if (cart[name] <= 0) delete cart[name];
        alert('товар удалён');
    } else {
        alert('неверный номер');
    }
}

function totalCost() {
    let total = 0;
    for (let name in cart) {
        let product = products.find(p => p.name === name);
        if (product) total += product.price * cart[name];
    }
    alert(`общая стоимость: ${total}`);
}

function showMenu() {
    let choice;
    do {
        choice = prompt(
            "меню:\n1. добавить товар\n2. добавить в корзину\n3. удалить из корзины\n4. итоговая стоимость\n5. выход"
        );
        switch (choice) {
            case '1': addProduct(); break;
            case '2': addToCart(); break;
            case '3': removeFromCart(); break;
            case '4': totalCost(); break;
            case '5': alert('выход'); break;
            default: alert('неверный пункт');
        }
    } while (choice !== '5');
}

showMenu();