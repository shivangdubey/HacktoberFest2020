#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct node{
		struct node *prev;
		struct node *next;
		int data;
	   };
struct node *head;

void insert_begin();
void insert_end();
void insert_pos();
void delete_begin();
void delete_end();
void delete_pos();
void display();
void search();

void main()
{       clrscr();
	int ch;
	printf("DOUBLY LINKED LIST");
	printf("\nRAJAT GUPTA [ IT-25-19 ] ");
	do{     clrscr();
		printf("\n\t-----MENU----\n");
		printf("\n1.INSERTION");
		printf("\n2.TRAVERSAL");
		printf("\n3.DELETION");
		printf("\n4.Searching");
		printf("\n5.Exit");
		printf("\nEnter your choice = ");
		scanf("%d",&ch);

		switch(ch)
		{
			case 1:printf("\n----INSERTION MENU----\n");
			       printf("\n1.Insert at beginning");
			       printf("\n2.Insert at end");
			       printf("\n3.Insert at position");
			       printf("\nEnter your choice = ");
			       scanf("%d",&ch);

			       switch(ch)
			       {
				case 1:insert_begin();break;
				case 2:insert_end();break;
				case 3:insert_pos();break;
				case 4:break;
			       }
			       getch();
			       break;
			case 2:display();
				getch();
			       break;

			case 3:printf("\n----DELETION MENU----\n");
			       printf("\n1.Delete at beginning");
			       printf("\n2.Delete at end");
			       printf("\n3.Delete at position");
			       printf("Enter your choice = ");
			       scanf("%d",&ch);

			       switch(ch)
			       {
				case 1:delete_begin();break;
				case 2:delete_end();break;
				case 3:delete_pos();break;
				case 4:break;
			       }
			       getch();
			       break;
			case 4:search();
				getch();
				break;
			case 5:break;
		}
	  }while(ch!=5);

}

void insert_begin()
{
	struct node *ptr;
	int item;

	ptr=(struct node*)malloc(sizeof(struct node));
	if(ptr==NULL)
	{
		printf("\nOverflow");
	}
	else
	{
		printf("\nEnter item value : ");
		scanf("%d",&item);
		if(head==NULL)
		{
			ptr->next=NULL;
			ptr->prev=NULL;
			ptr->data=item;
			head=ptr;
		}
		else
		{
			ptr->data=item;
			ptr->prev=NULL;
			ptr->next=head;
			head->prev=ptr;
			head=ptr;
		}
		printf("\nNODE INSERTED");
	}
}

void insert_end()
{
	struct node *ptr,*temp;
	int item;
	ptr=(struct node*)malloc(sizeof(struct node));
	if(ptr==NULL)
	{
		printf("\nOverflow");
	}
	else
	{
		printf("\nEnter value : ");
		scanf("%d",&item);
		ptr->data=item;
		if(head==NULL)
		{
			ptr->next=NULL;
			ptr->prev=NULL;
			head=ptr;
		}
		else
		{
			temp=head;
			while(temp->next!=NULL)
			{
				temp=temp->next;
			}
			temp->next=ptr;
			ptr->prev=temp;
			ptr->next=NULL;
		}
	}
	printf("Node Inserted");
}

void insert_pos()
{
	struct node*ptr,*temp;
	int item,loc,i;
	ptr=(struct node*)malloc(sizeof(struct node));
	if(ptr==NULL)
	{
		printf("\nOverflow");
	}
	else
	{
		temp=head;
		printf("\nEnter the location : ");
		scanf("%d",&loc);
		for(i=0;i<loc;i++)
		{
			temp=temp->next;
			if(temp==NULL)
			{
				printf("\nThere are less than %d elements",loc);
			}
		}
		printf("\nEnter value : ");
		scanf("%d",&item);
		ptr->data=item;
		ptr->next=temp->next;
		ptr->prev=temp;
		temp->next=ptr;
		temp->next->prev=ptr;
		printf("\nNode Inserted");
	}
}

void delete_begin()
{
	struct node*ptr;
	if(head==NULL)
	{
		printf("\nUnderflow");
	}
	else if(head->next==NULL)
	{
		head=NULL;
		free(head);
		printf("\nNode Deleted");
	}
	else
	{
		ptr=head;
		head=head->next;
		head->prev=NULL;
		free(ptr);
		printf("\nNode Deleted");
	}
}

void delete_end()
{
	struct node *ptr;
	if(head==NULL)
	{
		printf("\nUnderflow");
	}
	else if(head->next==NULL)
	{
		head=NULL;
		free(head);
		printf("\nNode Deleted\n");
	}
	else
	{
		ptr=head;
		if(ptr->next!=NULL)
		{
			ptr=ptr->next;
		}
		ptr->prev->next=NULL;
		free(ptr);
		printf("\nNode Deleted");
	}
}

void delete_pos()
{
	struct node *ptr,*temp;
	int item;
	printf("\nEnter the data after which the node is to be deleted");
	scanf("%d",&item);
	while(ptr->data!=item)
	{
		ptr=ptr->next;
	}
	if(ptr->next==NULL)
	{
		printf("\nUnderflow");
	}
	else if(ptr->next->next==NULL)
	{
		ptr->next=NULL;
	}
	else
	{
		temp=ptr->next;
		ptr->next=temp->next;
		temp->next->prev=ptr;
		free(temp);
		printf("\nNode Deleted");
	}
}

void display()
{
	struct node *ptr,*last;
	printf("\nTraverse from Front\n");
	printf("\n Linked List : \t");
	ptr=head;
	while(ptr!=NULL)
	{
		printf("%d->",ptr->data);
		ptr=ptr->next;
		last=ptr;
	}
	printf("\n\nTraverse from End\n");
	printf("\n10 -> 15 -> 20");
	while(last!=NULL)
	{
		printf("%d->",last->data);
		last=last->prev;
	}
}

void search()
{
	struct node *ptr;
	int item,i=0,flag;
	ptr=head;
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