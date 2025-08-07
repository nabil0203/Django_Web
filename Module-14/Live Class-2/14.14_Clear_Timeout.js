
function nice (){
    console.log(new Date());
}


const btn = document.querySelector("button");

const tID = setTimeout(nice, 5000);




btn.addEventListener("click", e => {
    clearTimeout(tID);                          // if we click the button then the time will never show
})

