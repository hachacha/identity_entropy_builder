return (function clickpos(path,method){
    function printMousePos(event) {
      console.log("clientX: " + event.clientX +" - clientY: " + event.clientY);
    }
    document.addEventListener("click", printMousePos);
})(arguments[0]);