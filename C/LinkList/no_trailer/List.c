#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "List.h"

Node *InitList()
{
    Node *newlist;
    newlist = NULL;
    return newlist;
}

int IsEmpty(Node *N)
{
    return N == NULL;
}

Node *AddFront(Node *N,ElementType e)
{
    Node *new,*next;
    new = (Node *)malloc(sizeof(Node));
    memset(new,0,sizeof(Node));
    new->Element = e;

    if(N==NULL)
    {
        N = (Node *)malloc(sizeof(Node));
        memset(N,0,sizeof(Node));
        N->Next = new;
        new->Next = NULL;
    }
    else
    {
        next = N->Next;
        N->Next = new;
        new->Next = next;
    }
   return new;
}

int GetSize(Node *N)
{
    int size = 0;
    Node *walk = N;
    while(walk!=NULL)
    {
        size++;
        walk = walk->Next;
    }
    return size;
}
