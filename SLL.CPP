#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

void insert_beg();
void insert_end();
void insert_pos();
void display();
void delete_beg();
void delete_end();
void delete_pos();
void search();
struct node{
		int data;
		struct node *next;
	   }*start=NULL,*q,*t;

void main()
{       clrscr();
	printf("\n\nSINGLY LINKED LIST\n");
	printf("RAJAT GUPTA [IT-25-19]");
	int ch;
	do{     clrscr();
		printf("\n-------MENU------\n");
		printf("\n1.INSERTION");
		printf("\n2.TRAVERSAL");
		printf("\n3.DELETION");
		printf("\n4.SEARCHING");
		printf("\n5.Exit");
		printf("\nEnter your choice = ");
		scanf("%d",&ch);

		switch(ch)
		{
			case 1:
			       printf("\n----INSERTION MENU----\n");
			       printf("\n1.Insert at beginning");
			       printf("\n2.Insert at end");
			       printf("\n3.Insert at position");
			       printf("\nEnter your choice = ");
			       scanf("%d",&ch);

			       switch(ch)
			       {
				case 1:insert_beg();break;
				case 2:insert_end();break;
				case 3:insert_pos();break;
				case 4:break;
			       }
			       getch();
			       break;
			case 2:
			       display();
			       getch();
			       break;

			case 3:
			       printf("\n----DELETION MENU----\n");
			       printf("\n1.Delete at beginning");
			       printf("\n2.Delete at end");
			       printf("\n3.Delete at position");
			       printf("\nEnter your choice = ");
			       scanf("%d",&ch);

			       switch(ch)
			       {
				case 1:delete_beg();break;
				case 2:delete_end();break;
				case 3:delete_pos();break;
				case 4:break;
			       }
			       getch();
			       break;
			case 4:
			       search();getch();break;
			case 5:break;
		}
	  }while(ch!=5);

}
void insert_beg()
{
	int num;
	t=(struct node*)malloc(sizeof(struct node));
	printf("\nEnter data : ");
	scanf("%d",&num);
	t->data = num;
	if(start==NULL)         //If list is empty
	{
		t->next=NULL;
		start=t;
	}
	else
	{
		t->next=start;
		start=t;
	}
}
void insert_end()
{
	int num;
	t=(struct node*)malloc(sizeof(struct node));
	printf("\nEnter data : ");
	scanf("%d",&num);
	t->data = num;
	t->next = NULL;
	if(start==NULL)         //If list is empty
	{
		start=t;
	}
	else
	{
		q=start;
		while(q->next!=NULL)
			q=q->next;
		q->next=t;
	}
}
void insert_pos()
{
	int pos,i,num;
	if(start==NULL)
	{
		printf("\nList is empty");
	}
	t=(struct node*)malloc(sizeof(struct node));
	printf("\nEnter position : ");
	scanf("%d",&pos);
	printf("\nEnter data : ");
	scanf("%d",&num);
	t->data = num;

	q=start;
	for(i=1;i<pos-1;i++)
	{
		if(q->next==NULL)
		{
			printf("There are less elements");
		}
		q=q->next;
	}
	t->next=q->next;
	q->next=t;
}
void display()
{
	if(start==NULL)
	{
		printf("\nList is empty");
	}
	else
	{
		q=start;
		printf("\nThe linked list is :\n");
		while(q!=NULL)
		{
			printf("%d ->",q->data);
			q=q->next;
		}
	}
}
void delete_beg()
{
	if(start==NULL)
	{
		printf("\nList is empty");
	}
	else
	{
		q=start;
		start=start->next;
		printf("Element Deleted");
		free(q);
	}
}
void delete_end()
{
	if(start==NULL)
	{
		printf("The list is empty");
	}
	else
	{
		q=start;
		while(q->next->next!=NULL)
			q=q->next;

		t=q->next;
		q->next=NULL;
		printf("Deleted element is %d ",t->data);
		free(t);
	}
}
void delete_pos()
{
	int pos,i;
	if(start==NULL)
	{
		printf("\nList empty is empty");
	}

	printf("Enter position to delete :");
	scanf("%d",&pos);

	q=start;
	for(i=1;i<pos-1;i++)
	{
		if(q->next==NULL)
		{
			printf("There are less elements");
		}
		q=q->next;
	}
	t=q->next;
	q->next=t->next;
	printf("Deleted element is %d ",t->data);
	free(t);
}
void search()
{
	struct node *ptr;
	int item,i=0,flag;
	ptr=start;
	if(ptr==NULL)
	{
		printf("\nList is Empty");
	}
	else
	{
		printf("\nEnter item which you want to search : \t");
		scanf("%d",&item);
		while(ptr!=NULL)
		{
			if(ptr->data==item)
			{
				printf("\nItem found at location %d ",i+1);
				flag=0;
				break;
			}
			else
			{
				flag=1;
			}
			i++;
			ptr=ptr->next;
		}
		if(flag==1)
		{
			printf("\nItem not found\n");
		}
	}
}