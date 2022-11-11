const s = 'Hello World';
console.log(s.toUpperCase());
console.log(typeof s1)

const s2 = new String('Hello');
console.log(typeof s2);

console.log(window);
window.alert('Hello');
alert('No window.')
console.log(navigator.appVersion);

// gonna make a book
 /*const circle = {
    radius: 1,
    loaction:{
        x: 1,
        y: 1
    },
    draw: function(){
        console.log('draw')
    }
 }

 circle.draw();*/

 //constructor fun again

 function createCircle(radius){//theclass c.c and u can put parameters init
    return{//use return bc it actually make sense. get it this the onfo u wanna return so yea return it
        radius: radius,//so is the first5 part the parameter or the second part?
        draw: function(){
            console.log('draw')
        } 
    };
 }

 const circle = createCircle(1);//this should call it and (1) is the parameter

 function Circle(radius){
    //console.log('this', this);
    this.radius;//'this' is a refrence to an odj and it use toset the classe like python
    this.draw = function() {
        console.log('draw');
    }
}

const another =  new Circle(1);// use the new operator so it can make a new obj

/*notes on scopes. do not mess with the global scope 
unless you need to this is not python. big scope messes with the whole browser and
maybe the server too*/

