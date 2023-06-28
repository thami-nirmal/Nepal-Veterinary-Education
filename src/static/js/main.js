//Date
try {
    const date = new Date();
    document.getElementById("date-top").innerHTML = date.toDateString();
} catch (error) {
    
}

try {
    const date1 = new Date()
    document.getElementById("date-content").innerHTML = date1.toDateString();
    
} catch (error) {
    
}

//hamburger in responsive header
function myFunction() {
    var x = document.getElementById("myLinks");
    x.classList.toggle("show");

    var layer = document.getElementsByClassName("whole-body-layer");
    layer[0].classList.toggle("whole-layer");

    var body = document.getElementsByClassName("body-one");
    body[0].classList.toggle("body-two");

    var ham_icon = document.getElementById("ham1");
    ham_icon.classList.toggle("ham-active");
}
function layer() {
    var x = document.getElementById("myLinks");
    x.classList.remove("show");
    var layer = document.getElementsByClassName("whole-body-layer");
    layer[0].classList.remove("whole-layer");
    var body = document.getElementsByClassName("body-one");
    body[0].classList.remove("body-two");
    var ham_icon = document.getElementById("ham1");
    ham_icon.classList.remove("ham-active");
}

//responsive dropdown
// function myFunction_dropdown(i) {
//     var x = document.getElementsByClassName("responsive-drop");
//     x[i - 1].classList.toggle("active_dropdown");
// }

//active-answer //openlinks-in-responsive-nav-items
function openanswer(answerid) {
    var a = document.getElementById(answerid);
    var b = document.getElementsByClassName("tabcontent");
    for (i = 0; i < b.length; i++) {
        if (b[i].id != answerid) {
            b[i].classList.remove("active_answer");
            ``;
            icon_parent = b[i].parentElement;
            try {
                icon_parent
                    .getElementsByClassName("drop-icon")[0]
                    .classList.remove("focus-item");
            } catch {
                continue;
            }
        } else {
            icon_parent = b[i].parentElement;
            try {
                icon_parent
                    .getElementsByClassName("drop-icon")[0]
                    .classList.toggle("focus-item");
            } catch {
                continue;
            }
        }
    }
    a.classList.toggle("active_answer");
}

//que-coll 
function opencontent(answerid) {
    var a = document.getElementById(answerid);
    var b = document.getElementsByClassName("que-coll-left-item");
    for (i = 0; i < b.length; i++) {
        if (b[i].id != answerid) {
            b[i].classList.remove("active_que-coll");
        }
    }
    a.classList.toggle("active_que-coll");
}

//stickey header
window.onscroll = function () {
    stickey_header();
};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;
function stickey_header() {
    if (window.pageYOffset > sticky) {
        header.classList.add("stickyhead");
    } else {
        header.classList.remove("stickyhead");
    }
}
