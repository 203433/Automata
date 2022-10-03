class Vehiculo {
    // atributos
    String marca;
    int numruedas;

    // métodos

    // método constructor (no se usa la palabra void, pese a que un constructor no devuelve ningún valor) 
    public Vehiculo(String marca, int numruedas) {
        this.marca = marca;
        this.numruedas = numruedas;
    }

    // método para mostrar los atributos del objeto creado
    public void mostrarVehiculo() {
        System.out.println("El carro es marca: " + marca);
        System.out.println("El carro tiene: " + numruedas + " ruedas");
    }
}

public class Main {

    public static void main(String[] args) {
        Vehiculo Carro1 = new Vehiculo("Ford", 4); //creamos objeto invocando al constructor con la palabra reservasa new y le pasamos los atributos

        Carro1.mostrarVehiculo(); //invocamos el método que mostrará los atributos del objeto creado
    }
}