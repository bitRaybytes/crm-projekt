const hamburger = document.getElementById("hamburger");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

const pipelineFilter = document.getElementById("pipeline-filter");
const pipelineSublink = document.getElementById("pipeline-sublinks");
// const closeClick = document.getElementById("body");

const buttonAccountFilter = document.getElementById("btn-account-filter");
const accountSublink = document.getElementById("account-dashboard-sublinks");

// Sidebar: click on burger menu arranges an overlay background 
let menuOpen = false;

function openMenu() {
  menuOpen = true;
  overlay.style.display = "block";
  sidebar.style.marginLeft = "0";
}

function closeMenu() {
  menuOpen = false;
  overlay.style.display = "none";
  sidebar.style.marginLeft = "-170px";
}

hamburger.addEventListener("click", function () {
  if (!menuOpen) {
    openMenu();
  }
});

// Overlay Background display none if clicked in the overlay area
overlay.addEventListener("click", function () {
  if (menuOpen) {
    closeMenu();
  }
});
hamburger.addEventListener("click", function () {
  if (!menuOpen) {
    closeMenu();
  }
});


// aus dem Video: https://www.youtube.com/watch?v=SAvLBQBLRM8

// aus eigener Creation:

//Pipeline Filter Button on Dashboard Menu
let pipelinesFilterOpen = false;

function openPipelineFilter() {
  menuOpen = true;
  pipelineSublink.style.display = "block";
}

function closePipelineFilter() {
  menuOpen = false;
  pipelineSublink.style.display = "none";
}

pipelineFilter.addEventListener("click", function () {
  if (!menuOpen) {
    openPipelineFilter();
  }
});

// pipelineFilter.addEventListener("click", function () {
//   if (menuOpen) {
//     closePipelineFilter();
//   }
// });

// Try to close events like Sidebar or Dropdown Menus wherever you click
// let closeClickOpen = false;

// function closeButtons() {
//   menuOpen = false;
//   pipelineSublink.style.display = "hidden";
//   accountSublink.style.display = "hidden";
// }

// closeClick.addEventListener("click", function () {
//   if (!menuOpen) {
//     closeButtons();
//   }
// });

// Filter Button for Account on Dashboards (everyone)

let accountFilterOpen = false;

function openAccountFilter() {
  menuOpen = true;
  accountSublink.style.display = "block";
  // accountSublink.style.borderBottomLeftRadius = "4px"
}

function closeAccountFilter() {
  menuOpen = false;
  accountSublink.style.display = "hidden";
}

buttonAccountFilter.addEventListener("click", function () {
  if (!menuOpen) {
    openAccountFilter();
  }
});
buttonAccountFilter.addEventListener("click", function () {
  if (!menuOpen) {
    closeAccountFilter();
  }
});
