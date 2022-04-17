var hideDiv = document.querySelectorAll("#partsOfSpeech > .not-hidden");

for (let div of hideDiv) {
  div.addEventListener("click", function () {
    // 1. Remove Class from All Lis
    for (let div of hideDiv) {
      li.classList.removeClass("not-hidden");
      console.log("div hidden");
    }

    // // 2. Add Class to Relevant Li
    this.classList.addClass("hidden");
    console.log("class added");
  });
}
