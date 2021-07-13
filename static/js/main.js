// Spinner
window.onload = function(){
    var loader = document.getElementById("outside-loader");
    loader.style.visibility = "hidden";
    loader.style.opacity = "0";
    loader.remove();
}
// End Spinner

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
// End Copy link to share

//Dark mode (activated/disabled). 
    // If this mode is active, the performance on the site is higher
const btn = document.querySelector(".btn-mode");
// Get the user's theme preference from local storage.
const currentTheme = localStorage.getItem("theme");

if (currentTheme == "dark") {
  document.body.classList.toggle("dark-mode");
} else if (currentTheme == "light") {
  document.body.classList.toggle("light-mode");
}else{
    // if it doesn't match, the default will be this:
    document.body.classList.toggle("light-mode");
}

// Change mode when the user clicks 
function changeMode(){
    if (currentTheme == "light") {
        document.body.classList.toggle("dark-mode");
        var theme = document.body.classList.contains("dark-mode") ? "dark" : "light";
    }else{
        document.body.classList.toggle("dark-mode");
        var theme = document.body.classList.contains("dark-mode") ? "dark" : "light";
    }

    localStorage.setItem("theme", theme);
}

// End Dark mode