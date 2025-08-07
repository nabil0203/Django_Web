
function nice (){
    console.log(new Date());
}


const btn = document.querySelector("button");

const iID = setInterval(nice, 1000);




btn.addEventListener("click", e => {
    clearInterval(iID);                          // if we click the button then the timer will stop
})

