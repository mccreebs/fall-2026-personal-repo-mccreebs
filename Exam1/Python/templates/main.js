async function sendLEDCommand(command){
    var response = await fetch(`/api/led/${command}`);
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;


}

async function sendFLASHCommand(number, period){
    var response = await fetch(`/api/flash/${number}/${period}`);
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;


}

function main() {
    console.log("Hello JavaScript!!!!!!!!");

// LED
    document.querySelector("#LEDOn").onclick = () => {
        sendLEDCommand("on");
    };

    document.querySelector("#LEDOff").onclick = () => {
        sendLEDCommand("off");
    };

// Flash

    document.querySelector("#FLASH").onclick = () => {
        let number = document.querySelector("#number").value;
        let period = document.querySelector("#period").value;
        sendFLASHCommand(number, period);
    };    

}


main();

