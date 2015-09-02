#ifndef MYTEMP_H_
#define MYTEMP_H_
template<typename T>
class Heap
{
    private:
        enum {MAX = 10};
        T buffer[MAX];
        int top;
        void upheap(int index);
        int parent(int index);
        int left(int index);
        int right(int index);
        void swap(int index1 , int index2);
        void downheap(int index);
    public:
        Heap();
        bool add(const T &e);
        bool remove(T &e);
        bool isfull();
        bool isempty();
        void showinfo();
};

template<typename T>
Heap<T>::Heap()
{
    top = 0;
}

template<typename T>
bool
Heap<T>::add(const T &e)
{
    if(isfull())
        return false;
    buffer[top++] = e;
    upheap(top-1);
    return true;
}

template<typename T>
bool
Heap<T>::remove(T &e)
{
    if(isempty())
        return false;
    e = buffer[0];
    buffer[0] = buffer[top-1];
    top--;
    downheap(0);
    return true;
}

template<typename T>
bool
Heap<T>::isempty()
{
    return top==0;
}

template<typename T>
bool
Heap<T>::isfull()
{
    return top==MAX-1;
}

template<typename T>
void
Heap<T>::showinfo()
{
    for (int i = 0; i < top; i++)
    {
        std::cout<<buffer[i]<<" ";
    }
    std::cout<<std::endl;
}

template<typename T>
void
Heap<T>::upheap(int index)
{
    if(index)
    {
        if(buffer[index]<buffer[parent(index)])
        {
            swap(index,parent(index));
            upheap(parent(index));
        }
    }
}

template<typename T>
void
Heap<T>::downheap(int index)
{
    if(left(index)<top)
    {
        int mi;
        mi = left(index);
        if(right(index)<top)
        {
            if(buffer[left(index)] > buffer[right(index)])
                mi = right(index);
        }
        if(buffer[index] > buffer[mi])
        {
            swap(mi,index);
            downheap(mi);
        }
    }
}

template<typename T>
int
Heap<T>::parent(int index)
{
     return (index-1)/2;
}

template<typename T>
int
Heap<T>::left(int index)
{
     return 2 * index + 1;
}

template<typename T>
int
Heap<T>::right(int index)
{
     return 2 * index + 2;
}

template<typename T>
void
Heap<T>::swap(int index1, int index2)
{
    T temp;
    temp = buffer[index2];
    buffer[index2] = buffer[index1];
    buffer[index1] = temp;
}

#endif
