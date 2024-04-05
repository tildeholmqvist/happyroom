// expertise.js
var currentPosition = 0;
var maxPosition = 2; 
updateContent();

document.getElementById("next-step1").addEventListener("click", function() {
    if (currentPosition < maxPosition) {
        currentPosition++;
        updateContent();
    }
});

document.getElementById("next-step2").addEventListener("click", function() {
    if (currentPosition < maxPosition) {
        currentPosition++;
        updateContent();
    }
});

document.getElementById("prev-step2").addEventListener("click", function() {
    if (currentPosition > 0) {
        currentPosition--;
        updateContent();
    }
});

document.getElementById("prev-step3").addEventListener("click", function() {
    if (currentPosition > 0) {
        currentPosition--;
        updateContent();
    }
});

function updateContent() {
    var content = document.getElementById("content");
    content.innerHTML = "Current Position: " + currentPosition + "<br><br>";
}
