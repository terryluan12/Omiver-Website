(function () {
    const buttons = document.querySelectorAll(".DEMO-ACTION")
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            document.getElementById("modal").style.display = "block";

        })
    })

    document.getElementById("close-modal-btn").onclick = () => {
        document.getElementById("modal").style.display = "none";
    }
})();