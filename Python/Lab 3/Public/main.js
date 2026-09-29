async function sendCommand(command){
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;


}

function main() {
    console.log("Hello JavaScript!!!!!!!!");
    // document.querySelector("#reset").innerHTML = "Hello";

    document.querySelector("#reset").onclick = () => {
        console.log("You pressed the button!")
        sendCommand("RESET");
    };

// X-Axis
    document.querySelector("#x1").onclick = () => {
        sendCommand("X-AXIS 1");
    };

    document.querySelector("#x2").onclick = () => {
        sendCommand("X-AXIS 2");
    };

    document.querySelector("#x3").onclick = () => {
        sendCommand("X-AXIS 3");
    };

    document.querySelector("#x4").onclick = () => {
        sendCommand("X-AXIS 4");
    };

    document.querySelector("#x5").onclick = () => {
        sendCommand("X-AXIS 5");
    };

// Gripper

    document.querySelector("#gripperOpen").onclick = () => {
        sendCommand("GRIPPER OPEN");
    };

    document.querySelector("#gripperClose").onclick = () => {
        sendCommand("GRIPPER CLOSE");
    };
}


main();