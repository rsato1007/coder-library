const showHideForm = (e) => {
    e.preventDefault();
    formEl.textContent === "Click here to add it" ? console.log(true) : console.log(false);
}

let formEl = document.querySelector(".show-subject-form");
formEl.addEventListener("click", e => {
    showHideForm(e)
});

