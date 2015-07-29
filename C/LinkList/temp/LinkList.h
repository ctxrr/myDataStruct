#ifndef _LINKLIST_H_
#define _LINKLIST_H_


typedef struct _tag_LinkListNode *LinkListNode;
typedef int ElementType;
typedef struct _tag_LinkList
{
    LinkListNode header;
    int length;
} TLinkList;


LinkList LinkList_Create();

void LinkList_Destroy(LinkList list);

void LinkList_Clear(LinkList list);

int LinkList_Length(LinkList list);

int LinkList_Insert(LinkList list, LinkListNode node, int pos);

LinkListNode LinkList_Get(LinkList list, int pos);

LinkListNode LinkList_Delete(LinkList list, int pos);

#endif
