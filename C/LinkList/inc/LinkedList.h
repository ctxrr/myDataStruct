#ifndef _List_H
#define _List_H

typedef int ElementType;

typedef struct Node
{
    ElementType Element;
    struct Node *Next;
}Node;

typedef struct LinkedList
{
	Node *header;
	Node *trailer;
	int size;
}List;

List *InitList();
Node *NewNode(ElementType e,Node *next);
int IsEmpty(List *L);
Node *AddFront(List *L,ElementType e);
int GetSize(List *L);
void ShowInfo(List *L);
void *DelFront(List *L);
//void Insert(ElementType e,List *L,Node *P);
// int IsLast(Position P,List L);
// Position Find(ElementType X,List L);
// void Delete(ElementType X,List L);
// Position FindPrevious(ElementType X,List L);
// void Insert(ElementType X,List L,Position P);
// void DeleteList(List L);
// Position Header(List L);
// Position First(List L);
// Position Advance(Position P);
// ElementType Retrieve(Position P);

#endif
