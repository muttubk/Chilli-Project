// TEst
var documentTitle = document.getElementById("document-title").innerText;
console.log(documentTitle);
const downloadLinkContainer = document.getElementById("download-link-container");

if (documentTitle === "Leaf Curl") {
  const downloadLink = document.createElement("a");

  downloadLink.href = "leaf_curl.html";
  downloadLink.textContent = "Download";
  // downloadLink.setAttribute("download", "https://training.github.com/downloads/github-git-cheat-sheet.pdf");
  downloadLink.setAttribute("target", "leaf_curl.html");

  downloadLinkContainer.appendChild(downloadLink);
} 
else if (documentTitle === "Document 2") {
  const downloadLink = document.createElement("a");

  downloadLink.href = "path/to/document2.pdf";
  downloadLink.textContent = "Download PDF";
  downloadLink.setAttribute("download", "");

  downloadLinkContainer.appendChild(downloadLink);
}