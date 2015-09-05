#include "genSLList.h"
#include "SingleLinkedList.h"
int main(int argc, char const* argv[])
{
    //test code for class intSLList<T>
    IntSLList<int> list;
    list.printAll();
    list.addToHead(1);
    list.addToHead(2);
    list.addToTail(3);
    list.printAll();

    //test code for class Singlelinkedlist<T>
    SingleLinkedList<int> l2;
    l2.addfront(1);
    l2.addfront(2);
    l2.addfront(3);
    l2.showinfo();

    return 0;
}
