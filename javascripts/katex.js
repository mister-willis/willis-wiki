// Render math with KaTeX (self-hosted in javascripts/katex/).
// pymdownx.arithmatex (generic mode) wraps formulas in .arithmatex spans/divs
// using \( \) and \[ \] delimiters. document$ is Material's page-load
// observable, so this also runs after instant navigation.
document$.subscribe(function () {
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false },
    ],
    throwOnError: false,
  });
});
