document.addEventListener('DOMContentLoaded', () => {
    // Elements
    const cartCount = document.getElementById('cart-count');
    const cartModal = document.getElementById('cart-modal');
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    const closeCartBtn = document.getElementById('close-cart');
    const cartBtn = document.getElementById('cart-btn');
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const increaseButtons = document.querySelectorAll('.increase-quantity');
    const decreaseButtons = document.querySelectorAll('.decrease-quantity');

    // Initialize cart from localStorage
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Function to update cart count in UI
    function updateCartCount() {
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        cartCount.textContent = totalItems;
    }

    // Function to update cart total price
    function updateCartTotal() {
        const total = cart.reduce((sum, item) => sum + item.quantity * item.price, 0);
        cartTotal.textContent = `Rs. ${total.toFixed(2)}`;
    }

    // Function to render cart items in the cart modal
    function renderCartItems() {
        cartItems.innerHTML = '';
        cart.forEach(item => {
            const cartItem = document.createElement('div');
            cartItem.classList.add('cart-item');
            cartItem.innerHTML = `
                <span>${item.name}</span>
                <span>Rs. ${item.price}</span>
                <div class="cart-item-quantity">
                    <button class="cart-item-decrease" data-uid="${item.uid}">-</button>
                    <span>${item.quantity}</span>
                    <button class="cart-item-increase" data-uid="${item.uid}">+</button>
                </div>
                <button class="cart-item-remove" data-uid="${item.uid}">Remove</button>
            `;
            cartItems.appendChild(cartItem);
        });
        updateCartTotal();
    }

    // Function to save cart to localStorage
    function saveCart() {
        localStorage.setItem('cart', JSON.stringify(cart));
    }

    // Function to show cart message
    function showCartMessage(message, type) {
        const messageContainer = document.createElement('div');
        messageContainer.classList.add('cart-message', type);
        messageContainer.textContent = message;
        document.body.appendChild(messageContainer);

        setTimeout(() => {
            messageContainer.remove();
        }, 3000);
    }

    // Handle quantity increase buttons
    increaseButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productUid = button.dataset.product;
            const quantityDisplay = document.getElementById(`product-quantity-display-${productUid}`);
            let currentQuantity = parseInt(quantityDisplay.textContent);
            currentQuantity++;
            quantityDisplay.textContent = currentQuantity;
        });
    });

    // Handle quantity decrease buttons
    decreaseButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productUid = button.dataset.product;
            const quantityDisplay = document.getElementById(`product-quantity-display-${productUid}`);
            let currentQuantity = parseInt(quantityDisplay.textContent);
            if (currentQuantity > 1) {
                currentQuantity--;
                quantityDisplay.textContent = currentQuantity;
            }
        });
    });

    // Handle Add to Cart button click
    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productUid = button.dataset.product;
            const productName = button.dataset.name;
            const productPrice = parseFloat(button.dataset.price);
            
            // Get current quantity from display
            const quantityDisplay = document.getElementById(`product-quantity-display-${productUid}`);
            const quantity = parseInt(quantityDisplay.textContent);

            // Check if the product already exists in the cart
            const existingItemIndex = cart.findIndex(item => item.uid === productUid);
            
            if (existingItemIndex > -1) {
                // Update quantity of existing item
                cart[existingItemIndex].quantity += quantity;
            } else {
                // Add new product to cart
                cart.push({
                    uid: productUid,
                    name: productName,
                    price: productPrice,
                    quantity: quantity
                });
            }

            // Save updated cart to localStorage
            saveCart();

            // Update UI
            updateCartCount();
            showCartMessage(`${productName} (${quantity}) added to your cart!`, 'success');

            // Temporarily disable button
            button.textContent = 'Added';
            button.disabled = true;
            
            // Reset quantity display
            quantityDisplay.textContent = '1';

            setTimeout(() => {
                button.textContent = 'Add to Cart';
                button.disabled = false;
            }, 2000);
        });
    });

    // Handle cart modal interactions
    cartBtn.addEventListener('click', () => {
        cartModal.style.display = 'block';
        cartModal.style.visibility = 'visible';
        renderCartItems();
    });

    closeCartBtn.addEventListener('click', () => {
        cartModal.style.display = 'none';
        cartModal.style.visibility = 'hidden';
    });

    // Handle cart item quantity adjustments within the cart modal
    cartItems.addEventListener('click', (e) => {
        if (e.target.classList.contains('cart-item-increase')) {
            const uid = e.target.dataset.uid;
            const cartItem = cart.find(item => item.uid === uid);
            if (cartItem) {
                cartItem.quantity++;
                saveCart();
                renderCartItems();
            }
        }

        if (e.target.classList.contains('cart-item-decrease')) {
            const uid = e.target.dataset.uid;
            const cartItemIndex = cart.findIndex(item => item.uid === uid);
            if (cartItemIndex > -1) {
                if (cart[cartItemIndex].quantity > 1) {
                    cart[cartItemIndex].quantity--;
                } else {
                    cart.splice(cartItemIndex, 1);
                }
                saveCart();
                renderCartItems();
            }
        }

        if (e.target.classList.contains('cart-item-remove')) {
            const uid = e.target.dataset.uid;
            const cartItemIndex = cart.findIndex(item => item.uid === uid);
            if (cartItemIndex > -1) {
                cart.splice(cartItemIndex, 1);
                saveCart();
                renderCartItems();
            }
        }
    });

    // Initialize cart count on page load
    updateCartCount();
});



