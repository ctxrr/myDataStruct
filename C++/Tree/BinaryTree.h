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
        BTNode<T> *add_root(const T &item);
        BTNode<T> *add_left(BTNode<T> *n,const T &item);
        BTNode<T> *add_right(BTNode<T> *n,const T &item);
        void preorder(BTNode<T> *root);
};

template<typename T>
BinaryTree<T>::BinaryTree()
{
    root = 0;
}

template<typename T>
BTNode<T> *
BinaryTree<T>::add_root(const T &item)
{
     if(this->size==0)
     {
         root = new BTNode<T>(item,0);
         this->size++;
     }
     else
         std::cout<<"Already has root!"<<std::endl;
     return root;
}

template<typename T>
BTNode<T> *
BinaryTree<T>::add_left(BTNode<T> *n,const T &item)
{
    if(n->left)
         std::cout<<"Already has left!"<<std::endl;
    else
    {
        auto node = new BTNode<T>(item,n);
        n->left = node;
        this->size++;
    }
    return n->left;
}

template<typename T>
BTNode<T> *
BinaryTree<T>::add_right(BTNode<T> *n,const T &item)
{
    if(n->right)
         std::cout<<"Already has right!"<<std::endl;
    else
    {
        auto node = new BTNode<T>(item,n);
        n->right = node;
        this->size++;
    }
    return n->right;
}

template<typename T>
void
BinaryTree<T>::preorder(BTNode<T> *root)
{
    std::cout<<root->element;
    if(root->left)
        preorder(root->left);
    if(root->right)
        preorder(root->right);
}

#endif

