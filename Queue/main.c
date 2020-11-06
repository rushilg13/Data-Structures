#include<stdio.h>
#include<stdlib.h>
int arr[10], front=-1, end = -1;
int main(){
    int choice;
    while(1){
    printf("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n");
    scanf("%d", &choice);
    if (choice==1)
        enqueue();
    else if (choice==2)
        dequeue();
    else if (choice==3)
        display();
    else if(choice==4)
        exit(0);
    }
}

void enqueue(){
    int n;
    if (end==9)
        printf("Queue is Full!");
    else
    {
        front=0;
        printf("Enter number to Enqueue: ");
        scanf("%d", &n);
        end ++;
        arr[end]=n;
    }
}
void dequeue(){
    int n;
    if (front==-1 || front>end)
        printf("Queue is Empty!");
    else
    {
        printf("Number dequeued is: %d", arr[front]);
        front ++;
    }
}
void display(){
    int i;
    if(front==-1)
        printf("Queue is empty!");
    else
    {
        for(i=front; i<=end; i++)
        printf("\n%d",arr[i]);
    }
}

