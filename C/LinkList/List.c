#include "List.h"
#include<stdlib.h>
#include<stdio.h>

List *InitList()
{
    List *L;
    L = malloc(sizeof(List));
    L->size = 0;

    L->header  = NewNode(0,NULL);
    L->trailer = NewNode(0,NULL);
    L->header->Next = L->trailer;
    return L;
}

Node *NewNode(ElementType e,Node *next)
{
    Node *N;
    N = malloc(sizeof(Node));
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

int GetSize(List *L)
{
    return L->size;
}

void ShowInfo(List *L)
{
    Node *walk = L->header;
    while (walk != L->trailer)
    {
        printf("%d\n",walk->Element);
        walk = walk->Next;
    }
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

