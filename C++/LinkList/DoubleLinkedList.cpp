#include <iostream>
#include "DoubleLinkedList.h"

using namespace std;

//----------------------------
class obj {

    public:
        obj():a(10),b(8){}
        obj(int m,int n):a(m),b(n){}
        friend ostream & operator<<(ostream &os,obj &e);
        int a;
        int b;
};

ostream & operator<<(ostream &os,obj &e){
    os<<e.a*e.b;
    return os;
}
//----------------------------

int main(int argc, char const* argv[])
{
    auto list = DoubleLinkedList<int>();
    list.add_front(5);
    list.add_front(6);
    list.add_front(7);

    list.show();

    auto li = DoubleLinkedList<obj>();
    auto r1 = obj(1,2);
    auto r2 = obj(3,4);
    auto r3 = obj(5,6);
    auto r4 = obj();
    li.add_front(r1);
    li.add_front(r2);
    li.add_front(r3);
    li.add_front(r4);
    li.show();
    return 0;
}
