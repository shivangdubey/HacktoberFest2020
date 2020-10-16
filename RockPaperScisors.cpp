#include <iostream>
#include <string>
#include <stdlib.h>
#define goal 3
#include <time.h>
using namespace std;
// 1= rock 2= paper 3 = scisors
int main() {
	srand(time(NULL));
	int win=0,pscore=0,cscore=0;
	cout<< "Let's play a game of rock paper scisors !!! \n\n First to 3 wins. \n\n\n\n" ;

	while(win==0){
		int cmove, pmove;
		cmove = rand()%3 + 1 ;  //this line determines the move the computer makes 

		cout << "\nenter \n1 for Rock \n2 for Paper \n3 for Scisors \n\n";
		cin >> pmove;
		/**************************
		computer wins
		**************************/
		if (pmove==cmove+2%3 || (pmove== 3 && cmove== 1) ){
			cout << "computer put out ";
			switch (cmove){
			case 1: cout << "Rock";
			break;
			case 2: cout << "Paper";
			break;
			case 3: cout << "Scisors";
			break;
			}
			cscore++;
			cout << "\n\nComputer won this round \n\nThe score now is computer : " << cscore << " Player : " << pscore << "\n\n";
			if (cscore == goal){
				win = 1;
			}
			else if (pscore == goal){
				win = 2;
			}
		continue;
		}
		/**************************
		computer wins ends
		**************************/
		/**************************
		player wins
		**************************/
		if (cmove==(pmove+2)%3 || (cmove== 3 && pmove== 1) ){
			cout << "computer put out ";
			switch (cmove){
			case 1: cout << "Rock";
			break;
			case 2: cout << "Paper";
			break;
			case 3: cout << "Scisors";
			break;
			}
			pscore++;
			cout << "\n\nPlayer won this round \n\nThe score now is computer : " << cscore << " Player : " << pscore << "\n\n";
			if (cscore == goal){
				win = 1;
			}
			else if (pscore == goal){
				win = 2;
			}
		continue;
		}
		/**************************
		player wins ends
		**************************/
		/**************************
		draw
		**************************/
		if (cmove==pmove) {
			cout << "computer also put out ";
			switch (cmove){
			case 1: cout << "Rock";
			break;
			case 2: cout << "Paper";
			break;
			case 3: cout << "Scisors";
			break;
			}
			cout << "\nThis round was a draw \n\nThe score now is\n\t computer : " << cscore << "\t Player : " << pscore << "\n\n";
		}
		/**************************
		draw ends
		**************************/
		if (cscore == goal){
			win = 1;
		}
		else if (pscore == goal){
			win = 2;
		}
	}
	switch (win){
	case 1: cout << "computer won\n";
	break;
	case 2: cout << "you won\n";
	break;
	}
	cout << "                              GAME OVER                        ";
	return 0;
}

