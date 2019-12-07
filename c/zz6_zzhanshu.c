#include <stdio.h>
void swap(int *p1,int *p2){
    int temp;
    temp=*p1;*p1=*p2;*p2=temp;
}

int main(){
    int a = 66, b = 99;
    swap(&a,&b);
    printf("a=%d, b=%d\n",a,b);

    
    system("pause");
    return 0;
}