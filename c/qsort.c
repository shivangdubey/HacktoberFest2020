#include <stdio.h>
#include <stdlib.h>
#include <string.h>

 struct info
{
	int rn;
	char fname[10];
	char lname[10];
	char dob[20];
	char place[10];
	char work[10];	
};


int struct_cmp_by_work(const void *a, const void *b) 
{ 
    struct info *ia = (struct info*)a;
    struct info *ib = (struct info *)b;
    /*if( strcmp(ia->work, ib->work)==0)
    {
        return struct_cmp_by_rn(ia,ib);
        //return 0;
    }
    else */
    return strcmp(ia->work, ib->work);
	/* strcmp functions works exactly as expected from
	comparison function */ 
}
int struct_cmp_by_place(const void *a, const void *b) 
{ 
    struct info *ia = (struct info*)a;
    struct info *ib = (struct info *)b;
    /*if( strcmp(ia->place, ib->place)==0)
    {
        return struct_cmp_by_work(ia,ib);
        //return 0;
    }
    else*/ 
    return strcmp(ia->place, ib->place);
	/* strcmp functions works exactly as expected from
	comparison function */ 
}


int struct_cmp_by_dob(const void *a, const void *b) 
{ 
    struct info *ia = (struct info*)a;
    struct info *ib = (struct info *)b;
    /*if( strcmp(ia->dob, ib->dob)==0)
    {
        return struct_cmp_by_place(ia,ib);
        //return 0;
    }
    else */
    return strcmp(ia->dob, ib->dob);
	/* strcmp functions works exactly as expected from
	comparison function */ 
} 
int struct_cmp_by_lname(const void *a, const void *b) 
{ 
    struct info *ia = (struct info*)a;
    struct info *ib = (struct info *)b;
    /*if( strcmp(ia->lname, ib->lname)==0)
    {
        return struct_cmp_by_dob(ia,ib);
        //return 0;
    }
    else */
    return strcmp(ia->lname, ib->lname);
	/* strcmp functions works exactly as expected from
	comparison function */ 
} 
int struct_cmp_by_fname(const void *a, const void *b) 
{ 
    struct info *ia = (struct info*)a;
    struct info *ib = (struct info *)b;
    /*if( strcmp(ia->fname, ib->fname)==0)
    {
        return struct_cmp_by_lname(ia,ib);
        //return 0;
    }
    else */
    return strcmp(ia->fname, ib->fname);

	/* strcmp functions works exactly as expected from
	comparison function */ 
} 

int struct_cmp_by_rn(const void *p, const void *q) 
{
    int l = ((struct info *)p)->rn;
    int r = ((struct info *)q)->rn; 
    return (l - r);
}

int main()
{
   struct info *s;
   int d,i=0;
   scanf("%d",&d);
   printf("%d\n",d);
    do
   {
   		
   		printf("%d\n",i);
	    scanf("%d",&s[i].rn);
	    scanf("%s",s[i].fname);
		scanf("%s",s[i].lname);
        scanf("%s",s[i].dob);
        printf("%s\n",s[i].dob);
   	    scanf("%s",s[i].place);
	    scanf("%s",s[i].work);
   		 i++;
   } while(!feof(stdin));
    
   int l=i;
   if (d==1)
   {
   	 	qsort(s,l,sizeof( struct info),struct_cmp_by_rn);
   }
   
   if(d==2)
   { 
     	qsort(s,l,sizeof( struct info),struct_cmp_by_fname);
   }
   if(d==3)
   { 
     	qsort(s,l,sizeof( struct info),struct_cmp_by_lname);
   }
   if(d==4)
   { 
     	qsort(s,l,sizeof( struct info),struct_cmp_by_dob);
   }
   if(d==5)
   { 
     	qsort(s,l,sizeof( struct info),struct_cmp_by_place);
   }
   if(d==6)
   { 
     	qsort(s,l,sizeof( struct info),struct_cmp_by_work);
   }
    printf("\n");
   for(int j=1;j<l+1;j++)
   {    printf("%d\n",j);
   		printf("rn=%d fname=%s lname=%s dob=%s place=%s work=%s\n",s[j].rn,s[j].fname,s[j].lname,s[j].dob,s[j].place,s[j].work);
   }

}
