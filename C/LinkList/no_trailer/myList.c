#include <stdio.h>
#include "List.h"
int main(int argc, const char *argv[])
{
    Node *myList;
    myList = InitList();
    printf("is empty:%d\n",IsEmpty(myList));
    AddFront(myList,1);
    printf("is empty:%d\n",IsEmpty(myList));
    return 0;
}
