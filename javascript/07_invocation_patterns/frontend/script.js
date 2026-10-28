function start() {
    console.log("---Method Invocation Pattern---");

    var person = {
        name:"Calvin",
        age :25,
        greet : function() {
            console.log("Hello, my name is " + this.name);
        }
    };

    person.greet();

    console.log("---Function Invocation Pattern---");

    person.calculateAge = function(yearsold) {
        function calculateYearsOld() {
            return this.age + yearsold;
        }
        console.log("I will be " + calculateYearsOld() + " years old in " + yearsold + " years.");
    }   
}