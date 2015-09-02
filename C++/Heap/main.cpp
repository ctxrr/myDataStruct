#include <iostream>
#include "heap.h"
using namespace std;

int main(int argc, char const* argv[])
{
    Heap<int> myheap;
    myheap.add(10);
    myheap.add(9);
    myheap.add(30);
    myheap.add(2);
    myheap.add(-1);
    myheap.add(1);
    myheap.showinfo();
    int ret;
    myheap.remove(ret);
    myheap.showinfo();
    myheap.remove(ret);
    myheap.showinfo();
    myheap.remove(ret);
    myheap.showinfo();
    myheap.remove(ret);
    myheap.showinfo();
    myheap.remove(ret);
    myheap.showinfo();

    return 0;
}
