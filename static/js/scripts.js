function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function opensignupForm() {
    document.getElementById("mysignupForm").style.display = "block";
  }
  
  function closesignupForm() {
    document.getElementById("mysignupForm").style.display = "none";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }
  
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    let modal = document.getElementById('mysignupForm');
    if (event.target == modal) {
      closeForm();
    }
  }