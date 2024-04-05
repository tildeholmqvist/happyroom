// code from https://www.tutorialspoint.com/how-to-create-previous-and-next-button-and-non-working-on-end-position-using-javascript

document.addEventListener("DOMContentLoaded", function() {
   let maxItem = 3;
   let currentItem = 0;
   let prevBtn = document.getElementById("prevBtn");
   let nextBtn = document.getElementById("nextBtn");

   if (prevBtn && nextBtn) {
       prevBtn.style.backgroundColor = "red";
       updateContent();
       prevBtn.addEventListener("click", function() {
           if(currentItem > 0) {
               currentItem--;
               document.getElementById("nextBtn").disabled = false;
               nextBtn.style.backgroundColor = "";
           }
           if(currentItem === 0) {
               this.disabled = true;
               prevBtn.style.backgroundColor = "red";
           }
           updateContent() ; 
       });
       nextBtn.addEventListener("click", function() {
           if(currentItem < maxItem) {
               currentItem++;
               document.getElementById("prevBtn").disabled = false;
               prevBtn.style.backgroundColor = "";
           }
           if(currentItem === maxItem) {
               this.disabled = true;
               nextBtn.style.backgroundColor = "red";
           }
           updateContent() ;
       });
   } else {
       console.error("One or both buttons not found.");
   }

   function updateContent() {
       // update UI or make API call here
       var content = document.getElementById("content");
       content.innerHTML = "Current Item: " + currentItem + "<br><br>";
   }
});
