#include <stdio.h>
int main(){
    int a = 10, *pa = &a, *paa = &a;
    double b = 99.9, *pb = &b;
    char c = '宁', *pc = &c;
    printf("&a=%#x,&b=%#x,&c=%#x\n",&a,&b,&c);
    printf("pa=%#x,pb=%#x,pc=%#x\n",pa,pb,pc);

    pa++;pb++;pc++;
    printf("pa=%#x,pb=%#x,pc=%#x\n",pa,pb,pc);
    pa-=2;pb-=2;pc-=2;
    printf("pa=%#x,pb=%#x,pc=%#x\n",pa,pb,pc);
    if (pa==paa){
        printf("%d\n",*paa);
    }
    else{
        printf("%d\n",*pa);
    }


    int a1 = 1, b1 = 2, c1 = 3;
    int *p = &c1;
    int i;
    for(i=0; i<12; i++){
        printf("%d, ", *(p+i) );
    }

    system("pause");return 0;
}