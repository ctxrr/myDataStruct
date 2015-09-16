#include <iostream>
#include "BinaryTree.h"

int main(int argc, char const* argv[])
{
    BinaryTree<int> tr1;
    auto r1 = tr1.add_root(1);
    auto r2 = tr1.add_left(r1,2);
    auto r3 = tr1.add_right(r1,3);
    auto r4 = tr1.add_left(r2,4);
    auto r5 = tr1.add_right(r2,5);
    auto r6 = tr1.add_left(r3,6);
    auto r7 = tr1.add_right(r3,7);
    auto r8 = tr1.add_left(r4,8);
    tr1.preorder(tr1.root);

    return 0;
}
