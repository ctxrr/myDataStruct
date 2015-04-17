#include "List.h"
#include "myList.h"
#include<stdio.h>

void main()
{
    List mylist;
    Insert(4,mylist,mylist);
    int ret;
    ret=IsEmpty(mylist);
    printf("%d\n",ret);
}



