window.onload = function() {}

function makeFontSizer(){
let fontSize = 16
document.body.style.fontSize = fontSize +"px";;
function changeSize(val){
    fontSize += val;
    document.body.style.fontSize = fontSize +"px";
}
return{
    bigger:function(){
        changeSize(2);
    },
    smaller:function(){
        changeSize(-2);
    }       
}   
}
