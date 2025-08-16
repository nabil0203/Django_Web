// 1:36:20


// a real example
// fetch github account details



let promise1 = new Promise((resolve, reject) => {

    fetch('https://api.github.com/users/nabil0203')                                 // fetch itself is a promise that's why ".then" & ".catch" is used here
        .then((response) => resolve(response.json()))
        .catch((error) => reject('Network error: ${error.message}'));

});

promise1
    .then((user) => console.log("GitHub User Data:", user))
    .catch((err) => console.log("Error:", err));

