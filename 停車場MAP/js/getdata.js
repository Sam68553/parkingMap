function getdata(){
    $.ajax({
        type: "GET",
        url: "http://localhost:5001/getdata",
        contentType: "application/json;charset=utf-8",
        success: function (e) {
            data = e;
            mapboxgl.accessToken = 'pk.eyJ1Ijoiam9jODg4ODgiLCJhIjoiY2s3azllOW84MHl3dDNkazBxMHJidmdqNCJ9.KTsko6_RGFr8liErUNs_DA';
            var map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/mapbox/streets-v11',
            zoom: 11,
            center: [121.25,24.97]
            });
            for(var i=0;i<data.length;i++){
                console.log(data[i]);
                var popup = new mapboxgl.Popup({ closeOnClick: false })
                    .setLngLat([data[i]['wgsX'],data[i]['wgsY']])
                    .setHTML('<div style="font-weight:bolder;">'+data[i]['surplusSpace']+'</div>')
                    .addTo(map);
            }


        }

    })
}