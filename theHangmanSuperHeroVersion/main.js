var theWord, wordLength, chance, playingGame;

// RESET AND INITILIZING GAME
function resetGame(){
    playingGame = true;
    theWord = wordGenerator();
    wordLength = theWord.length;
    if (wordLength>=9){
        chance =  wordLength + 7;
    } 
    else{    
        chance =  wordLength + 4;
    }
    generateButtons();
    createBlocks(wordLength);
    initialWord(theWord);

}
document.getElementById('new-game').addEventListener('click', function(){
    location.reload();
});
var audio = new Audio("reload.mp3");
audio.play();
resetGame();

//  CREATING KEYBOARD
function generateButtons() {
    let buttonsHTML = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').map(letter =>
      `
        <button class="btn btn-lg btn-primary m-2 key-btn" id='`+ letter +`' onClick="addWord('`+letter+`')">
            ` + letter + `
        </button>`).join('');
  
    document.getElementById('keyboard').innerHTML = buttonsHTML;
  }

// DISPLAYING RESULTS  
function addWord(letter){
    if (playingGame){
        document.getElementById('chance').textContent = 'CHANCE  ' + chance;  
        // enough chances? adding letters
        if (chance>0){
            chance = chance-1;
            for (var k = 0; k<wordLength; k++){
                if (letter === theWord[k] && document.getElementById(k).textContent === ''){
                    var audio = new Audio("correct.mp3");
                    audio.play();
                    document.getElementById(k).textContent = letter;
                    document.getElementById(k).style.backgroundColor = '#65ba65';
                    break;
                }
                else if(letter !== theWord[k]){
                    var audio = new Audio("kick-bass.mp3");
                    audio.play();
                }
            }
            for (var k = 0; k<wordLength; k++){
                if (document.getElementById(k).textContent === ''){
                    break;
                }
            }
            // completed puzzel ? displaying winner
            if(k === wordLength) {
                var audio = new Audio("winner.mp3");
                audio.play();
                document.getElementById("hint").textContent = '';
                document.getElementById('chance').textContent = '';
                playingGame = false;
            }
            
        }
    
         // out of chance and incomplete puzzel ? displaying looser
        else if(chance==0){
            var audio = new Audio("lost.mp3");
            audio.play();
            document.getElementById("hint").textContent = '';
            document.getElementById("chance").style.color = 'red';
            for(var i = 0; i<wordLength; i++){
                document.getElementById(i).textContent = theWord[i];
                document.getElementById(i).style.backgroundColor = '#ff5e45';
            }
            playingGame = false;
        }
    }
}

// CREATING THE PUZZLE BLOCKS ACCORDING TO THE PUZZEL LENGTH
function createBlocks(wordLength){
    for (var i = 0; i<wordLength; i++){
        var node = document.createElement("h2");
        node.setAttribute("class", "char")
        node.setAttribute("id", i);
        document.getElementById("blocks").appendChild(node);
    }
}

// INITIALIZING THE PUZZLE
function initialWord(word){
    var j = Math.floor(Math.random()*word.length);
    if (wordLength <= 5){
        document.getElementById(j).textContent = word[j];
        document.getElementById(j).style.backgroundColor = '#87869e'; 
    }
    else if (j === 0 || j === 1){
        document.getElementById(j).textContent = word[j];
        document.getElementById(j).style.backgroundColor = '#87869e';
        document.getElementById(j+2).textContent = word[j+2];
        document.getElementById(j+2).style.backgroundColor = '#87869e';
    }
    else{
        document.getElementById(j).textContent = word[j];
        document.getElementById(j).style.backgroundColor = '#87869e';
        document.getElementById(j-2).textContent = word[j-2];
        document.getElementById(j-2).style.backgroundColor = '#87869e';
    }
}

// GENERATING RANDOM WORDS FOR PUZZLE
function wordGenerator(){
    var x = Math.floor(Math.random()*4);
    if (x === 0){
        dc = ['BOSTERGOLD', 'GREENARROW', 'JOHONCONSTANTINE', 'AQUAMAN', 'MARTIANMANHUNTER',
        'WONDERWOMAN', 'GREENLANTERN', 'FLASH', 'BATMAN', 'SUPERMAN'];
        document.getElementById("hint").textContent = 'A HERO OF DC UNIVERSE'; 
        document.querySelector(".wrapper").style.backgroundImage = "url('dc.jpg')";
        var i = Math.floor(Math.random()*dc.length);
        return dc[i];
    }

    if (x === 3){
        dc_e = ['BLACKADAM', 'JOKER', 'DARKSIDE', 'DEATHSTROKE', 'RIDDLER',
        'DOOMSDAY', 'SINESTRO', 'PENGUIN', 'REDHOOD', 'BRAINIAC'];
        document.getElementById("hint").textContent = 'A VILLAIN OF DC UNIVERSE';
        document.querySelector(".wrapper").style.backgroundImage = "url('dc.jpg')";
        var i = Math.floor(Math.random()*dc_e.length);
        return dc_e[i]

    }

    if (x === 2){
        marvel = ['WOLVERINE', 'SPIDERMAN', 'THOR', 'IRONMAN', "HULK", 'CAPTAINAMERICA',
        'DAREDEVIL', 'PUNISHER', 'DEADPOOL', 'SILVERSURFER', 'CYCLOPS', 'NIGHTCRAWLER',
        'BUCKY', 'DOCTORSTRANGE', 'BLACKPANTHER', 'HAWKEYE', 'SCARLETWITCH', 'CAPTAINMARVEL',
        'VISION', 'BLACKWIDOW', 'BLADE', 'NOVA', 'FALCON']
        document.getElementById("hint").textContent = 'A HERO OF MARVEL UNIVERSE';
        var i = Math.floor(Math.random()*marvel.length);
        return marvel[i]

    }
    if (x === 1){
        marvel_e = ['DOCTORDOOM', 'MAGNETO', 'GREENGOBLIN', 'REDSKULL', 'LOKI', 'ULTRON', 'THANOS', 'GALACTUS',
        'VENOM', 'DORMAMMU', 'JUGGERNAUT', 'DOCTOROCTOPUS', 'SANDMAN']
        document.getElementById("hint").textContent = 'A VILLAIN OF MARVEL UNIVERSE';
        var i = Math.floor(Math.random()*marvel_e.length);
        return marvel_e[i]

    }  
}
