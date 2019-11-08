
let Path = location.pathname.split('/').slice(1, 4);
Path = Path.join('/');
$('#sidebarnav li a').map(function () {
    if ($(this).attr('href') === '/' + Path + '/') {
        $(this).addClass("active");
    } else {
        $(this).removeClass("active");
    }
}).get();

document.getElementById("title_en").focus();


// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("cancelBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var no = document.getElementsByClassName("No")[0];
// When the user clicks the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
};

no.onclick = function () {
    modal.style.display = "none";
};
// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

