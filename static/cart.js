function isValidCartItem(item) {
    return item && typeof item.quantity === 'number' && item.quantity > 0;
}

function getCurrentQuantity() {
    const quantityDisplay = document.getElementById('quantity-display');
    if (!quantityDisplay || isNaN(parseInt(quantityDisplay.textContent, 10))) {
        console.error("Quantity display element is missing or not a valid number");
        return 1;
    }
    return parseInt(quantityDisplay.textContent, 10);
}

function addToCart(productName, price = 0) {
    const quantity = getCurrentQuantity();
    if (isNaN(quantity) || quantity <= 0) {
        console.error("Invalid quantity for product:", quantity);
        return;
    }

    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    const cartKey = `${productName}|${price}`;

    if (!cartKey || quantity <= 0) {
        console.warn("Invalid cart item data:", { cartKey, quantity });
        return;
    }

    if (!cart[cartKey]) {
        cart[cartKey] = {
            name: productName,
            quantity: quantity,
            price: price
        };
    } else {
        cart[cartKey].quantity += quantity;
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartDisplay();
    showAddToCartSuccessMessage(productName);
}

function updateCartDisplay() {
    const cart = JSON.parse(localStorage.getItem('cart')) || {};
    let totalItems = 0;
    const cartItemsContainer = document.getElementById('cart-items');
    let total = 0;

    if (cartItemsContainer) {
        cartItemsContainer.innerHTML = '';
        for (const cartKey in cart) {
            const item = cart[cartKey];
            if (isValidCartItem(item)) {
                totalItems += item.quantity;
                const itemTotal = item.price * item.quantity;
                total += itemTotal;
                cartItemsContainer.innerHTML += `
                    <div class="cart-item">
                        <span class="cart-item-name">${item.name}</span>
                        <div class="cart-item-controls">
                            <button class="cart-quantity-btn minus" data-product="${item.name}">-</button>
                            <span class="cart-item-quantity">${item.quantity}</span>
                            <button class="cart-quantity-btn plus" data-product="${item.name}">+</button>
                        </div>
                        <span class="cart-item-price">Rs.${itemTotal.toFixed(2)}</span>
                        <button class="remove-item" data-product="${item.name}">Remove</button>
                    </div>
                `;
            } else {
                console.warn("Invalid cart item encountered while updating count", item);
            }
        }
    }

    const cartCountElement = document.getElementById('cart-count');
    if (cartCountElement) {
        cartCountElement.innerText = totalItems;
    }

    const cartTotalElement = document.getElementById('cart-total');
    if (cartTotalElement) {
        cartTotalElement.textContent = `Rs.${total.toFixed(2)}`;
    }

    addCartEventListeners();
}

function addCartEventListeners() {
    document.querySelectorAll('.cart-quantity-btn').forEach(button => {
        button.addEventListener('click', () => {
            const productName = button.getAttribute('data-product');
            let cart = JSON.parse(localStorage.getItem('cart')) || {};
            const cartKey = Object.keys(cart).find(key => cart[key].name === productName);
            if (cartKey) {
                if (button.classList.contains('minus')) {
                    cart[cartKey].quantity = Math.max(cart[cartKey].quantity - 1, 1);
                } else if (button.classList.contains('plus')) {
                    cart[cartKey].quantity++;
                }
                localStorage.setItem('cart', JSON.stringify(cart));
                updateCartDisplay();
            }
        });
    });

    document.querySelectorAll('.remove-item').forEach(button => {
        button.addEventListener('click', () => {
            const productName = button.getAttribute('data-product');
            removeFromCart(productName);
            updateCartDisplay();
        });
    });
}

function showAddToCartSuccessMessage(productName) {
    const successMessage = document.getElementById('success-message');
    const successText = document.getElementById('success-text');
    if (successMessage && successText) {
        successText.textContent = `${productName} added to cart successfully!`;
        successMessage.style.display = 'block';
        successMessage.style.opacity = '1';
        successMessage.style.transform = 'translate(-50%, -50%) scale(1)';
        setTimeout(() => {
            closeSuccessMessage();
        }, 3000);
    }
}

function closeSuccessMessage() {
    const successMessage = document.getElementById('success-message');
    if (successMessage) {
        successMessage.style.opacity = '0';
        successMessage.style.transform = 'translate(-50%, -50%) scale(0.9)';
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 300);
    }
}

function removeFromCart(productName) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    const cartKey = Object.keys(cart).find(key => cart[key].name === productName);
    if (cartKey) {
        delete cart[cartKey];
        localStorage.setItem('cart', JSON.stringify(cart));
    }
}

document.addEventListener('DOMContentLoaded', function() {
    updateCartDisplay();
});