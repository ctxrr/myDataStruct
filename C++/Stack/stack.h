// stack.h -- class definition for the stack ADT
#ifndef STACK_H_
#define STACK_H_

template<typename T>
class Stack
{
private:
    enum {MAX = 10};    // constant specific to class
    T items[MAX];    // holds stack items
    int top;            // index for top stack item
public:
    Stack();
    bool isempty() const;
    bool isfull() const;
    // push() returns false if stack already is full, true otherwise
    bool push(const T & item);   // add item to stack
    // pop() returns false if stack already is empty, true otherwise
    bool pop(T & item);          // pop top into item
};

template<typename T>
Stack<T>::Stack()    // create an empty stack
{
    top = 0;
}

template<typename T>
bool Stack<T>::isempty() const
{
    return top == 0;
}

template<typename T>
bool Stack<T>::isfull() const
{
    return top == MAX;
}

template<typename T>
bool Stack<T>::push(const T & item)
{
    if (top < MAX)
    {
        items[top++] = item;
        return true;
    }
    else
        return false;
}

template<typename T>
bool Stack<T>::pop(T & item)
{
    if (top > 0)
    {
        item = items[--top];
        return true;
    }
    else
        return false;
}
#endif
