#include <stdio.h>
#include <string.h>
int main(){

    char str[]= "http://c.biancheng.net/c",*pstr;
    pstr = &str;
    int len = strlen(str), i;
    printf("%s\n",str);
    for (i = 0; i<len; i++){
        printf("%c",str[i]);
    }
    printf("\n");
    for(i=0 ;i<len; i++){
        printf("%c",*(pstr+i));
    }
    printf("\n");
    for(i=0 ;i<len; i++){
        printf("%c",*(str+i));
    }
    printf("\n");
    for(i=0 ;i<len; i++){
        printf("%c",*pstr++);
    }



    printf("\n");
    system("pause");
    return 0;
}

