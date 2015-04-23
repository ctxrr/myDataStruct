#include <stdio.h>

int main()
{
    int i;

    char *a="hello";
    char *b="world";
    char *c="huwei";
    char *d="ctxrr";

    /*"p" is a pointer to pointer array*/
    char *p[4]={a,b,c,d};
    for (i = 0; i < sizeof(*p); i++)
    {
        printf("%s\n", *(p+i));
    }

    printf("\n");

    /*"q" is a pointer to pointer*/
    char **q=p;
    for (i = 0; i < sizeof(*q); i++)
    {
        printf("%s\n", *q++);
    }

    return 0;
}
