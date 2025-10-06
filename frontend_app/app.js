const latInput = document.getElementById("lat");
const lngInput = document.getElementById("lng");

const spinner = document.getElementById("spinner");

const map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19
}).addTo(map);

let marker;


function updateLocation(lat, lng) {
  latInput.value = lat.toFixed(6);
  lngInput.value = lng.toFixed(6);
  
}

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const lat = position.coords.latitude;
      const lng = position.coords.longitude;
      
      map.setView([lat, lng], 13);
      marker = L.marker([lat, lng], { draggable: true }).addTo(map);
      
      updateLocation(lat, lng);
      
      marker.on("dragend", () => {
        const pos = marker.getLatLng();
        updateLocation(pos.lat, pos.lng);
      });
      
      map.on("click", (e) => {
        marker.setLatLng(e.latlng);
        updateLocation(e.latlng.lat, e.latlng.lng);
      });
    },
    (error) => {
      alert("Geolocation failed: " + error.message);
    }
  );
} else {
  alert("Geolocation not supported");
}


document.getElementById("dataForm").addEventListener("submit", function(event) {
      event.preventDefault(); 
      
      document.getElementById("predictBtn").disabled=true
      document.getElementById("predictBtn").value = "Predicting...";
      
let n = document.getElementById("n");
let p = document.getElementById("p");
let k = document.getElementById("k");
let ph = document.getElementById("ph");
let h = document.getElementById("h");
let r = document.getElementById("r");
let t = document.getElementById("t");


// let url = `https://api.open-meteo.com/v1/forecast?latitude=${latInput.value}&longitude=${lngInput.value}&current_weather=true&hourly=relativehumidity_2m,precipitation`;

/*fetch(url)
  .then(response => response.json())
  .then(data => {*/
      //console.log(data);
      
      // let temperature = data.current_weather.temperature;
      // let humidity = data.hourly.relativehumidity_2m[0]; 
      // let rainfall = data.hourly.precipitation[0];
      
      
      fetch("http://127.0.0.1:8000/api/predict/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
        body: JSON.stringify({
          N: n.value,
          P: p.value,
          K: k.value,
          temperature: t.value,
          humidity: h.value,
          ph: ph.value,
          rainfall: r.value
        })
    
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    return response.json();
  })
  .then(data => {
    console.log("Response JSON:", data);
    
    

    const cropRecKeys = Object.keys(data)

   // document.getElementById("resultBox").textContent = JSON.stringify(data, null, 2);

    console.log(data)
    console.log(cropRecKeys)
    console.log(data[cropRecKeys[0]])
    my_modal_1.showModal()

    document.getElementById("cropRec0").textContent = cropRecKeys[0] + " : " + data[cropRecKeys[0]] + " %";
    document.getElementById("cropRec1").textContent = cropRecKeys[1] + " : " + data[cropRecKeys[1]] + " %";
    document.getElementById("cropRec2").textContent = cropRecKeys[2] + " : " + data[cropRecKeys[2]] + " %";
    document.getElementById("cropRec3").textContent = cropRecKeys[3] + " : " + data[cropRecKeys[3]] + " %";
    document.getElementById("cropRec4").textContent = cropRecKeys[4] + " : " + data[cropRecKeys[4]] + " %";
    document.getElementById("cropRec5").textContent = cropRecKeys[5] + " : " + data[cropRecKeys[5]] + " %";
    document.getElementById("cropRec6").textContent = cropRecKeys[6] + " : " + data[cropRecKeys[6]] + " %";

    
  })
  .catch(error => {
    console.error("Error:", error);
  }).finally(() => {
    console.log("Prediction completed.");

    document.getElementById("predictBtn").disabled = false
    document.getElementById("predictBtn").value = "Predict";
  });
  
 
  /*
}).catch(error => {
  console.error("ErrorRR:", error)
  }).finally(() => {
  console.log("Prediction completed.");
  
  document.getElementById("predictBtn").disabled= false
      document.getElementById("predictBtn").value = "Predict";
});*/


    })
