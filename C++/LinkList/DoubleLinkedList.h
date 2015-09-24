/**
  ******************************************************************************
  * @file    DoubleLinkedList.h
  * @author  Wayne Hu
  * @date    2015.09.05
  * @brief   This file provides all the headers of the menu functions.
  ******************************************************************************
*/

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef DOUBLELINKEDLIST_H_
#define DOUBLELINKEDLIST_H_

/* Includes ------------------------------------------------------------------*/
#include <iostream>

/* Template definition -------------------------------------------------------*/
template<typename T>
class DLLNode {
    public:
        DLLNode(const T &e,DLLNode<T> *next,DLLNode<T> *prev) {
            this->prev = prev;
            this->next = next;
            element = new T;
            memcpy(element,&e,sizeof(T));
        }
        DLLNode() = default;
        ~DLLNode() {delete element;}

        T *element;
        DLLNode *prev,*next;
};

template<typename T>
class DoubleLinkedList {

    public:
        DoubleLinkedList(){
            size = 0;
            header = new DLLNode<T>;
            trailer = new DLLNode<T>;
            header->next = trailer;
            trailer->prev = header;
        }
        ~DoubleLinkedList();
        DLLNode<T>* add_front(const T &e);
        void show();
        int size;
        DLLNode<T> *header,*trailer;
};

/**
 *
 */
template<typename T>
DoubleLinkedList<T>::~DoubleLinkedList(){
    auto walk = header->next;
    while(walk!=trailer){
        auto temp = walk->next;
        delete walk;
        walk = temp;
    }
}

/**
 *
 */
template<typename T>
DLLNode<T> *
DoubleLinkedList<T>::add_front(const T &e){
    auto n = new DLLNode<T>(e,header->next,header);
    header->next->prev = n;
    header->next = n;
    size++;
    return n;
}

/**
 *
 */
template<typename T>
void
DoubleLinkedList<T>::show(){
    auto walk = header->next;
    while(walk!=trailer){
        std::cout<<*walk->element<<" ";
        walk = walk->next;
    }
    std::cout<<std::endl;
}

#endif
