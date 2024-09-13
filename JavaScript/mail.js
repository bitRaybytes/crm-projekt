const minimize = document.getElementById("minimize");
const mailsSidebar = document.getElementById("mails-sidebar")
const SidebarMails = document.getElementsByClassName("mails_sidebar")

let menuOpen = false;

function openMenu() {
    mailsSidebar.style.gridTemplateColumns = "250px 250px 1fr";
    
}

function closeMenu() {
    mailsSidebar.style.gridTemplateColumns = "24px 250px 1fr";
   
}

minimize.addEventListener("click", function() {
    if (!menuOpen){
        closeMenu();
    }
})
minimize.addEventListener("click", function(){
    if (!menuOpen){
        openMenu();
    }
})