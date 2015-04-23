#include <stdio.h>

int main()
{
    int i;

    char *a="hello";
    char *b="world";
    char *c="huwei";
    char *d="ctxrr";
    char *p[4]={a,b,c,d};
    char **q=p;

    for (i = 0; i < sizeof(*q); i++)
    {
        printf("%s\n", *q++);
    }
    return 0;
}
