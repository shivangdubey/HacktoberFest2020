import java.util.Random;
import java.util.Scanner;



public class Tictactoe {
static Scanner inp=new Scanner(System.in);
static int playerScore=0;
static int computerScore=0;

    public static void main(String[] args) {
        char[][] board = {{'_','|','_','|','_'},{'_','|','_','|','_'},{' ','|',' ','|',' '} };
        boolean GameOver=false;
        boolean playAgain=true;
        displayBoard(board);

while(playAgain) {


    while (!GameOver) {

        playerMove(board);
        GameOver = isGameOver(board);
        if (GameOver) {
            break;
        }

        computerMove(board);
        GameOver = isGameOver(board);
        if (GameOver) {
            break;
        }
    }
    System.out.println("Player Score: "+playerScore);
    System.out.println("Computer Score: "+computerScore);
    System.out.println("Do you want to play again? Y/N: ");
    inp.nextLine();

    String result= inp.nextLine();

    switch(result){
        case "Y":
        case "y":
            playAgain=true;
            System.out.println("OKAY, LETS PLAY AGAIN!!");
            resetBoard(board);
            GameOver=false;
            displayBoard(board);
            break;

        case "n":
        case "N":
            playAgain=false;
            System.out.println("THANKS FOR PLAYING!!");
            break;
        default:
            break;


    }

}
    }

    public static void displayBoard(char[][] board){

        for(char [] row: board) {
            for (char c : row) {
                System.out.print(c);
            }
            System.out.println();
          }
    }


