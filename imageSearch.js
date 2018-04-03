#!/usr/bin/node
var DomParser = require('dom-parser');
var parser = new DomParser();

const args = process.argv; var query = args[2];
query = encodeURIComponent(query)
var http = require('http');

var options = {
  host: 'cors-anywhere.herokuapp.com',
  path: "/https://www.google.com.ua/search?source=lnms&sa=X&gbv=1&tbm=isch&q="+query,
  headers: {'origin': 'null'}
};

callback = function(response) {
  var res = '';

  //another chunk of data has been recieved, so append it to `res`
  response.on('data', function (chunk) {
    res += chunk;
  });

  //the whole response has been recieved, so we just print it out here
  response.on('end', function () {
        parser = parser.parseFromString(res, "text/html")

        // Gets DOM element with image results
        let images = parser.getElementById("ires")

        images = images.getElementsByTagName("img")

        for (i = 0; i < images.length ; i ++) {
          console.log(images[i].getAttribute('src'))
        }

  });
}

http.request(options, callback).end();


