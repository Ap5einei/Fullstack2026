window.onload = function(){ if (localStorage.getItem("message")) {
    const localMMessage = document.getElementById("local");
    localMessage.textContent = "In local Storage:"+message;
}}
if (sessionStorage.get ("message")){
    const message = sessionStorage.getItem("message");
    const sessionMessage = document.getElementById("session");
    sessionMessage.textContent = "In session Storage:"+message;
    }
function saveToLocalStorage()
{localStorage.setItem("message",document.getEllementById("message").value)}

function saveToSessionStorage()
{sessionStorage.setItem("message",document.getElementbyId("message").value)}
