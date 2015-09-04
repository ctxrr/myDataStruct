#ifndef BINARYTREE_H_
#define BINARYTREE_H_
template<typename T>
class BinaryTree {
    private:
        Node root;
        int num;
        class Node {
            private:
                Node *parent,left,right;
                T item;
            public:
                Node();
        };
        Node::Node() {

        }
    public:
        BinaryTree();
        void add_left(T &item);
        Node & left(const Node n);
};
BinaryTree::BinaryTree() {

}
#endif
