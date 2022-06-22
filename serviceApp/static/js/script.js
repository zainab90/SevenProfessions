let header = document.querySelector("header");
window.onscroll = () =>{
    let pos = document.documentElement.scrollTop
    if (pos > 0 ){
        header.classList.add("sticky");
    }
    else{
        header.classList.remove("sticky");
    }
    if (pos >300){
        scrollTopBtn.style.display = "grid";
    }
    else{
        scrollTopBtn.style.display = "none";
    }
    scrollTopBtn.addEventListener("click", () =>{
        document.documentElement.scrollTop = 0

    })
}

let hamMenuIcone = document.getElementById("ham-menu");
let navBar = document.getElementById("nav-bar");
let navLink = navBar.querySelectorAll("li");
let scrollTopBtn = document.getElementById("scroll-top")


hamMenuIcone.addEventListener("click", ()=> {
    navBar.classList.toggle("active")
    hamMenuIcone.classList.toggle("fa-times")
})

// navLink.forEach((navLink) =>{
//     navLink.addEventListener("click", ()=>{
//         navBar.classList.remove("active");
//         hamMenuIcone.classList.toggle("fa-times")
//     })
// })