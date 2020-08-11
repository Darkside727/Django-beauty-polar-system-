function myMap() {
  var mapOptions1 = {
    center: new google.maps.LatLng(51.508742,-0.120850),
    zoom:9,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map1 = new google.maps.Map(document.getElementById("googleMap1"),mapOptions1);
}
