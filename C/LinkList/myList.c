#include "List.h"
#include "myList.h"
#include<stdio.h>

int main(int argc, const char *argv[])
{

    List *mylist = InitList();

     int ret;
     ret=IsEmpty(mylist);
     printf("%d\n",ret);

     Node *n1 = AddFront(mylist,1);
     Node *n2 = AddFront(mylist,2);
     ShowInfo(mylist);
     return 0;
}



