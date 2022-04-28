$("#myModal").on("shown.bs.modal", function () {
  $("#myInput").trigger("focus");
});

// Make it so the last word in each panel ends in a period, rather than a comma.
const words = document.querySelectorAll(".accordion-body");
for (const word of words) {
  commaToPeriod = word.childNodes[
    word.childNodes.length - 2
  ].textContent.replace(",", ".");
  word.childNodes[word.childNodes.length - 2].textContent = commaToPeriod;
}

// If a user finds a section useless, let them remove it if they want to
const removePanel = document.querySelectorAll(".exit-button");

// Each one that is clicked, remove panel from HTML
for (const panel of removePanel) {
  panel.addEventListener("click", function () {
    panel.parentElement.parentElement.parentElement.remove();
  });
}
// Abbreviation & Meanings of POS Tags
// NOTE: in app.py I renamed PRP$ since the character gave me issues in output.html
const pos_tags = [
  ["CC", "coordinating conjunction"],
  ["CD", "cardinal digit"],
  ["DT", "determiner"],
  ["EX", "existential there"],
  ["FW", "foreign word"],
  ["IN", "preposition/subordinating conjunction"],
  ["JJ", "adjective"],
  ["JJR", "adjective, comparative"],
  ["JJS", "adjective, superlative"],
  ["LS", "list market"],
  ["MD", "modal"],
  ["NN", "noun, singular"],
  ["NNS", "noun plural"],
  ["NNP", "proper noun, singular"],
  ["NNPS", "proper noun, plural"],
  ["PDT", "predeterminer"],
  ["POS", "possessive ending"],
  ["PRP", "personal pronoun"],
  ["PRPS", "(formerly PRP$) possessive pronoun"],
  ["RB", "adverb"],
  ["RBR", "adverb, comparative"],
  ["RBS", "adverb, superlative"],
  ["RP", "particle"],
  ["TO", "infinite marker"],
  ["UH", "interjection"],
  ["VB", "verb"],
  ["VBG", "verb gerund"],
  ["VBD", "verb past tense"],
  ["VBN", "verb past participle"],
  ["VBP", "verb, present tense not 3rd person singular"],
  ["VBZ", "verb, present tense with 3rd person singular"],
  ["WDT", "wh-determiner"],
  ["WP", "wh- pronoun"],
  ["WRB", "wh- adverb"],
];

const tagRenaming = document.querySelectorAll(".POS-tag");

for (const tag of tagRenaming) {
  for (let i = 0; i < pos_tags.length; i++) {
    if (tag.textContent === pos_tags[i][0]) {
      tag.textContent += `: ${pos_tags[i][1]}`;
    }
  }
}

// This checks to see if the Parts of Speech span's text contains:
// noun, verb, adjective, or miscellaneous
function loopOverPOSTags(labelText) {
  for (const tag of tagRenaming) {
    if (tag.innerText.includes(labelText.toLowerCase())) {
      tag.parentElement.parentElement.parentElement.classList.toggle("hidden");
    } else if (
      !tag.innerText.includes("noun") &&
      !tag.innerText.includes("verb") &&
      !tag.innerText.includes("adjective") &&
      labelText === "Miscellaneous"
    ) {
      tag.parentElement.parentElement.parentElement.classList.toggle("hidden");
    }
  }
}

const filterCheckboxes = document.querySelectorAll(".form-check-input");

for (const checkbox of filterCheckboxes) {
  checkbox.addEventListener("click", function () {
    // Label Text examples: Noun, Verb, Miscellaneous
    let labelText = checkbox.nextSibling.nextSibling.textContent;

    switch (labelText) {
      case "Noun":
        loopOverPOSTags(labelText);
        break;
      case "Verb":
        loopOverPOSTags(labelText);
        break;
      case "Adjective":
        loopOverPOSTags(labelText);
        break;
      case "Miscellaneous":
        loopOverPOSTags(labelText);
        break;
      default:
        console.log(false);
    }
  });

  let box = document.getElementById("inlineCheckbox4");
  box.click();
  box.checked = false;
}

// Original copy/paste, but I wanted to remove the examples
// const pos_tags = [
//   ["CC", "coordinating conjunction"],
//   ["CD", "cardinal digit"],
//   ["DT", "determiner"],
//   ["EX", "existential there"],
//   ["FW", "foreign word"],
//   ["IN", "preposition/subordinating conjunction"],
//   ["JJ", "This NLTK POS Tag is an adjective (large)"],
//   ["JJR", "adjective, comparative (larger)"],
//   ["JJS", "adjective, superlative (largest)"],
//   ["LS", "list market"],
//   ["MD", "modal (could, will)"],
//   ["NN", "noun, singular (cat, tree)"],
//   ["NNS", "noun plural (desks)"],
//   ["NNP", "proper noun, singular (sarah)"],
//   ["NNPS", "proper noun, plural (indians or americans)"],
//   ["PDT", "predeterminer (all, both, half)"],
//   ["POS", "possessive ending (parent ‘s)"],
//   ["PRP", "personal pronoun (hers, herself, him, himself)"],
//   ["PRPS", "(formerly PRP$) possessive pronoun (her, his, mine, my, our)"],
//   ["RB", "adverb (occasionally, swiftly)"],
//   ["RBR", "adverb, comparative (greater)"],
//   ["RBS", "adverb, superlative (biggest)"],
//   ["RP", "particle (about)"],
//   ["TO", "infinite marker (to)"],
//   ["UH", "interjection (goodbye)"],
//   ["VB", "verb (ask)"],
//   ["VBG", "verb gerund (judging)"],
//   ["VBD", "verb past tense (pleaded)"],
//   ["VBN", "verb past participle (reunified)"],
//   ["VBP", "verb, present tense not 3rd person singular(wrap)"],
//   ["VBZ", "verb, present tense with 3rd person singular (bases)"],
//   ["WDT", "wh-determiner (that, what)"],
//   ["WP", "wh- pronoun (who)"],
//   ["WRB", "wh- adverb (how)"],
// ];
