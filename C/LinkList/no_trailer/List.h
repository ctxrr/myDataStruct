#ifndef _LIST_H_
#define _LIST_H_

typedef int ElementType;
typedef struct Node
{
    ElementType Element;
    struct Node *Next;
}Node;
//typedef Node List;

Node *InitList();
int IsEmpty(Node *N);
Node *AddFront(Node *N,ElementType e);
int GetSize(Node *N);
#endif