    public static void updateBoard(int position, int palyer, char[][] board){

        char character;
        if(palyer==1){
            character='X';
        }
        else{
        character='O';
        }

        switch (position){

            case 1:
                board[0][0]=character;
                displayBoard(board);
                break;
            case 2:
                board[0][2]=character;
                displayBoard(board);
                break;
            case 3:
                board[0][4]=character;
                displayBoard(board);
                break;
            case 4:
                board[1][0]=character;
                displayBoard(board);
                break;
            case 5:
                board[1][2]=character;
                displayBoard(board);
                break;
            case 6:
                board[1][4]=character;
                displayBoard(board);
                break;
            case 7:
                board[2][0]=character;
                displayBoard(board);
                break;
            case 8:
                board[2][2]=character;
                displayBoard(board);
                break;
            case 9:
                board[2][4]=character;
                displayBoard(board);
                break;
            default:
               break;

        }


    }


public  static void playerMove(char[][] board){
    System.out.println("Make a move (1-9)");



    int move = inp.nextInt();

    boolean result = isValidmove(move,board);

    while(!result){
        System.out.println("Invalid move, Please make a valid Move!!");
        move = inp.nextInt();
        result=isValidmove(move,board);
    }
    System.out.println("Player moved at Position: "+move);

    updateBoard(move,1,board);


}



public static boolean isValidmove(int move, char[][] board){

        switch(move){
            case 1:
                if(board[0][0]=='_') {
                    return true; }
                else {
                    return false;  }
            case 2:
                if(board[0][2]=='_') {
                    return true; }
                else {
                    return false;  }
            case 3:
                if(board[0][4]=='_') {
                    return true; }
                else {
                    return false;  }
            case 4:
                if(board[1][0]=='_') {
                    return true; }
                else {
                    return false;  }
            case 5:
                if(board[1][2]=='_') {
                    return true; }
                else {
                    return false;  }
            case 6:
                if(board[1][4]=='_') {
                    return true; }
                else {
                    return false;  }
            case 7:
                if(board[2][0]==' ') {
                    return true; }
                else {
                    return false;  }
            case 8:
                if(board[2][2]==' ') {
                    return true; }
                else {
                    return false;  }
            case 9:
                if(board[2][4]==' ') {
                    return true; }
                else {
                    return false;  }

            default:
                return false;



        }


}



public static void computerMove(char[][] board){

        Random random=new Random();

    int move= random.nextInt( 9)+1;
    boolean result=isValidmove(move, board);

    while(!result){
        move= random.nextInt( 9)+1;
        result=isValidmove(move, board);
    }
    System.out.println("Computer moved at Position: "+move);
    updateBoard(move,2,board);

}



public static boolean isGameOver(char[][] board){

        //horizontal
        if (board[0][0]=='X' && board[0][2]=='X' && board[0][4]=='X' ){
            System.out.println("Player wins!!");
            playerScore++;
            return true;
        }
        if (board[1][0]=='X' && board[1][2]=='X' && board[1][4]=='X' ){
        System.out.println("Player wins!!");
            playerScore++;
        return true;
        }
        if (board[2][0]=='X' && board[2][2]=='X' && board[2][4]=='X' ){
        System.out.println("Player wins!!");
            playerScore++;
        return true;
        }
        if (board[0][0]=='O' && board[0][2]=='O' && board[0][4]=='O' ){
        System.out.println("Computer wins!!");
        computerScore++;
        return true;
        }
        if (board[1][0]=='O' && board[1][2]=='O' && board[1][4]=='O' ){
        System.out.println("Computer wins!!");
            computerScore++;
        return true;
        }
        if (board[2][0]=='O' && board[2][2]=='O' && board[2][4]=='O' ){
        System.out.println("Computer wins!!");
            computerScore++;
        return true;
    }

    //vertical
    if (board[0][0]=='X' && board[1][0]=='X' && board[2][0]=='X' ){
        System.out.println("Player wins!!");
        playerScore++;
        return true;
    }
    if (board[0][0]=='O' && board[1][0]=='O' && board[2][0]=='O' ){
        System.out.println("Computer wins!!");
        computerScore++;
        return true;
    }

    if (board[0][2]=='X' && board[1][2]=='X' && board[2][2]=='X' ){
        System.out.println("Player wins!!");
        playerScore++;
        return true;
    }
    if (board[0][2]=='O' && board[1][2]=='O' && board[2][2]=='O' ){
        System.out.println("Computer wins!!");
        computerScore++;
        return true;
    }
    if (board[0][4]=='X' && board[1][4]=='X' && board[2][4]=='X' ){
        System.out.println("Player wins!!");
        playerScore++;
        return true;
    }
    if (board[0][4]=='O' && board[1][4]=='O' && board[2][4]=='O' ){
        System.out.println("Computer wins!!");
        computerScore++;
        return true;
    }

    //Diagonals
    if (board[0][0]=='X' && board[1][2]=='X' && board[2][4]=='X' ){
        System.out.println("Player wins!!");
        playerScore++;
        return true;
    }
    if (board[0][0]=='O' && board[1][2]=='O' && board[2][4]=='O' ){
        System.out.println("Computer wins!!");
        computerScore++;
        return true;
    }
    if (board[2][4]=='X' && board[1][2]=='X' && board[0][4]=='X' ){
        System.out.println("Player wins!!");
        playerScore++;
        return true;
    }
    if (board[2][4]=='O' && board[1][2]=='O' && board[0][4]=='O' ){
        System.out.println("Computer wins!!");
        computerScore++;
        return true;
    }

    //tie

    if (board[0][0]!='_' && board[0][2]!='_'&&  board[0][4]!='_'
            &&  board[1][0]!='_'&&  board[1][2]!='_'&&  board[1][4]!='_'
            &&  board[2][0]!=' '&&  board[2][2]!=' '&&  board[2][4]!=' '){

        System.out.println("Its a TIE!!");
        return true;
    }

return false;
}

public static void resetBoard(char [][] board){

        board[0][0]='_';
        board[0][2]='_';
        board[0][4]='_';
        board[1][0]='_';
        board[1][2]='_';
        board[1][4]='_';
        board[2][0]=' ';
        board[2][2]=' ';
        board[2][4]=' ';

}


}
