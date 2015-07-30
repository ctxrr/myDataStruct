#include "inc/LinkedList.h"
#include<stdlib.h>
#include<stdio.h>
#include <string.h>

List *InitList()
{
    List *L;
    L = (List *)malloc(sizeof(List));
    memset(L,0,sizeof(List));
    L->size = 0;

    L->header  = NewNode(0,NULL);
    L->trailer = NewNode(0,NULL);
    L->header->Next = L->trailer;
    return L;
}

Node *NewNode(ElementType e,Node *next)
{
    Node *N;
    N = (Node *)malloc(sizeof(Node));
    memset(N,0,sizeof(Node));
    N->Element = e;
    N->Next = next;
    return N;
}

int IsEmpty(List *L)
{
    return L->size == 0;
}

Node *AddFront(List *L,ElementType e)
{
    Node *new = NewNode(e,L->header->Next);
    L->header->Next = new;
    L->size++;
    return new;
}

void *DelFront(List *L)
{
    if(!IsEmpty(L))
    {
        Node *old = L->header->Next;
        L->header->Next = old->Next;
        free(old);
        L->size--;
    }
    else
    {
        printf("List is empty!\n");
    }
}

int GetSize(List *L)
{
    return L->size;
}

void ShowInfo(List *L)
{
    printf("info:[");
    Node *walk = L->header->Next;
    while (walk != L->trailer)
    {
        printf("%d ",walk->Element);
        walk = walk->Next;
    }
    printf("]\n");
}
// int IsLast(Position P,List L)
// {
//     return P->Next ==NULL;
// }

// Position Find(ElementType X,List L)
// {
//     Position P;

//     P=L->header->Next;
//     while(P!=NULL && P->Element !=X)
//         P = P->Next;

//     return P;
// }

// void Delete(ElementType X ,List L)
// {
//     Position P,TmpCell;

//     P=FindPrevious(X,L);

//     if(!IsLast(P,L))
//     {
//         TmpCell = P->Next;
//         P->Next = TmpCell->Next;
//         free(TmpCell);
//     }
// }

// Position FindPrevious(ElementType X,List L)
// {
//     Position P;

//     P=L->header;
//     while(P->Next !=NULL && P->Next->Element !=X)
//         P=P->Next;

//     return P;
// }

/*void Insert(ElementType e,List *L,Node *P)*/
/*{*/
     /*Node *TmpCell = malloc(sizeof(Node));*/
     /*if(TmpCell==NULL)*/
     /*{*/
         /*printf("Failed to create new node!");*/
     /*}*/

     /*TmpCell->Element = e;*/
     /*TmpCell->Next = P->Next;*/
     /*P->Next = TmpCell;*/
     /*L->size++;*/
/*}*/

// void DeleteList(List L)
// {
//     Position P,Tmp;

//     P = L->header->Next;
//     L->header->Next = NULL;
//     while(P !=NULL)
//     {
//         Tmp=P->Next;
//         free(P);
//         P=Tmp;
//     }
// }

