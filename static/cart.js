// Function to open the cart modal and display updated cart items
function openCartModal() {
    const cartModal = document.getElementById('cartModal');
    if (cartModal) {
        updateCartDisplay();  // Ensure cart is updated before displaying modal
        cartModal.style.display = 'block';
    }
}

// Function to close the cart modal
function closeCartModal() {
    const cartModal = document.getElementById('cartModal');
    if (cartModal) {
        cartModal.style.display = 'none';
    }
}

// Initialize variables for selected color and size
let selectedColor = localStorage.getItem('selectedColor') || '';
let selectedSize = localStorage.getItem('selectedSize') || '';
let cart = JSON.parse(localStorage.getItem('cart')) || {};

// Function to select a color
function selectColor(button) {
    const colorButtons = document.querySelectorAll('button[data-color]');
    colorButtons.forEach(btn => btn.classList.remove('selected')); // Remove previous selection
    selectedColor = button.dataset.color;
    localStorage.setItem('selectedColor', selectedColor);
    button.classList.add('selected'); // Add selection to the current button
    updatePrice();
    console.log(`Color selected: ${selectedColor}`);
}

// Function to select a size
function selectSize(button) {
    const sizeButtons = document.querySelectorAll('button[data-size]');
    sizeButtons.forEach(btn => btn.classList.remove('selected')); // Remove previous selection
    selectedSize = button.dataset.size;
    localStorage.setItem('selectedSize', selectedSize);
    button.classList.add('selected'); // Add selection to the current button
    updatePrice();
    console.log(`Size selected: ${selectedSize}`);
}

// Function to update the price based on selected color and size
function updatePrice() {
    const priceDisplay = document.getElementById('product-price');
    const basePriceElement = document.getElementById('base-price');

    if (!priceDisplay || !basePriceElement) {
        console.error('Price display or base price element not found');
        return;
    }

    const basePrice = parseFloat(basePriceElement.textContent.replace('Rs.', '').trim());
    let additionalPrice = 0;

    if (selectedColor) {
        const colorButton = document.querySelector(`button[data-color="${selectedColor}"]`);
        if (colorButton) {
            additionalPrice += parseFloat(colorButton.dataset.price) || 0;
        }
    }

    if (selectedSize) {
        const sizeButton = document.querySelector(`button[data-size="${selectedSize}"]`);
        if (sizeButton) {
            additionalPrice += parseFloat(sizeButton.dataset.price) || 0;
        }
    }

    const totalPrice = basePrice + additionalPrice;
    priceDisplay.textContent = `Rs.${totalPrice.toFixed(2)}`;
}

// Function to initialize and update quantity display
function updateQuantityDisplay() {
    const quantitySpan = document.getElementById('quantity-display');
    if (quantitySpan) {
        const savedQuantity = localStorage.getItem('quantity') || '1';
        quantitySpan.textContent = savedQuantity; // Load saved quantity or set default to 1
    }
}

// Function to increase quantity
function increaseQuantity() {
    const quantitySpan = document.getElementById('quantity-display');
    if (quantitySpan) {
        let currentQuantity = parseInt(quantitySpan.textContent, 10);
        if (!isNaN(currentQuantity)) {
            currentQuantity += 1;
            quantitySpan.textContent = currentQuantity.toString();
            localStorage.setItem('quantity', currentQuantity); // Save updated quantity to local storage
        }
    }
}

// Function to decrease quantity
function decreaseQuantity() {
    const quantitySpan = document.getElementById('quantity-display');
    if (quantitySpan) {
        let currentQuantity = parseInt(quantitySpan.textContent, 10);
        if (!isNaN(currentQuantity) && currentQuantity > 1) { // Ensure quantity doesn't go below 1
            currentQuantity -= 1;
            quantitySpan.textContent = currentQuantity.toString();
            localStorage.setItem('quantity', currentQuantity); // Save updated quantity to local storage
        }
    }
}

