# Default constructor
# 'this' in java = 'self' in python



class Car:
    def __init__(self):             # Constructor
        self.brand = ""
        self.model = ""
        


car1 = Car()                 # object created

car1.brand = "Toyota"
car1.model = "Corolla"
print(car1.brand, car1.model)






"""
-----------Eqvalant Code in JAVA------------



class Car {

    String brand;
    String model;

    
    Car() {                                            // Constructor
       
        this.brand = "";
        this.model = "";

    }

    public static void main(String[] args) {

        Car car1 = new Car();                             // object created

        car1.brand = "Toyota";
        car1.model = "Corolla";

        System.out.println(car1.brand + " " + car1.model);
    }
}

"""
