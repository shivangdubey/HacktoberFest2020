import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;
public class Program
{
    public static void main(String[] args) {
        System.out.println("Hello!\nType Rock, Paper or Scissors");
        Scanner scanner = new Scanner(System.in);
        String playerChoice = scanner.nextLine().toUpperCase().replace(" ", "");
        System.out.println("\nYou've chosen: " + playerChoice);
        
        if (playerChoice.equals("ROCK") || playerChoice.equals("PAPER") || playerChoice.equals("SCISSORS")) {
            
            generateOutcome(generateCPUChoice(), playerChoice);
        
    } else {
       System.out.println("\nYour input was not valid. Game exited");
    }
    
    }
    
    
    private static String generateCPUChoice() {
        
        int randomInt = ThreadLocalRandom.current().nextInt(1, 4);
        
        String cpuChoice = null;
        
        switch (randomInt) {
            case 1:
                cpuChoice = "ROCK";
                break;
            case 2:
                cpuChoice = "PAPER";
                break;
            case 3:
                cpuChoice = "SCISSORS";
                break;
        }
        
        return cpuChoice;
        
    }
    
    private static void generateOutcome(String cpuChoice, String playerChoice) {
    
        System.out.println("CPU chose: " + cpuChoice);
    
        if (cpuChoice.equals(playerChoice)) {
           
           System.out.println("It's a draw");
            
        } else {
        
            boolean playerWon = false;
        
        if (cpuChoice.equals("ROCK")) {
           if (playerChoice.equals("PAPER"))
               playerWon = true;
            else
                playerWon = false;
        } else if (cpuChoice.equals("PAPER")) {
           if (playerChoice.equals("SCISSORS"))
               playerWon = true;
            else
                playerWon = false;
        } else if (cpuChoice.equals("SCISSORS")) {
            if (playerChoice.equals("ROCK"))
                playerWon = true;
            else
                playerWon = false;
        }
        
        if (playerWon)
            System.out.println("You win");
        else
            System.out.println("You lose");
    
    }
    
}

}
