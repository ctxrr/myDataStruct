//************************  genSLList.h  **************************

#ifndef GEN_LINKED_LIST
#define GEN_LINKED_LIST

#include <iostream>
using namespace std;

template<typename T>
class IntSLLNode {
public:
    IntSLLNode() {
        next = 0;
    }
    IntSLLNode(int el, IntSLLNode *ptr = 0) {
        info = el; next = ptr;
    }
    int info;
    IntSLLNode *next;
};

template<typename T>
class IntSLList {
public:
    IntSLList() {
        head = tail = 0;
    }
    ~IntSLList();
    int isEmpty() {
        return head == 0;
    }
    void addToHead(T);
    void addToTail(T);
    T  deleteFromHead(); // delete the head and return its info;
    T  deleteFromTail(); // delete the tail and return its info;
    void deleteNode(T);
    bool isInList(T) const;
    void printAll() const;
private:
    IntSLLNode<T> *head, *tail;
};

template<typename T>
IntSLList<T>::~IntSLList() {
    for (IntSLLNode<T> *p; !isEmpty(); ) {
        p = head->next;
        delete head;
        head = p;
    }
}

template<typename T>
void IntSLList<T>::addToHead(T el) {
    head = new IntSLLNode<T>(el,head);
    if (tail == 0)
       tail = head;
}

template<typename T>
void IntSLList<T>::addToTail(T el) {
    if (tail != 0) {      // if list not empty;
         tail->next = new IntSLLNode<T>(el);
         tail = tail->next;
    }
    else head = tail = new IntSLLNode<T>(el);
}

template<typename T>
T IntSLList<T>::deleteFromHead() {
    T el = head->info;
    IntSLLNode<T> *tmp = head;
    if (head == tail)     // if only one node on the list;
         head = tail = 0;
    else head = head->next;
    delete tmp;
    return el;
}

template<typename T>
T IntSLList<T>::deleteFromTail() {
    T el = tail->info;
    if (head == tail) {   // if only one node on the list;
         delete head;
         head = tail = 0;
    }
    else {                // if more than one node in the list,
         IntSLLNode<T> *tmp; // find the predecessor of tail;
         for (tmp = head; tmp->next != tail; tmp = tmp->next);
         delete tail;
         tail = tmp;      // the predecessor of tail becomes tail;
         tail->next = 0;
    }
    return el;
}

template<typename T>
void IntSLList<T>::deleteNode(T el) {
    if (head != 0)                     // if non-empty list;
         if (head == tail && el == head->info) { // if only one
              delete head;                       // node on the list;
              head = tail = 0;
         }
         else if (el == head->info) {  // if more than one node on the list
              IntSLLNode<T> *tmp = head;
              head = head->next;
              delete tmp;              // and old head is deleted;
         }
         else {                        // if more than one node in the list
              IntSLLNode<T> *pred, *tmp;
              for (pred = head, tmp = head->next; // and a non-head node
                   tmp != 0 && !(tmp->info == el);// is deleted;
                   pred = pred->next, tmp = tmp->next);
              if (tmp != 0) {
                   pred->next = tmp->next;
                   if (tmp == tail)
                      tail = pred;
                   delete tmp;
              }
         }
}

template<typename T>
bool IntSLList<T>::isInList(T el) const {
    IntSLLNode<T> *tmp;
    for (tmp = head; tmp != 0 && !(tmp->info == el); tmp = tmp->next);
    return tmp != 0;
}

template<typename T>
void IntSLList<T>::printAll() const {
    for (IntSLLNode<T> *tmp = head; tmp != 0; tmp = tmp->next)
        cout << tmp->info << " ";
	cout << endl;
}

#endif
