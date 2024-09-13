const createAccount = document.getElementById("createAccount");
const popupForm = document.getElementById("popup-form");
const overlay = document.getElementById("overlay");
const registerBtn = document.getElementById("register-btn");
const headerRegister = document.getElementById("register-button-header");

let popupOpen = false;

function openPopup() {
  popupOpen = true;
  overlay.style.display = "block";
  popupForm.style.display = "block";
  popupForm.style.transition = "3s ease-in";
}

function closePopup() {
  popupOpen = false;
  overlay.style.display = "none";
  popupForm.style.display = "none";
}

createAccount.addEventListener("click", function () {
  if (!popupOpen) {
    openPopup();
  }
});

headerRegister.addEventListener("click", function () {
  if (!popupOpen) {
    openPopup();
  }
});

overlay.addEventListener("click", function () {
  if (popupOpen) {
    closePopup();
  }
});
