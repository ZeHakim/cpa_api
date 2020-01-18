function generate(){
    var hf = window.location.href;
    var split = hf.split('generate');             


    var href = split[0]+"generate/"+document.getElementById('nbrPoints_g').value;
    document.getElementById("generatePoint").href = href;
}
function generateListe1(){
    var split = window.location.href.split('generate');
    var href = split[0]+"generate/"+"list1";
    document.getElementById("generatePoint_liste1").href = href;
}

function generateListe2(){
    var split = window.location.href.split('generate');
    var href = split[0]+"generate/"+"list2";
    document.getElementById("generatePoint_liste2").href = href;
}
function generateListe3(){
    var split = window.location.href.split('generate');
    var href = split[0]+"generate/"+"list3";
    document.getElementById("generatePoint_liste4").href = href;
}


var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var width = canvas.offsetWidth;
var height = canvas.offsetHeight;
var points = [];

function drawPoints(pts){
    points = []; // clean
    for (let i = 0; i < pts.length; i++) { 
        //(pts[i]);
        var x = pts[i][0]
        var y = pts[i][1]
        ctx.fillRect(x, y, 0.6,0.6);
        var coord = [x, y];
        points.push(coord);
    }
            
}

function drawCircle(info){
    ctx.beginPath();
    ctx.arc(info[0][0], info[0][1], info[1], 0,  2 * Math.PI);
    ctx.stroke();
}

function generate_algo(){
    var hf = window.location.href;

    var algo = "ritter";
    var partition = "list1";

    var rit = document.getElementById('ritterChoice').checked;
    var qui = document.getElementById('quickhullChoice').checked;
    var conv = document.getElementById('convexeChoice').checked;

    var l1 = document.getElementById('choice1').checked;
    var l2 = document.getElementById('choice2').checked;
    var l3 = document.getElementById('choice3').checked;
    var l4 = document.getElementById('choice4').checked;

    if (qui) algo = "quickhull";
    else if (conv) algo = "envloppe_convexe"

    if (l2) partition = "list2";
    else if (l3) partition = document.getElementById("nbrPoints").value;
    else if (l4) partition = "list3";

    var split = hf.split('generate');
    var href = split[0]+"generate/"+algo+"/"+partition+"/"
    document.getElementById("generate_algo").href = href;
}

function drawLine(pts){
    for (let i = 0; i < pts.length; i++) { 
        ctx.beginPath(); 
        ctx.moveTo(pts[i][0],pts[i][1]);
        ctx.lineTo(pts[(i+1)%pts.length][0],pts[(i+1)%pts.length][1]);
        ctx.stroke();
    }
}