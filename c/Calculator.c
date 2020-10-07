/*
*   Integer Number calculator,
*   This program doesn't support floating point numbers yet
*   This program assumes that you are inputing a correct expression
*   Say my name baby: Sukhchain Singh
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// function to be used by qsort
int minimum (const void *a, const void *b) 
{
   return ( *(int*)a - *(int*)b );
}

int main()
{
    system("title Calculator");
    

    char str[500], str_cpy[500];
    char *delim_operators = "+-*/ \n\t";
    char *delim_numbers = "0123456789 \n\t";
    int total_numbers=0;

    // Take input as a string!
    fgets(str, 499, stdin); 
    strcpy(str_cpy, str);

    char* token = strtok((char*) str_cpy, delim_operators);
    
    // count the number of Numbers
    while (token) {
        total_numbers++;
        // Get next token
        token = strtok(NULL, delim_operators);
    }
    int length = total_numbers-1;
    // refil the str_cpy string
    strcpy(str_cpy, str);


    // Now create a Numbers array and store the numbers in it
    int Numbers[total_numbers], i=0;
    token = strtok((char*) str_cpy, delim_operators);
    while (token) {
        Numbers[i] = atoi(token);

        // Get next token
        token = strtok(NULL, delim_operators);
        i++;
    }
    // refil the str_cpy string
    strcpy(str_cpy, str);

    
    // store operators seperately
    char Operators[total_numbers-1]; i=0;    
    token = strtok((char*) str_cpy, delim_numbers);
    while (token) {
        Operators[i] = token[0];

        // Get next token
        token = strtok(NULL, delim_numbers);
        i++;
    }


    // Now we have Numbers and Operators seperated,
    // now let's bring them together.
    // DIVIDE and CONQUER!

    // AST to track the BODMAS order
    typedef struct
    {
        char operator;
        int operand1;
        int operand2;
    } AST;

    // Number of operators == number of Operations
    AST Operations[total_numbers-1], operation_temp;

    for (int i=0; i<length; i++)
    {
        Operations[i].operator = Operators[i];
        Operations[i].operand1 = Numbers[i];
        Operations[i].operand2 = Numbers[i+1];
    }

    // Sort Operations accorfing to BODMAS
    typedef enum { PLUS, MINUS, MULTIPLY, DIVIDE } BODMAS;
    BODMAS order[total_numbers-1];

    for (int i=0; i<length; i++)
    {
        if (Operators[i] == '+')
            order[i] = PLUS;
        else if (Operators[i] == '-')
            order[i] = MINUS;
        else if (Operators[i] == '*')
            order[i] = MULTIPLY;
        else if (Operators[i] == '/')
            order[i] = DIVIDE;
    }


    // BODMAS sort algorithm,
    // sort it in such an order that the lower order operator
    // would go in the last and the higher order operator 
    // would come first.

    // Exp: operators [*,*,-,+,-,/,*,+,+,-,-,-,-,/]
    // Firstly Addition :- [*,*,-,-,/,*,-,-,-,-,/,+,+,+]
    // Secondly Subtraction :- [*,*,/,*,/,-,-,-,-,-,-,+,+,+]
    // Thirdly Multiplication :- [/,/,*,*,*,-,-,-,-,-,-,+,+,+]
    // Divide will automatically come in order.
    qsort(order, total_numbers-1, sizeof(BODMAS), minimum);
    // Faster lookup time
    for (size_t i = 0; i < length; i++)
    {
        if (order[i] == PLUS)
            for (size_t j = i; j < length; j++)
            {
                if (Operations[j].operator == '+')
                {
                    operation_temp = Operations[j];
                    Operations[j] = Operations[i];
                    Operations[i] = operation_temp;
                    break;
                }
            }
        else if (order[i] == MINUS)
            for (size_t j = i; j < length; j++)
            {
                if (Operations[j].operator == '-')
                {
                    operation_temp = Operations[j];
                    Operations[j] = Operations[i];
                    Operations[i] = operation_temp;
                    break;
                }
            }
        else if (order[i] == MULTIPLY)
            for (size_t j = i; j < length; j++)
            {
                if (Operations[j].operator == '*')
                {
                    operation_temp = Operations[j];
                    Operations[j] = Operations[i];
                    Operations[i] = operation_temp;
                    break;
                }
            }
        else if (order[i] == DIVIDE)
            for (size_t j = i; j < length; j++)
            {
                if (Operations[j].operator == '/')
                {
                    operation_temp = Operations[j];
                    Operations[j] = Operations[i];
                    Operations[i] = operation_temp;
                    break;
                }
            }
    }

    printf("\n\n");

    
    // Do the Calculations
    // You prbably are never going to get the correct value if you use divide,
    // but who cares?
    int total;
    for (int i = length - 1; i >= 0; i--)
    {
        if (Operations[i].operator == '+')
            total = Operations[i].operand1 + Operations[i].operand2;
        else if (Operations[i].operator == '-')
            total = Operations[i].operand1 - Operations[i].operand2;
        else if (Operations[i].operator == '*')
            total = Operations[i].operand1 * Operations[i].operand2;
        else if (Operations[i].operator == '/') {
            // A bit of error handling for the sake of mathematics,
            // otherwise keep your input clean!
            if (Operations[i].operand2 == 0) {
                printf("You can't divide by Zero"); exit(EXIT_FAILURE);
            }
            total = Operations[i].operand1 / Operations[i].operand2;
        }
    }

    printf("Total: %d", total);

    return 0;
}