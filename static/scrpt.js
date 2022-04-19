const play          = () => location.href = "/tirage";
const restart       = () => {Musique(); location.href = "/game";}
const goHomePage    = () => location.href = "/";

const clickOnCardForReverse = thisCard => {
    let selectedCard = thisCard.getAttribute("data-card");
    let stateImg     = thisCard.getAttribute("src");

    stateImg === "/static/cards/back.png"
        ? stateImg = `/static/cards/${selectedCard}.png`
        : stateImg = `/static/cards/back.png`;

    thisCard.setAttribute("src", stateImg);
}


function Musique(time=0){
    window.addEventListener("DOMContentLoaded", event => {
        const audio = document.querySelector("audio");
        audio.volume = 0.2;
        audio.currentTime=time;
        console.log(audio)
        audio.play();
      });
}
    


// function Musique(){
//     const audio = document.querySelector("audio");
//     let time = audio.currentTime;

// }
