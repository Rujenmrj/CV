progressBarh=document.querySelector(".loadbarhtml");
progressBarc=document.querySelector(".loadbarcss");
progressBarj=document.querySelector(".loadbarjs");
var observer = new IntersectionObserver(function(entries) {
    if(entries[0].isIntersecting === true) {
        entries[0].target.style.width=entries[0].target.innerHTML;
    } else {
        entries[0].target.style.width=0;
    }
}, { threshold: [0] });

observer.observe(progressBarh);
observer.observe(progressBarc);
observer.observe(progressBarj);
