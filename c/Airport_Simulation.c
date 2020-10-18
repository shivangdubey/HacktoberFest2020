#include<stdio.h>
#include<time.h>
#include<stdlib.h>

typedef struct plane
{
	int num;
	int ops;
	int wait;
} Plane;

extern Plane dat;

typedef struct landing
{
	Plane data;
	struct landing * link;
} Land;

extern Land *Front;
extern Land *Rear;

typedef struct takeoff
{
	Plane data;
	struct takeoff * link;
} Leave;

extern Leave *FrontTo;
extern Leave *RearTo;


void add_Land_Queue(Plane dat);
void add_Takeoff_Queue(Plane dat);
void Landed(int run);
void Takenoff(int run);
void new_Planes(int acs);
void Airport_Traffic_Control(int lim);
void refused(int planeOps, Plane dat);
void stats();



#define MAX 3

// The following global variables have to be initialised to 0 at the start of the program and hence used

int land_queue=0;
int takeoff_queue=0;
int land_Total=0;
int takeoff_Total=0;
int idleRun=0;
int handled=0;
int refuse=0;
int count=0;


Plane dat;
Land *Front;
Land *Rear;
Leave *FrontTo;
Leave *RearTo;



// This function is used to add planes to the landing queue

void add_Land_Queue(Plane dat)
{
	Land * temp = malloc(sizeof(Land));
	temp->data = dat;
	printf("\nPlane %d is ready to land",dat.num);
	if(Front==NULL)
		{
		Front=temp;
		Rear=temp;
		}
	else
		{
			if(land_queue==MAX)
			{
			refused(0,dat);
			}
	else
		{
		Rear->link=temp;
		Rear=temp;
		}
	}

	temp = NULL;
	free(temp);
	land_queue++;
}


// This function has been used to add planes to the takeoff queue


void add_Takeoff_Queue(Plane dat)
{
	Leave * temp = malloc(sizeof(Land));
	temp->data = dat;
	printf("\nPlane %d is ready to depart",dat.num);
	if(FrontTo==NULL)
		{
		FrontTo=temp;
		RearTo=temp;
		}
	else
		{
		if(takeoff_queue==MAX)
		{
	refused(1,dat);
		}
		else
		{
		RearTo->link=temp;
		RearTo=temp;
		}
		}

	temp = NULL;
	free(temp);
	takeoff_queue++;
}


// This function is used to remove the planes that has landed from the landing queue
void Landed(int run)
{
	Land *temp=malloc(sizeof(Land));
	if(Front==NULL)
		{
		printf("\nLanding queue is empty");
		}
	else
		{
		temp=Front;
		printf("\nPlane number %d has landed on runway %d",(temp->data).num,run);
		Front = Front->link;
		land_queue--;
		land_Total++;
		count++;
		}

	free(temp);
}

// This function is used to remove the planes that have taken off from the takeoff queue

void Takenoff(int run)
{
	Leave *temp=malloc(sizeof(Leave));
	if(FrontTo==NULL)
		{
		printf("\nno planes to depart");
		}
	else
		{
		temp=FrontTo;
		printf("\nPlane number %d has taken off from runway %d",(temp->data).num,run);
		FrontTo = FrontTo->link;
		takeoff_queue--;
		takeoff_Total++;
		count++;
		}

	free(temp);
}

// This function is used to generate new planes

void new_Planes(int acs)
{
	Plane new;
	for(int i=0;i<acs;i++)
		{
		handled++;
		new.num=handled;
		new.ops=rand()%2;
		new.wait=0;
		if(new.ops==0)
			{
			add_Land_Queue(new);
			}
		else
			{
			add_Takeoff_Queue(new);
			}
		}
}

// This function has been used for checking if the runway is idle , or if there is heavy traffic and since it is better to land a plane rather than make it wait in the air, the other runway is also used for landing

void Airport_Traffic_Control(int lim)
{
	int noDep=0;
	new_Planes(3);
		for(int i=0;i<lim;i++)
		{

		if(Front==NULL && noDep==1)
			{
			noDep=0;
			printf("\nAll planes in the air have landed");
			}

		if(FrontTo==NULL && Front==NULL)
			{
			idleRun++;
			printf("\nrunway is idle");
			}
		else
			{
			if(land_queue==MAX)
			{
			noDep=1;
			printf("\nHeavy traffic, both runways will be used to land planes\n");
			}
			if(Front==NULL)
			{
			Takenoff(1);
			}

		else
			{
			Landed(1);
			}

		if(noDep==0)
		Takenoff(2);
		else
		Landed(2);
		}
		new_Planes(3);
		}
}

// This function is used for refusing a plane to land

void refused(int planeOps, Plane dat)
{
	if(planeOps!=0)
		{
		printf("\nPlane %d is asked to try again later",dat.num);
		}

	refuse++;
}

// I have used this function to print all that stats of the program
void stats()
{
printf("\n Stats: \n ");
printf("The simulation has concluded after %d units \n",count);
printf("Total number of planes processed %d \n",handled);
printf("Number of planes landed %d \n",land_Total);
printf("Number of planes taken off %d \n",takeoff_Total);
printf("Number left ready to land %d \n",land_queue);
printf("Number left ready to take off %d \n",takeoff_queue);
printf("Number of planes refused to land %d \n",refuse);
}


int main()
{
printf("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
printf("Welcome to the Airport Simulation program where we have 2 runways, one only for takeoff and the other only for landing and in cases of heavy traffic , since it is better to land a plane rather than make it wait in the air, both runways will be used for landing. \n");
printf("Runway 1 has been chosen for landing\n");
printf("Runway 2 has been chosen for for takeoffs\n");
printf("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
srand(time(0));
int n;
printf("Enter the limit for new planes ");
scanf("%d",&n);
Airport_Traffic_Control(n);
stats();
}