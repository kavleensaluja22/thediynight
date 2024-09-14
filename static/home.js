document.addEventListener('DOMContentLoaded', () => {
    updateCartDisplay();

    document.querySelectorAll('.quantity').forEach(quantityElement => {
        if (!quantityElement.textContent.trim()) {
            quantityElement.textContent = '1';
        }
    });

    document.querySelectorAll('.quantity-btn').forEach(button => {
        button.addEventListener('click', () => {
            const productName = button.getAttribute('data-product');
            const quantityElement = document.querySelector(`.quantity[data-product='${productName}']`);
            let quantity = parseInt(quantityElement.textContent);

            if (button.classList.contains('minus')) {
                quantity = Math.max(quantity - 1, 1);
            } else if (button.classList.contains('plus')) {
                quantity++;
            }

            quantityElement.textContent = quantity;
        });
    });

    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', () => {
            const productName = button.getAttribute('data-product');
            const price = parseFloat(button.getAttribute('data-price'));
            const quantityElement = document.querySelector(`.quantity[data-product='${productName}']`);
            const quantity = parseInt(quantityElement.textContent);

            if (quantity > 0) {
                addToCart(productName, price, quantity);
                updateCartDisplay();
                quantityElement.textContent = '1';
            }
        });
    });

    const cartBtn = document.getElementById('cart-btn');
    const cartModal = document.getElementById('cart-modal');
    const closeCartBtn = document.getElementById('close-cart');

    if (cartBtn && cartModal && closeCartBtn) {
        cartBtn.addEventListener('click', () => {
            cartModal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        });

        closeCartBtn.addEventListener('click', () => {
            cartModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    }
});

function addToCart(productName, price, quantity) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    const cartKey = `${productName}|${price}`;

    if (cart[cartKey]) {
        cart[cartKey].quantity += quantity;
    } else {
        cart[cartKey] = { name: productName, price, quantity };
    }

    localStorage.setItem('cart', JSON.stringify(cart));
}

function updateCartDisplay() {
    const cartItemsContainer = document.getElementById('cart-items');
    const cart = JSON.parse(localStorage.getItem('cart')) || {};
    let total = 0;

    if (cartItemsContainer) {
        cartItemsContainer.innerHTML = '';
        for (const cartKey in cart) {
            const item = cart[cartKey];
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
        }

        const cartTotalElement = document.getElementById('cart-total');
        if (cartTotalElement) {
            cartTotalElement.textContent = `Rs.${total.toFixed(2)}`;
        }

        addCartEventListeners();
    }

    updateCartCount();
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || {};
    const totalItems = Object.values(cart).reduce((sum, item) => sum + item.quantity, 0);
    const cartCountElement = document.getElementById('cart-count');
    if (cartCountElement) {
        cartCountElement.textContent = totalItems;
    }
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

function removeFromCart(productName) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    const cartKey = Object.keys(cart).find(key => cart[key].name === productName);
    if (cartKey) {
        delete cart[cartKey];
        localStorage.setItem('cart', JSON.stringify(cart));
    }
}