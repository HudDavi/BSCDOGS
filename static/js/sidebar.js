// OPEN AND CLOSE SIDEBAR
const showaside = (toggleId, navbarId) =>{
  const toggleAside = document.getElementById(toggleId);
  const navbarAside = document.getElementById(navbarId);
  if(toggleAside && navbarAside){
      toggleAside.addEventListener('click', ()=>{
          navbarAside.classList.toggle('aside-show');
      });
  }
}

showaside('aside-toggle','aside');