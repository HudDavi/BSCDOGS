// OPEN AND CLOSE MENU
const showMenu = (toggleId, navbarId) =>{
  const toggleMenu = document.getElementById(toggleId);
  const navbarMenu = document.getElementById(navbarId);
  if(toggleMenu && navbarMenu){
      toggleMenu.addEventListener('click', ()=>{
          navbarMenu.classList.toggle('menu-show');
      });
  }
}

showMenu('menu-toggle','menu');