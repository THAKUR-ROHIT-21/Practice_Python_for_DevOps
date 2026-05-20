// 01.Task : Authentication System

const username = "user1";
const validPwd = "pass@123";


let enterName = prompt("Enter your username:");
let enterPassword = prompt("Enter your password:");

if (enterName === username && enterPassword === validPwd) {
    console.log("Authentication successful! Welcome, " + username);
} else {
    console.log("Authentication failed! Invalid username or password.");
}

// secound Question 

let num1 = parseFloat(prompt("Enter first number:"));
let num2 = parseFloat(prompt("Enter second number:"));
let num3 = parseFloat(prompt("Enter third number:"));

let numbers = [num1, num2, num3];
numbers.sort((a, b) => b - a);


console.log("Numbers in Descending Order: " + numbers.join(", "));