// Spinner
window.onload = function(){
    var loader = document.getElementById("outside-loader");
    loader.style.visibility = "hidden";
    loader.style.opacity = "0";
    loader.remove();
}

// Copy link to share
function getlink() {
    var aux = document.createElement("input");
    aux.setAttribute("value",window.location.href);
    document.body.appendChild(aux);
    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
    var linkCopy = document.getElementById("linkCopy");
    linkCopy.innerHTML = "Link copiado, gracias 🙌";
}
