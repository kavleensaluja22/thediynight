// Validate if a cart item is valid
function isValidCartItem(item) {
    return item && typeof item.quantity === 'number' && item.quantity > 0;
}

// Retrieve the current quantity for a product
function getCurrentQuantity() {
    const quantityDisplay = document.getElementById('quantity-display');
    if (!quantityDisplay || isNaN(parseInt(quantityDisplay.textContent, 10))) {
        console.error("Quantity display element is missing or not a valid number");
        return 1; // Default to 1 if there's an issue
    }
    return parseInt(quantityDisplay.textContent, 10);
}

// Add item to the cart
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

// Update cart display (quantity, items, etc.)
function updateCartDisplay() {
    const cart = JSON.parse(localStorage.getItem('cart')) || {};
    let totalItems = 0;

    for (const cartKey in cart) {
        const item = cart[cartKey];
        if (isValidCartItem(item)) {
            totalItems += item.quantity;
        } else {
            console.warn("Invalid cart item encountered while updating count", item);
        }
    }

    const cartCountElement = document.getElementById('cart-count');
    if (cartCountElement) {
        cartCountElement.innerText = totalItems;
    }
}

// Show success message when item is added to the cart
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
        }, 3000); // Keep the message displayed for 3 seconds
    }
}

// Close the success message
function closeSuccessMessage() {
    const successMessage = document.getElementById('success-message');
    if (successMessage) {
        successMessage.style.opacity = '0';
        successMessage.style.transform = 'translate(-50%, -50%) scale(0.9)';
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 300); // Match the fade-out time
    }
}

// Increase the quantity of the product
function increaseQuantity() {
    const quantityDisplay = document.getElementById('quantity-display');
    if (quantityDisplay) {
        let currentQuantity = parseInt(quantityDisplay.textContent, 10);
        quantityDisplay.textContent = currentQuantity + 1;
    }
}

// Decrease the quantity of the product (don't go below 1)
function decreaseQuantity() {
    const quantityDisplay = document.getElementById('quantity-display');
    if (quantityDisplay) {
        let currentQuantity = parseInt(quantityDisplay.textContent, 10);
        if (currentQuantity > 1) {
            quantityDisplay.textContent = currentQuantity - 1;
        }
    }
}

// Change the main product image
function changeMainImage(src) {
    const mainImage = document.getElementById('main-image');
    if (mainImage) {
        mainImage.src = src;
    }
}

// Select color and update UI
function selectColor(button) {
    const colorButtons = document.querySelectorAll('.color-option');
    colorButtons.forEach(btn => btn.classList.remove('selected'));
    button.classList.add('selected');
    updatePrice();
}

// Select size and update UI
function selectSize(button) {
    const sizeButtons = document.querySelectorAll('.size-option');
    sizeButtons.forEach(btn => btn.classList.remove('selected'));
    button.classList.add('selected');
    updatePrice();
}

// Update the product price based on the selected options
function updatePrice() {
    const productPriceElement = document.getElementById('product-price');
    if (productPriceElement) {
        const basePrice = parseFloat(productPriceElement.dataset.basePrice) || 0;
        const selectedColor = document.querySelector('.color-option.selected');
        const selectedSize = document.querySelector('.size-option.selected');
        let newPrice = basePrice;
        if (selectedColor) {
            newPrice += parseFloat(selectedColor.dataset.price) || 0;
        }
        if (selectedSize) {
            newPrice += parseFloat(selectedSize.dataset.price) || 0;
        }
        productPriceElement.textContent = `Rs. ${newPrice.toFixed(2)}`;
    }
}

// Run this code when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    updateCartDisplay(); // Update cart count on page load
});
