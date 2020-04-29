#include <stdio.h>
int main () {
    int a = 100; int *p1 = &a; int **p2 = &p1;int ***p3 = &p2;
    printf("a=%d ,*p1=%d ,**p2=%d ,***p3=%d\n",a,*p1,**p2,***p3);
    printf("&p2=%#x,p3=%#x\n",&p2,p3);
    printf("&p1=%#x,p2=%#x,*p3=%#x",&p1,p2,*p3);

    system("pause");
    return 0;
}