const shrink_btn = document.querySelector(".shrink-btn")
const sidebar_links = document.querySelectorAll(".sidebar-links a");
const active_tab = document.querySelector(".active-tab");

let activeIndex;

shrink_btn.addEventListener("click", ()=>{
   document.body.classList.toggle("shrink")
   shrink_btn.classList.add("hovered");

   setTimeout(
       () => {
          shrink_btn.classList.remove("hovered");
       }, 500
   )
});

function moveActiveTab() {
   let topPosition = activeIndex * 58 + 2.5;
   active_tab.style.top = `${topPosition}px`;
}

function changeLink() {
   sidebar_links.forEach(sideLink => sideLink.classList.remove("active"));
   this.classList.add("active");

   activeIndex = this.dataset.active;
   moveActiveTab();
}

sidebar_links.forEach(link => link.addEventListener("click", changeLink));