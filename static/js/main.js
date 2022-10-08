let nav = document.getElementById("nav_bar123")
let btn = document.getElementById('brg')
btn.addEventListener("click", (e)=>{
    document.body.classList.toggle("_lock");
    nav.classList.toggle("_active")
    nav.classList.toggle("bg")
    btn.classList.toggle("_active")
})

let btc1 = document.getElementById("btc1")
let btc2 = document.getElementById("btc2")
let inp1 = document.getElementById("inp1")
let inp2 = document.getElementById("inp2")
inp1.addEventListener("input", (e)=>{
    let place = Number(inp1.value) * Number(btc1.value)
    console.log(place);
    console.log(btc2.value);
    inp2.value = place / btc2.value
    console.log(inp2.value);
})
function myFunction() {
    var copyText = document.getElementById("myInput");
    copyText.select();
    document.execCommand("copy");
    
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Text copied";
  }
  
  function outFunc() {
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy to clipboard";
  }