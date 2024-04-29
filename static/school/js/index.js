setTimeout(function() {
        document.getElementById('message-container').style.display = 'none';
    }, 8000);


function openNav() {
  document.getElementById("mySidebar").style.width = "210px";
  document.getElementById("main").style.display = "none";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.display = "block";
}

