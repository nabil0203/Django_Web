
const hiDiv = document.querySelector("h1");




// event listener

hiDiv.addEventListener("mouseover", e => {
    hiDiv.textContent = "BYE";
});                                                                   // when the cursor is on Hi; it will turn into BYE



hiDiv.addEventListener("mouseleave", e => {
    hiDiv.textContent = "Hi";
});                                                                   // when the cursor is moved out from BYE; it will turn into Hi again


