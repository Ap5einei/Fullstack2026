function findMe(){
    const status = document.getElementById("status");
    const maplink = document.getElementById("maplink");

    function success(position){
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        status.textContent = "";
        maplink.href = "https://www.openstreetmap.org/#map=18/"+latitude+"/"+longitude;
        maplink.textContent = "Your location";
    }


    function error(){
        status.textContent = "Unable to retrieve your location";
    }

    if(!navigator.geolocation){
        status.textContent = "Geolocation is not supported by your browser";
    } else {
        status.textContent =  "No geolocatin";}
        if(!navigator.geolocation){
            status.textContent = "Geolocation is not supported by your browser";
        }
        navigator.geolocation.getCurrentPosition(success, error);

}