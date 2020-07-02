var menuButton = document.querySelector("#menuContainer");
var nightContainer = document.querySelector("#nightContainer");
var sunContainer = document.querySelector("#sunContainer");
var links = document.querySelector("#links");
var clickableLinks = document.querySelectorAll('#linkContainer a');
var goDown = "normalContainerAnimation";
var comeUp = "reverseContainerAnimation";

menuButton.addEventListener('click', menuClick);

clickableLinks.forEach(el => {
    el.addEventListener('click', menuClick);
});

function menuClick(e) {
    if((sunContainer.getAttribute('class') === null) && (nightContainer.getAttribute('class') === null)){
        sunContainer.style = "display: block;";
        links.style = "display: block;";
        nightContainer.setAttribute('class', goDown);
        sunContainer.setAttribute('class', comeUp);
        links.setAttribute('class', comeUp);
    } else if(sunContainer.getAttribute('class') === comeUp){
        sunContainer.removeAttribute('class');
        nightContainer.removeAttribute('class');
        links.removeAttribute('class');
        void sunContainer.getBBox();
        void nightContainer.getBBox();
        void links.offsetWidth;
        nightContainer.setAttribute('class', comeUp);
        sunContainer.setAttribute('class', goDown);
        links.setAttribute('class', goDown);
        // wait for animation to end
        setTimeout(function(){links.style = "display: none;"}, 1000);
    }else if(nightContainer.getAttribute('class') === comeUp){
        links.style = "display: block;";
        sunContainer.removeAttribute('class');
        nightContainer.removeAttribute('class');
        links.removeAttribute('class');
        void sunContainer.getBBox();
        void nightContainer.getBBox();
        void links.offsetWidth;
        nightContainer.setAttribute('class', goDown);
        sunContainer.setAttribute('class', comeUp);
        links.setAttribute('class', comeUp);
    }
}