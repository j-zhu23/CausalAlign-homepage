const video = document.querySelector("#demo-video");
const chapterButtons = [...document.querySelectorAll(".chapters button")];

function selectChapter(time) {
  const current = chapterButtons.reduce((selected, button) => {
    return Number(button.dataset.time) <= time ? button : selected;
  }, chapterButtons[0]);
  for (const button of chapterButtons) {
    if (button === current) button.setAttribute("aria-current", "true");
    else button.removeAttribute("aria-current");
  }
}

for (const button of chapterButtons) {
  button.addEventListener("click", () => {
    const time = Number(button.dataset.time);
    const seekAndPlay = () => {
      video.currentTime = time;
      selectChapter(time);
      video.play().catch(() => {});
    };
    if (video.readyState === 0) {
      video.addEventListener("loadedmetadata", seekAndPlay, { once: true });
      video.load();
    } else {
      seekAndPlay();
    }
  });
}
video.addEventListener("timeupdate", () => selectChapter(video.currentTime));

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
