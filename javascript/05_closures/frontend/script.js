window.onload = function() {
const fontSizer = makeFontSizer();
document.getElementById("bigger").onclick = fontSizer.bigger;
document.getElementById("smaller").onclick = fontSizer.smaller;
}
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
function makeCounter(val){
    let privateCounter = 0;
    if(val){
        privateCounter = val;
    }
    return{
        increment:function()
        {
            changeVal(1);
        },
        decrement:function()
        {
            changeVal(-1);
        },
        value:function()
        {
            return privateCounter;
        }
    }
}
        
}
