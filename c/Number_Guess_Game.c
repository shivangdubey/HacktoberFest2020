#ifdef _WIN32
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#endif

#ifdef linux
#include <stdio.h>
#include <ncurses.h>
#include <stdlib.h>
#include <string.h>
#endif

int menu();

int main()
{
    int num, option=0;
    char* options[2];

    options[0] = "start";
    options[1] = "select mode";

    printf("Welcome to the Game!\n");
    while(1) 
    {
        option = menu(2, options);
        switch (option)
        {
        default:
            break;
        }

    }

    printf("Enter a number to start the game:- ");
    scanf(" %d", &num);
    printf("You entered %d\n", num);

    return 0;
}

int menu(int no_of_options, char* options[]) 
{
    // two charachers to read arrow keys
    char menu_ch1, menu_ch2;

    // "a H" for KEY_UP
    // "a P" for KEY_DOWN
    // "a K" for KEY_LEFT
    // "a M" for KEY_RIGHT
    // lookup on Grey codes for more info
    int option=1;
    while(1)
    {
        for (int i=0; i<no_of_options; i++)
        {
            if (i == option)
                printf("* ");
            else printf("  ");
            printf("%s\n", options[i]);
        }

        menu_ch1 = getch();
        if (menu_ch1 == -32) 
        {
            menu_ch2 = getch();
            switch(menu_ch2)
            {
                case 'H': // UP
                    option--;
                    break;
                case 'P': // DOWN
                    option++;
                    break;
                case 'K': // LEFT
                    option--;
                    break;
                case 'M': // RIGHT
                    option++;
                    break;
            }
            option%=no_of_options;
        }

        if (menu_ch1 == 'q')
            break;
        else if (menu_ch1 == ' ')
        {
            menu()
        }

        //printf("\e[1;1H\e[2J");
        system("clear");
    }
}