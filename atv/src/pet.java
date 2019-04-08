import java.util.ArrayList;
import java.util.Scanner;


class Pet{
    String name;
    int energy;
    int hungry;
    int clean;
    int energyMax;
    int hungryMax;
    int cleanMax;


    public Pet(String name, int energy, int hungry, int clean){

        this.name = name;
        this.energy = energy;
        this.hungry = hungry;
        this.clean = clean;
        this.energyMax = energyMax;
        this.hungryMax = hungryMax;
        this.cleanMax = cleanMax;

    }

    public String toString() {
        return  "[" + this.name + "]" +
                "E: " + this.energy + "/" + this.energyMax + " " +
                "S: " + this.hungry + "/" + this.hungryMax + " " +
                "L: " + this.clean + "/" + this.cleanMax;
    }
}

class pet(){
public static void main(String[]args){
Scanner scan = new Scanner(System.in);
Pet pet=new Pet(name="",energy=0,hungry=0,clean=0);
System.out.println("end, init _nome _E _s _L, show");
    while(True){
            String line = scan.nextLine();
            int[]vet;
            vet=new int[]{2,3,4,1,2};
            String[]ui = line.split(regex: " ");
            if(ui[0].equal( "end")){
               break;
            }else if(ui[0].equals("init")){
                pet=new Pet(ui[1],Integer.parseInt(ui[2]),
                    Integer.parseInt(ui[3]),
                    Integer.parseInt(ui[4]));

            }else if(ui[0].equals("show")){
                System.out.println(pet);
            }else{
                System.out.println("fail: comand invalido");
        }

        }
    }

}
