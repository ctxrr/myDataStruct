/**
  ******************************************************************************
  * @file    BinaryTree.h
  * @author  Wayne Hu
  * @date    2015.09.05
  * @brief   This file provides all the headers of the menu functions.
  ******************************************************************************
*/

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef BINARYTREE_H_
#define BINARYTREE_H_

/* Includes ------------------------------------------------------------------*/
#include <iostream>
#include "Tree.h"

/* Exported macro ------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Exported types ------------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/
/* Exported functions ------------------------------------------------------- */
/* Class delcaration ---------------------------------------------------------*/
/* Template definition -------------------------------------------------------*/

template<typename T>
class BTNode : public TNode<T>
{
    public:
        BTNode(T e,BTNode<T> *p):TNode<T>(e) {parent = p;left = right = 0;}
        BTNode<T> *parent,*left,*right;
};

template<typename T>
class BinaryTree : public Tree<T>
{
    public:
        BTNode<T> *root;
        BinaryTree();
        void add_root(const T &item);
        ////Node add_left(const Node & n,const T &item);
        //Node root();
        //Node left(const Node n);
};

template<typename T>
BinaryTree<T>::BinaryTree()
{
    root = 0;
}

template<typename T>
void BinaryTree<T>::add_root(const T &item)
{
     if(this->size==0)
     {
         root = new BTNode<T>(item,0);
         this->size++;
     }
     else
         std::cout<<"Already has root!"<<std::endl;
}

#endif
