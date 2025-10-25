console.log("JavaScript файл підключено та працює!");

const jsFormSubmit = document.getElementById("intercept-submit");

jsFormSubmit.addEventListener("click", function(event) {
    event.preventDefault();

    const form = event.target.form;
    const formData = new FormData(form);

    fetch("/form", {
        method: "POST", 
        body: formData
    })
    .then(response => {
        return response.text()
    })
    .then(text => {
        const resultContainer = document.getElementById("js-form-result");
        resultContainer.innerText = text;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

const saveDataBtn = document.getElementById("save-data-btn");
saveDataBtn.addEventListener("click", function() {
    const textData = document.getElementById("text-data").value;

    fetch("/save-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mytext: textData })
    })

});


const getDataBtn = document.getElementById("get-data-btn");
getDataBtn.addEventListener("click", function() {
    fetch("/get-data")
    .then(response => {
        return response.json();
    })
    .then(data => {
        document.getElementById("data-display").innerText = data.data;
    })
    
});