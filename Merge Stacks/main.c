#include<stdio.h>
#include<stdlib.h>
int s1[20]={1,2,3,4,5,6,7,8,9,10};
int s2[20]={5,6,7,8,9};
int top1=9;
int top2 =4;
int main(){
    int ch;
    printf("enter 1 to merge stacks s1 and s2: ");
    scanf("%d", &ch);
    if (ch==1)
        merge();
}
void merge(){
    for(int i=top2; i>=0; i--)
    {
        top1++;
        s1[top1]=s2[i];
    }
        for(int i=top1; i>=0; i--)
    {
        printf("%d\n", s1[i]);
    }

}
