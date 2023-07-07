// store each club's url
var urls = []
var div = document.getElementById("org-search-results")
var nodelist = div.getElementsByTagName("a")

for (let i = 0; i < nodelist.length; i++) {
   urls[i]=nodelist[i].href 
}

// store html websiste data as text
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

// find email substring
let emails = []

for(let i=0; i<urls.length; i++){
    var content = httpGet(urls[i])
    var start = content.indexOf("\"email\":")+9
    var end = content.indexOf("\"",start)

emails[i] = content.substring(start, end)
}

// code for storing club names
var club_names = []
var div = document.getElementById("org-search-results")
var nodelist = div.getElementsByTagName("a")

for( let i=0; i<nodelist.length; i++){
    if(nodelist[i].getElementsByTagName("img").length != 0){
        club_names[i]=nodelist[i].getElementsByTagName("img")[0].alt
    }
}
