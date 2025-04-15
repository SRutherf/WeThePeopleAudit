
var divElement = document.getElementById('viz1742953780454');
var vizElement = divElement.getElementsByTagName('object')[0];

function resizeViz() {
    var parentWidth = divElement.offsetWidth;
    var windowHeight = window.innerHeight;

    if (parentWidth > 800) {
        vizElement.style.width = '100%';
        vizElement.style.height = (windowHeight * 0.85) + 'px';
    } else if (parentWidth > 500) {
        vizElement.style.width = '100%';
        vizElement.style.height = (windowHeight) + 'px';
    } else {
        vizElement.style.width = '100%';
        vizElement.style.height = (windowHeight ) + 'px';
    }
}
//window is resized
window.addEventListener('resize', resizeViz);
resizeViz(); // Initial call to ensure correct size

//Tableau JavaScript API
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);


document.getElementById("download-btn").addEventListener("click", function() {
    alert("Download Data functionality coming soon.");
});

document.getElementById("download-btn2").addEventListener("click", function() {
    alert("Download Table functionality coming soon.");
});
