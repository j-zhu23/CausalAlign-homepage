const dialog = document.querySelector("#figure-dialog");
const dialogImage = dialog.querySelector("img");
document.querySelectorAll(".figure-button").forEach((button) => {
  button.addEventListener("click", () => {
    dialogImage.src = button.dataset.full;
    dialogImage.alt = button.dataset.alt || "Expanded research figure";
    dialog.showModal();
  });
});
dialog.querySelector(".dialog-close").addEventListener("click", () => dialog.close());
dialog.addEventListener("click", (event) => {
  if (event.target === dialog) dialog.close();
});
dialog.addEventListener("close", () => {
  dialogImage.removeAttribute("src");
});
