#include "inc/LinkedList.h"
#include "inc/myList.h"
#include<stdio.h>

int main(int argc, const char *argv[])
{

    List *mylist = InitList();

    Node *n1 = AddFront(mylist,1);
    Node *n2 = AddFront(mylist,2);
    ShowInfo(mylist);
    printf("size:%d\n", GetSize(mylist));
    return 0;
}



