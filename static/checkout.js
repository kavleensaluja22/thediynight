
  // // Apply promo code
  // function applyPromoCode() {
  //   const promoCodeInput = document.getElementById("promo-code-input");
  //   const promoCode = promoCodeInput.value.trim();
  
  //   if (!promoCode) {
  //     alert("Please enter a promo code");
  //     return;
  //   }
  
  //   // Simulate API call to validate promo code
  //   setTimeout(() => {
  //     // Mock promo codes
  //     const validPromoCodes = {
  //       WELCOME10: 0.1, // 10% off
  //       SUMMER20: 0.2, // 20% off
  //       FREESHIP: "free-shipping", // Free shipping
  //     };
  
  //     if (validPromoCodes[promoCode]) {
  //       // Valid promo code
  //       checkoutState.promoCode = promoCode;
  
  //       if (validPromoCodes[promoCode] === "free-shipping") {
  //         // Free shipping promo
  //         checkoutState.shippingCost = 0;
  //         alert("Promo code applied! Free shipping.");
  //       } else {
  //         // Percentage discount
  //         checkoutState.promoDiscount =
  //           checkoutState.subtotal * validPromoCodes[promoCode];
  //         alert(`Promo code applied! ${validPromoCodes[promoCode] * 100}% off.`);
  //       }
  
  //       // Update order summary
  //       updateOrderSummary();
  //     } else {
  //       // Invalid promo code
  //       alert("Invalid promo code");
  //     }
  //   }, 500);
  // }
//   payButton.addEventListener("click", function (e) {
//     e.preventDefault();
//     console.log("Pay button clicked");

//     fetch(`/create-payment/${productId}/`, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": csrfToken
//         }
//     })
//     .then(response => {
//         console.log("Response received");
//         return response.json();
//     })
//     .then(data => {
//         console.log("Response JSON:", data);
//         if (data.order_id) {
//             const options = {
//                 key: data.razorpay_key_id,
//                 amount: data.amount,
//                 currency: "INR",
//                 name: "TheDIYNight",
//                 description: data.product_name || "Product Purchase",
//                 order_id: data.order_id,
//                 prefill: {
//                     name: data.user_name,
//                     email: data.user_email,
//                     contact: data.user_contact
//                 },
//                 callback_url: data.callback_url,
//                 theme: {
//                     color: "#6daabd"
//                 }
//             };

//             const rzp = new Razorpay(options);
//             rzp.open();
//         } else {
//             alert("Failed to create payment. Please try again.");
//         }
//     })
//     .catch(error => {
//         console.error("Error:", error);
//         alert("Something went wrong. Please try again.");
//     });
// });
