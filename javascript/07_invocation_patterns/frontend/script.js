function start() {
    console.log("---Method Invocation Pattern---");

    var person = {
        name:"Calvin",
        age :25,
        greet : function() {
            console.log("Hello, my name is " + this.name);
        }
    };

    person.calculateAge(10);

    console.log("---Function Invocation Pattern---");

    person.calculateAge = function(yearsold) {
        function calculateYearsOld() {
            return this.age + yearsold;
        }
        calculateYearsOld = calculateYearsOld.bind(this);
        console.log("I will be " + calculateYearsOld() + " years old in " + yearsold + " years.");
    }   

    person.calculateAge(10);

       console.log("---Constructor Invocation Pattern---");

       var Person2 = function(name){
        this.name = name;
       }

       person2.prototype.greet = function() {

        return this.name+" says hello!";
         }
         console.log(new Person2 ("Calvin").greet());

         console.log("--- Apply Invoce Pattern---");

         person2.prototype.waveTo = function(who){
            console.log(this);
            return this.name +"waves to"+who.name;
         }

         var calvin = new Person2("Calvin");
         var hobbes = new Person2("Hobbes");
         var rover = {"name":"Rover"};

         console.log(calvin.waveTo.apply(hobbes["Calvin"]));
          console.log(calvin.waveTo.apply(rover["Calvin"]));

}