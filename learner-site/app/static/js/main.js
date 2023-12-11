
function rotateIcon(){
    document.getElementsByClassName("crossB")[0].animate({
        rotate: "90deg"
    }, {duration: 225, fill: "forwards"});
}


document.getElementsByClassName("goBackButtonBurger")[0].addEventListener( "mouseenter", () => {
    document.getElementsByClassName("crossB")[0].animate({
        rotate: "90deg"
    }, {duration: 225, fill: "forwards"});
});

document.getElementsByClassName("goBackButtonBurger")[0].addEventListener( "mouseleave", () => {
    document.getElementsByClassName("crossB")[0].animate({
        rotate: "-90deg"
    }, {duration: 225, fill: "forwards"});
});





document.getElementsByClassName("goBackButtonBurger")[0].addEventListener("click", () => {
    const PANE = document.getElementsByClassName("burgerFullPane")[0];
    PANE.animate({
        left: "-100vw",
        opacity: "0"
    }, { duration: 200, fill: "forwards" });
});

document.querySelector(".hamburgerContainer .hamburger").addEventListener("click", () => {
    const PANE = document.getElementsByClassName("burgerFullPane")[0];
    PANE.animate({
        left: "0vw",
        opacity: "1"
    }, { duration: 200, fill: "forwards" });
});






window.addEventListener( "scroll", () => {
    if(document.querySelector(".lssec"))
        document.querySelector(".lssec").style.top = window.scrollY + "px";
});



// MAIN COURSE JS +++++++++++++++++++++++++++++++++++++++++++++++++++


document.getElementsByClassName("closeButtonPFP")[0].addEventListener("click", () => {
    const PANE = document.getElementsByClassName("profilePane")[0];

    PANE.animate({
        right: "-100vw",
        opacity: "0"
    }, { duration: 200, fill: "forwards" });
});



document.querySelectorAll(".profileContainer").forEach( profile => profile.addEventListener("click", () => {
    const PANE = document.getElementsByClassName("profilePane")[0];
    PANE.animate({
        right: "0vw",
        opacity: "1"
    }, { duration: 310, fill: "forwards" });
}));

