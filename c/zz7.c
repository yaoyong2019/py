#include <stdio.h>

int max(int *intarr,int len){
    int i, maxv = intarr[0];
    for(i=1;i<len;i++){
        if (maxv<intarr[i]) {
            maxv=intarr[i];}
    }
    return maxv;
    
}
int main(){
    
    int nums[6],i;
    int len=sizeof(nums)/sizeof(int);
    for (i=0;i<len;i++){
        scanf("%d",nums+i);
    }
    printf("max value is %d\n",max(nums,len));
    system("pause");
    return 0;
}