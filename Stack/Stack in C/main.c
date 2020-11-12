//STACK CODE -Rushil Goel

#include<stdio.h>
#include<stdlib.h>
int arr[10], top=-1;
int main()
{
    int choice;
    while(1){
        printf("\n1. PUSH\n2. POP\n3. DISPLAY\n4.EXIT\n\n");
        printf("Enter a choice: ");
        scanf("%d", &choice);
        if (choice==1)
            push(); //printf("Entered 1 ");//
        else if (choice==2)
            pop(); //printf("Entered 2 ");
        else if (choice==3)
            display(); //printf("Entered 3 ");
        else if (choice==4)
            exit(0);
        else
        printf("INVALID CHOICE");
    }
}

void push(){
    int n;
    if (top==9)
        printf("\nStack is full!\n");
    else
        printf("Enter a number to push ");
        scanf("%d", &n);
        top++;
        arr[top]=n;
}
void pop(){
    int n;
    if (top<=-1)
        printf("\nStack is empty!\n");
    else
        printf("Element popped is:%d\n",arr[top]);
        top--;
}

void display(){
    int i;
    if(top<=-1)
    {
    printf("Stack is empty\n");
    }
    else
    {
    for(i=top;i>=0;i--)
    printf("%d\n",arr[i]);
    }
}
