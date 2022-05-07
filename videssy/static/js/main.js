let collapsibleEl = document.getElementsByClassName("collapsible");
let i;

for (i = 0; i < collapsibleEl.length; i++) {
  collapsibleEl[i].addEventListener("click", function() {
    this.classList.toggle("active");
    let hiddenEl = document.getElementById("hiddenEl");
    hiddenEl.classList.toggle("hidden");
  });
} 
