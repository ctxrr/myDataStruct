/**
  ******************************************************************************
  * @file    Tree.h
  * @author  Wayne Hu
  * @date    2015.09.05
  * @brief   This file provides all the headers of the menu functions.
  ******************************************************************************
*/

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef TREE_H_
#define TREE_H_

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
class TNode
{
    public:
        TNode(T e) {element = e;}
        T element;
};


template<typename T>
class Tree
{
    public:
        Tree();
        int size;
};

template<typename T>
Tree<T>::Tree()
{
    size = 0;
}


#endif
