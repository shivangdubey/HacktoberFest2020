
#include<stdio.h>
#include<stdlib.h>
     #define Swiss_Franc_rate 0.6072;      /*Swiss Franc rate*/
     #define British_Pounds_rate 1.4320;      /*British Pound rate*/
     #define Japanese_Yen_rate 0.0081;      /*Japanese Yen rate*/
     #define Canadian_Dollar_rate 0.6556;      /*Canadian Dollar rate*/
     #define Euros_rate 0.8923;


int main(void){
 
/*Declare floaters*/

float Swiss_Franc;          /*Swiss Franc*/
float British_Pounds;          /*British pounds*/
float Japanese_Yen;          /*Japanese Yen*/
float Canadian_Dollar;          /*Canadian Dollar*/
float Euros;               /*European Union Euro*/
float USD;               /*US Dollar*/
int   choice;

                   /*Title*/

printf("        Currency Conversion Program\n");

printf("----------------------------------------\n\n");


                  /*Menu*/

     printf("1)   Swiss Franc               \n");
     printf("2)   British Pound             \n");
     printf("3)   Japanese Yen              \n");
     printf("4)   Canadian Dollar           \n");
     printf("5)   Euro                      \n");
     printf("6)   Exit the Program          \n");

       
printf("\n");
printf("\n");

          /*Input from User*/

printf("Please enter your choice (1-6): ");
scanf("%d",&choice);

while((choice<1) || (choice>6)){
printf("Invalid entry, please Enter 1-6: ");
scanf("%i",&choice);
}
if(choice==1){
printf("Please the amount:  ");
scanf("%f",&Swiss_Franc);

     /*Conversion Calculation 1*/
Swiss_Franc = USD / Swiss_Franc_rate;

}
if(choice==2){
printf("Please enter the amount:  ");
scanf("%f",&British_Pounds);

     /*Conversion Calculation 2*/
British_Pounds = USD / British_Pounds_rate;
}

if(choice==3){
printf("Please enter the amount:  ");
scanf("%f",&Japanese_Yen);

     /*Conversion Calculation 3*/
Japanese_Yen = USD / Japanese_Yen_rate
}

if(choice==4){
printf("Please enter the amount:  ");
scanf("%f",&Canadian_Dollar);

     /*Conversion Calculation 4*/
Canadian_Dollar = USD / Canadian_Dollar_rate;
}

if(choice==5){
printf("Please enter the amount:  ");
scanf("%f",&Euros);

     /*Conversion Calculation 5*/
Euros = USD / Euros_rate;
}

if(choice==6){
printf("Exit the program:  ");

while (getchar() != '\n')
      continue;            
    goto top;              
  }                      
  printf("Goodbye!\n");
  return 0;

 }
    //Function
 
 void dashbar()                        
 {  
  int i = 1;                                  
  while (i < 50)                              
  {
     putchar ('-');                            
     i = i + 1;                              
  }
  putchar ('\n');                            
 }