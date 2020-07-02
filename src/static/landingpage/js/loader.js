window.onload = (event) => {
    let loader = document.querySelector('#loaderContainer');
    loader.classList.add("hidden");
    loader.addEventListener("animationend", function() {
    loader.parentNode.removeChild(loader);
    });
};

