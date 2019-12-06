#include <stdio.h>
int main ()
{
    int var1;
    char var2[10];

    printf("Var1变量的地址 %x\n",&var1);
    printf("var2变量的地址 %x\n",&var2);

    int var = 10 ;
    int *ip ;
    ip = &var ;
    printf("Address of var variable*变量var的地址*: %x\n ",&var);/*变量var的地址*/
    printf("Address stored in ip variable*指针变量钟存储的变量的地址*: %x\n",ip);/*指针变量钟存储的变量的地址*/
    printf("Value of *ip variable*使用指针访问变量值*: %d\n",*ip);/*使用指针访问变量值*/

    int *ptr = NULL;
    int i;
    for (i=0;i<10;i++){
        var2[i] = i + 1;
        printf("%d ",var2[i]);
    }
    int *p;
    p = var2;
    printf("var[0]:%d\n",var2[0]);
    printf("zhizheng+1:%d\n",(*)p[0]);

    printf("ptr的值是%x\n",p);





    system("pause");

    return 0 ;
    
}