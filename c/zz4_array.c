#include <stdio.h>
int main(){
    int arr[] = {99,15,100,888,252};
    int len = sizeof(arr)/sizeof(int);
    int *p = arr;
    int *q = arr;
    int i;
    for (i = 0;i<len;i++){
        printf("%d ",*(arr+i));
        printf("%d ",*(p+i));
        printf("%d ",*q++);
    }
    printf("\n%d, %d, %d, %d, %d\n", *p, *(p+1), *(p+2), *(p+3), *(p+4) );
    /*引入数组指针后，我们就有两种方案来访问数组元素了，一种是使用下标，另外一种是使用指针*/
    system("pause");
    return 0;
}