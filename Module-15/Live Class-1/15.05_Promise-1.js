// 1:14:10


// a new Promise has an Arrow function
// that Arrow function has resolve and reject




let p1 = new Promise((resolve, reject) => {

    let success = true;                                    // any operation can happen here

    if (success) {
        resolve("Successful Operation")
    }
    else {
        reject("Failed");
    }

}
);




p1                                                          // after promise is executed:-
    .then(result => {                                                 // if resolve is called, it goes to ".then"
        console.log(result);
    })                 
    .catch(result => {                                                // if reject is called, it goes to ".catch"
        console.log(result);
    })


