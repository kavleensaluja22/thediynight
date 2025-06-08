// document.addEventListener('DOMContentLoaded', function () {
//     // Common Variables
//     const cart = JSON.parse(localStorage.getItem('cart')) || {};
//     const cartCount = document.getElementById('cart-count');
//     const cartItems = document.getElementById('cart-items');
//     const cartTotal = document.getElementById('cart-total');
//     const successMessage = document.getElementById('success-message');
//     const successClose = document.getElementById('success-close');
//     let basePrice = 0;
//     let selectedColorPrice = 0;
//     let selectedSizePrice = 0;

//     // Common Functions
//     const saveCartToLocalStorage = () => {
//         localStorage.setItem('cart', JSON.stringify(cart));
//     };

//     const updateCartUI = () => {
//         let totalCount = 0;
//         let totalAmount = 0;
//         cartItems.innerHTML = '';
//         Object.values(cart).forEach(item => {
//             const itemRow = `<div class="cart-item">
//                 <p>${item.name}</p>
//                 <p>${item.quantity} x Rs. ${item.price} = Rs. ${item.quantity * item.price}</p>
//             </div>`;
//             cartItems.innerHTML += itemRow;
//             totalCount += item.quantity;
//             totalAmount += item.quantity * item.price;
//         });
//         cartCount.textContent = totalCount;
//         cartTotal.textContent = `Rs. ${totalAmount}`;
//     };

//     const showSuccessMessage = () => {
//         successMessage?.style.display = 'block';
//         setTimeout(() => {
//             successMessage?.style.display = 'none';
//         }, 3000);
//     };

//     const closeSuccessMessage = () => {
//         successMessage?.style.display = 'none';
//     };

//     successClose?.addEventListener('click', closeSuccessMessage);

//     // Specific to `prodd.html`
//     if (document.body.dataset.page === 'product') {
//         const productPriceElement = document.getElementById('product-price');
//         const colorOptions = document.querySelectorAll('.color-option');
//         const sizeOptions = document.querySelectorAll('.size-option');
//         const quantityDisplay = document.getElementById('quantity-display');
//         const decreaseQuantityButton = document.getElementById('decrease-quantity');
//         const increaseQuantityButton = document.getElementById('increase-quantity');
//         const addToCartButton = document.querySelector('.add-to-cart');

//         basePrice = parseInt(productPriceElement?.dataset.basePrice, 10) || 0;

//         const updatePrice = () => {
//             const finalPrice = basePrice + selectedColorPrice + selectedSizePrice;
//             productPriceElement.textContent = `Rs. ${finalPrice}`;
//             addToCartButton.dataset.price = finalPrice;
//         };

//         colorOptions.forEach(button => {
//             button.addEventListener('click', () => {
//                 selectedColorPrice = parseInt(button.dataset.price, 10) || 0;
//                 colorOptions.forEach(b => b.classList.remove('selected'));
//                 button.classList.add('selected');
//                 updatePrice();
//             });
//         });

//         sizeOptions.forEach(button => {
//             button.addEventListener('click', () => {
//                 selectedSizePrice = parseInt(button.dataset.price, 10) || 0;
//                 sizeOptions.forEach(b => b.classList.remove('selected'));
//                 button.classList.add('selected');
//                 updatePrice();
//             });
//         });

//         decreaseQuantityButton?.addEventListener('click', () => {
//             let quantity = parseInt(quantityDisplay.textContent, 10);
//             if (quantity > 1) {
//                 quantity -= 1;
//                 quantityDisplay.textContent = quantity;
//             }
//         });

//         increaseQuantityButton?.addEventListener('click', () => {
//             let quantity = parseInt(quantityDisplay.textContent, 10);
//             quantity += 1;
//             quantityDisplay.textContent = quantity;
//         });

//         addToCartButton?.addEventListener('click', () => {
//             const productId = addToCartButton.dataset.product;
//             const productName = addToCartButton.dataset.name;
//             const productPrice = parseInt(addToCartButton.dataset.price, 10);
//             const quantity = parseInt(quantityDisplay.textContent, 10);

//             if (cart[productId]) {
//                 cart[productId].quantity += quantity;
//             } else {
//                 cart[productId] = {
//                     name: productName,
//                     price: productPrice,
//                     quantity
//                 };
//             }
//             saveCartToLocalStorage();
//             updateCartUI();
//             showSuccessMessage();
//         });

//         updatePrice();
//     }

//     // Specific to `home.html`
//     if (document.body.dataset.page === 'home') {
//         const productGrid = document.getElementById('product-grid');

//         productGrid?.addEventListener('click', function (event) {
//             const target = event.target;

//             if (target.classList.contains('add-to-cart')) {
//                 const productId = target.dataset.product;
//                 const productName = target.dataset.name;
//                 const productPrice = parseInt(target.dataset.price, 10);

//                 if (cart[productId]) {
//                     cart[productId].quantity += 1;
//                 } else {
//                     cart[productId] = {
//                         name: productName,
//                         price: productPrice,
//                         quantity: 1
//                     };
//                 }
//                 saveCartToLocalStorage();
//                 updateCartUI();
//                 showSuccessMessage();
//             }

//             if (target.classList.contains('increase-quantity')) {
//                 const productId = target.dataset.product;
//                 const quantityDisplay = document.getElementById(`product-quantity-display-${productId}`);
//                 let quantity = parseInt(quantityDisplay.textContent, 10);
//                 quantity += 1;
//                 quantityDisplay.textContent = quantity;
//             }

//             if (target.classList.contains('decrease-quantity')) {
//                 const productId = target.dataset.product;
//                 const quantityDisplay = document.getElementById(`product-quantity-display-${productId}`);
//                 let quantity = parseInt(quantityDisplay.textContent, 10);
//                 if (quantity > 1) {
//                     quantity -= 1;
//                     quantityDisplay.textContent = quantity;
//                 }
//             }
//         });
//     }

//     // Initialize Cart UI
//     updateCartUI();
// });

// document.addEventListener("DOMContentLoaded", function () {
//     const payButton = document.getElementById("rzp-button1");

//     if (!payButton) return;

//     const productId = payButton.dataset.productId;
//     const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//     payButton.addEventListener("click", function (e) {
//         e.preventDefault();

//         fetch(`/create-payment/${productId}/`, {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//                 "X-CSRFToken": csrfToken
//             }
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.order_id) {
//                 const options = {
//                     key: data.razorpay_key_id,
//                     amount: data.amount,
//                     currency: "INR",
//                     name: "TheDIYNight",
//                     description: data.product_name || "Product Purchase",
//                     order_id: data.order_id,
//                     prefill: {
//                         name: data.user_name,
//                         email: data.user_email,
//                         contact: data.user_contact
//                     },
//                     callback_url: data.callback_url,
//                     theme: {
//                         color: "#6daabd"
//                     }
//                 };

//                 const rzp = new Razorpay(options);
//                 rzp.open();
//             } else {
//                 alert("Failed to create payment. Please try again.");
//             }
//         })
//         .catch(error => {
//             console.error("Error:", error);
//             alert("Something went wrong. Please try again.");
//         });
//     });
// });
