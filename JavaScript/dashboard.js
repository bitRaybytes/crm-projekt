const body = document.getElementsByTagName("body")
//Sidebar
const hamburger = document.getElementById("hamburger");
const sidebar = document.getElementById("sidebarmenu");
const overlay = document.getElementById("overlay");
//Header
const header = document.getElementById("header");

//Dashboard Filters
//Pipeline Filter
const pipelineFilter = document.getElementById("pipeline-filter");
const pipelineSublink = document.getElementById("pipeline-sublinks");
//Account Filter
const buttonAccountFilter = document.getElementById("btn-account-filter");
const accountSublink = document.getElementById("account-dashboard-sublinks");
//test close dropdowns at click on any space in body
const clickClose = document.getElementById("click");


//Sidebar Menu
let menuOpen = false;

function openMenu() {
    menuOpen = true;
    sidebar.style.marginLeft = "0";
    overlay.style.display = "block";
}
function closeMenu(){
    menuOpen = false;
    sidebar.style.marginLeft = "-170px";
    overlay.style.display = "none";
}

hamburger.addEventListener("click", function () {
    if (!menuOpen) {
      openMenu();
    }
  });
  hamburger.addEventListener("click", function(){
    if (!menuOpen){
        closeMenu()
    }
  })

overlay.addEventListener("click", function (){
    if(menuOpen) {
        closeMenu();
    }
});


// Pipeline Filter
let pipelinesFilterOpen = false;

function openPipelineFilter() {
  pipelinesFilterOpen = true;
  pipelineSublink.style.display = "block";
  pipelineFilter.style.borderBottomLeftRadius = "0"
}

function closePipelineFilter() {
  pipelinesFilterOpen = false;
  pipelineSublink.style.display = "none";
  pipelineFilter.style.borderBottomLeftRadius = "4px"
}

pipelineFilter.addEventListener("click", function () {
  if (!pipelinesFilterOpen) {
    openPipelineFilter();
  }
});
// document.addEventListener("click", function (){
//   if (!pipelinesFilterOpen){
//     closePipelineFilter();
//   }
// })


// Accounts Filter
let accountFilterOpen = false;

function openAccountFilter() {
  accountFilterOpen = true;
  accountSublink.style.display = "block";
  buttonAccountFilter.style.borderBottomLeftRadius = "0"
  buttonAccountFilter.style.borderBottomRightRadius = "0"
}

function closeAccountFilter() {
  accountFilterOpen = false;
  accountSublink.style.display = "none";
  buttonAccountFilter.style.borderBottomLeftRadius = "4px"
  buttonAccountFilter.style.borderBottomRightRadius = "4px"
  
}

buttonAccountFilter.addEventListener("click", function () {
  if (!accountFilterOpen) {
    openAccountFilter();
  }
});
buttonAccountFilter.addEventListener("click", function () {
  if (!accountFilterOpen) {
    closeAccountFilter();
  }
});
buttonAccountFilter.addEventListener("click", function(){
  if (!accountFilterOpen) {
    closeAccountFilter();
  }
});

body.addEventListener("click", function () {
  if (!accountFilterOpen)
    closeAccountFilter()
});


// click outside to close (Doesnt work yet!!!!!)

// clickClose.addEventListener("click", function() {
//     if(!menuOpen) {
//         closeAccountFilter()
//     }
// });
// clickClose.addEventListener("click", function() {
//     if(!menuOpen) {
//         closePipelineFilter()
//     }
// });


