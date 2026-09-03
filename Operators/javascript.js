let cartTotal = 150;
let is_Loyalty_Member = true;

let discountPercentage;

if (cartTotal >= 100 && is_Loyalty_Member) {
    discountPercentage = 20;
} else if (cartTotal >= 100) {
    discountPercentage = 15;
} else if (is_Loyalty_Member) {
    discountPercentage = 5;
} else {
    discountPercentage = 0;
}

let discountAmount = cartTotal * (discountPercentage / 100);
let finalAmount = cartTotal - discountAmount;

if (finalAmount < 20) {
    finalAmount = finalAmount + 4.99;
}

console.log("Cart Total: $" + cartTotal);
console.log("Discount: $" + discountAmount);
console.log("Final Amount: $" + finalAmount);