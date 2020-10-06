#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
    int id ;
    int counter = 100;
    id = fork() ;
    if ( id == 0 ) {
        printf ("\nCHILD::PID: %d", getpid());
        counter = counter+200;
    }else {
        printf ( "\nPARENT::PID: %d", getpid()); 
        counter = counter +50;
    } 
    printf ("\ncounter: %d, PID: %d", counter, getpid());
    return 0;
}