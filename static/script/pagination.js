const galerItem = document.querySelector(".galer").children;
const galer = document.querySelector(".galer");
const prev = document.querySelector(".Prev");
const next = document.querySelector(".Next");
const page = document.querySelector(".pagepos");
const totalpage = document.querySelector(".pagenum");
const pagenav = document.querySelector(".pagenav");
const maxItem = 9;
let index = 0;

const pagination=Math.ceil(window.mappingKey.length/maxItem);

function isCharDigit(n){
    return !!n.trim() && n*0==0;
  }


const skipto = document.getElementById('skip').addEventListener('input', function(){
    if(isCharDigit(this.innerHTML) && this.innerHTML>0 && this.innerHTML<=pagination){
        index = (this.innerHTML)-1;
    }
    else if(isCharDigit(this.innerHTML) && this.innerHTML>pagination){
        index = pagination-1;
    }
    else{
        index = 0;
    }
    console.log(this.innerHTML);
    showItems();
})

prev.addEventListener("click",function(){
    if (index>0){
        index--;
    }
    page.innerHTML=String(index+1);
    showItems();
})

next.addEventListener("click",function(){
    if (index<pagination-1){
        index++;
    }
    page.innerHTML=String(index+1);
    showItems();
})

function showItems(){
    totalpage.innerHTML='/ '+String(pagination);
    pagenav.classList.remove("invisible");
    galer.classList.remove("invisible");
    var dir = 'static/dataset/'

    for (let i=0;i<9;i++){
        if (i+9*index<window.mappingKey.length){
            galerItem[i].children[0].setAttribute("src",dir+window.mappingKey[i+9*index][1])
            galerItem[i].children[1].innerHTML = (window.mappingKey[i+9*index][0])+'%';
        }
        else{
            galerItem[i].children[0].setAttribute("src","")
            galerItem[i].children[1].innerHTML = " ";
        }
    }
}

window.onload=function(){
    page.innerHTML=String(index+1);
    showItems();
}

