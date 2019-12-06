#include <stdio.h>

int main(){
    int a = 15,b = 25,c = 35;
    int *p = &a;
    int *q;
    q = &a;
    
    *p = c;
    
    printf("%d, %d, %d , %d, %d\n", a, b, c, *p, *q);  //两种方式都可以输出a的值
    system("pause");
    return 0;
}