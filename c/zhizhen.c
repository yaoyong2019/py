#include <stdio.h>
int main ()
{
    int var1;
    char var2[10];

    printf("Var1�����ĵ�ַ %x\n",&var1);
    printf("var2�����ĵ�ַ %x\n",&var2);

    int var = 10 ;
    int *ip ;
    ip = &var ;
    printf("Address of var variable*����var�ĵ�ַ*: %x\n ",&var);/*����var�ĵ�ַ*/
    printf("Address stored in ip variable*ָ������Ӵ洢�ı����ĵ�ַ*: %x\n",ip);/*ָ������Ӵ洢�ı����ĵ�ַ*/
    printf("Value of *ip variable*ʹ��ָ����ʱ���ֵ*: %d\n",*ip);/*ʹ��ָ����ʱ���ֵ*/

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

    printf("ptr��ֵ��%x\n",p);





    system("pause");

    return 0 ;
    
}