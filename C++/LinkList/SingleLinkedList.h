/**
  ******************************************************************************
  * @file    SingleLinkedList.h
  * @author  Wayne Hu
  * @version V1.0.0
  * @date    2015.09.05
  * @brief   This file provides all the headers of the menu functions.
  ******************************************************************************
*/

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef SINGLELINKEDLIST_H_
#define SINGLELINKEDLIST_H_

/* Includes ------------------------------------------------------------------*/
#include <iostream>


/* Exported macro ------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Exported types ------------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/
/* Exported functions ------------------------------------------------------- */
/* Class delcaration ---------------------------------------------------------*/
/* Template definition -------------------------------------------------------*/

template<typename T>
class SLLNode
{
    public:
        SLLNode() {next = 0;}
        SLLNode(T e,SLLNode *node) {element = e;next = node;}
        T element;
        SLLNode *next;
};

template<typename T>
class SingleLinkedList
{
    public:
        SingleLinkedList();
        ~SingleLinkedList();
        void addfront(T e);
        void addend(T e);
        void showinfo();
        SLLNode<T> *header,*trailer;
    private:
        int size;

};

template<typename T>
SingleLinkedList<T>::SingleLinkedList()
{
    header = new SLLNode<T>;
    trailer = new SLLNode<T>;
    header->next = trailer;
    size = 0;
}

template<typename T>
SingleLinkedList<T>::~SingleLinkedList()
{
    SLLNode<T> *walker = header->next;
    while(walker!=trailer)
    {
        SLLNode<T> *temp = walker;
        walker = walker->next;
        std::cout<<temp->element<<std::endl;
        delete temp;
    }
    delete header;
    delete trailer;
}

template<typename T>
void SingleLinkedList<T>::addfront(T e)
{
    SLLNode<T> *temp = new SLLNode<T>(e,header->next);
    header->next = temp;
}

template<typename T>
void SingleLinkedList<T>::showinfo()
{
    SLLNode<T> *walker = header->next;
    std::cout<<"List info:[";
    while(walker!=trailer)
    {
        std::cout<<walker->element<<" ";
        walker = walker->next;
    }
    std::cout<<"]"<<std::endl;
}

#endif

