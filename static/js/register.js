const usernameField = document.querySelector('#username');

usernameField.addEventListener("keyup", (e)=>{
console.log('7778889');
const usernameVal = e.target.value;

if (usernameVal.length > 0){
    fetch("/authenticate:register", {
        body: JSON.stringify({usernameField: usernameVal}),
        method: "POST"
    })
    .then((res)=>res.json())
    .then((data)=>{
        console.log("data", data);
    })
}

})