// Function to save the cart to local storage
function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Function to update cart display
function updateCartDisplay() {
    const cartItemsElement = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    let total = 0;

    if (cartItemsElement) {
        cartItemsElement.innerHTML = '';
        for (const [itemKey, item] of Object.entries(cart)) {
            const [productName, color, size] = itemKey.split('|');
            const itemTotal = item.price * item.quantity;
            total += itemTotal;
            cartItemsElement.innerHTML += `
                <div class="cart-item">
                    <div class="cart-item-details">
                        <h3>${productName}</h3>
                        <p>Color: ${color}</p>
                        <p>Size: ${size}</p>
                        <p>Rs.${item.price} x ${item.quantity}</p>
                    </div>
                    <div class="cart-item-quantity">
                        <button class="cart-quantity-btn minus" data-product="${itemKey}">-</button>
                        <span>${item.quantity}</span>
                        <button class="cart-quantity-btn plus" data-product="${itemKey}">+</button>
                    </div>
                    <button class="cart-item-remove" data-product="${itemKey}">Remove</button>
                </div>
            `;
        }
        if (cartTotalElement) {
            cartTotalElement.textContent = `Rs.${total.toFixed(2)}`;
        }
        updateCartCount();
    }
}

// Function to add an item to the cart
function addToCart(productName, price, quantity = 1) {
    if (quantity > 0 && selectedColor && selectedSize && !isNaN(price) && price > 0) {
        const itemKey = `${productName}|${selectedColor}|${selectedSize}`;
        if (cart[itemKey]) {
            cart[itemKey].quantity += quantity;
        } else {
            cart[itemKey] = { price: price, quantity: quantity, color: selectedColor, size: selectedSize };
        }
        saveCart();
        updateCartDisplay();
        openCartModal(); // Open the cart modal after adding an item
        console.log(`Added ${quantity} of ${productName} (${selectedColor}, ${selectedSize}) to the cart at Rs.${price} each.`);
    } else {
        console.log('Please select a color and size before adding to the cart.');
    }
}

// Function to update the cart count
function updateCartCount() {
    const totalItems = Object.values(cart).reduce((sum, item) => sum + item.quantity, 0);
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        cartCount.textContent = totalItems;
        cartCount.style.display = totalItems > 0 ? 'flex' : 'none';
    }
    localStorage.setItem('cartCount', totalItems); // Save cart count to local storage
}

// Function to load the cart count from local storage on page load
function loadCartCount() {
    const cartCount = document.querySelector('.cart-count');
    const savedCartCount = localStorage.getItem('cartCount') || '0';
    if (cartCount) {
        cartCount.textContent = savedCartCount;
        cartCount.style.display = savedCartCount > 0 ? 'flex' : 'none';
    }
}

// Event listener for quantity buttons
document.addEventListener('DOMContentLoaded', function() {
    // Initialize quantity display
    updateQuantityDisplay();

    // Load cart from local storage
    cart = JSON.parse(localStorage.getItem('cart')) || {};

    // Load cart count on page load
    loadCartCount();

    // Load cart display on page load
    updateCartDisplay();

    // Event listener for Add to Cart buttons
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const productName = this.dataset.product;
            const price = parseFloat(this.dataset.price);
            const quantitySpan = document.getElementById('quantity-display');
            if (quantitySpan) {
                const quantity = parseInt(quantitySpan.textContent, 10);
                if (!isNaN(quantity) && quantity > 0) {
                    addToCart(productName, price, quantity);
                    updateQuantityDisplay(); // Reset the displayed quantity to 1 after adding to cart
                }
            }
        });
    });

    // Event listener for cart modal close button
    document.querySelector('.close-modal')?.addEventListener('click', closeCartModal);

    // Event listener for quantity adjustment buttons in cart modal
    document.addEventListener('click', function(event) {
        if (event.target.matches('.cart-quantity-btn.plus')) {
            const itemKey = event.target.dataset.product;
            if (cart[itemKey]) {
                cart[itemKey].quantity += 1;
                saveCart();
                updateCartDisplay();
            }
        } else if (event.target.matches('.cart-quantity-btn.minus')) {
            const itemKey = event.target.dataset.product;
            if (cart[itemKey] && cart[itemKey].quantity > 1) {
                cart[itemKey].quantity -= 1;
                saveCart();
                updateCartDisplay();
            }
        } else if (event.target.matches('.cart-item-remove')) {
            const itemKey = event.target.dataset.product;
            delete cart[itemKey];
            saveCart();
            updateCartDisplay();
        }
    });

    // Event listener for cart icon button
    document.querySelector('.cart-icon')?.addEventListener('click', openCartModal);
});
