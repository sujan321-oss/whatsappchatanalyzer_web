document.addEventListener("DOMContentLoaded", function () {
    const leftDiv = document.querySelector(".leftdiv");
    const showButton = document.getElementById("showLeftDivButton");
    const firsticon=document.getElementById("firsticon")
    const secondicon=document.getElementById("secondicon")
    
    

    firsticon.addEventListener("click", function () {
      leftDiv.classList.toggle("hidden");
      firsticon.style.display = "none";
      secondicon.style.display='block';

    });


    secondicon.addEventListener("click", function () {
        firsticon.style.display = "block";
        secondicon.style.display = "none";
        leftDiv.classList.toggle("hidden");
        
      });


    
  });