#include <iostream>
template<typename T>
class BinaryTree {
    private:
        class Node
        {
            private:
                Node *parent,left,right;
                T item;
            public:
                Node();
                Node(Node &p,T &e);
                Node(T &e);
        };
        Node _root;
        int _num;
    public:
        BinaryTree();
        Node add_root(const T &item);
        //Node add_left(const Node & n,const T &item);
        Node root();
        Node left(const Node n);
};

//constructor of Node()
template<typename T>
BinaryTree<T>::Node::Node() {
    parent = nullptr;
    left = nullptr;
    right = nullptr;
}

//constructor of Node(Node,T)
template<typename T>
BinaryTree<T>::Node::Node(Node &p,T &e)
{
    parent = &p;
    left = nullptr;
    right = nullptr;
    item = e;
}

template<typename T>
BinaryTree<T>::Node::Node(T &e)
{
    parent = nullptr;
    left = nullptr;
    right = nullptr;
    item = e;
}

template<typename T>
BinaryTree<T>::BinaryTree()
{
    _num = 0;
}

template<typename T>
typename BinaryTree<T>::Node
BinaryTree<T>::add_root(const T &item)
{
     if(_num!=0)
     {
         _root = Node(item);
     }
     return &_root;
}

int main(int argc, char const* argv[])
{
    //BinaryTree<int> tree = new BinaryTree<int>;
    BinaryTree<int> tree;
    return 0;
}
