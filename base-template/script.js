document.addEventListener("DOMContentLoaded", function() {
    var input = document.querySelector(".barra__pesquisa");

    input.addEventListener("focus", function() {
        input.classList.add("placeholder-hidden");
    });

    input.addEventListener("blur", function() {
        if (input.value === "") {
            input.classList.remove("placeholder-hidden");
        }
    });
});