#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int top=-1;
char stack[20];
int main(){
    char exp[100];
    printf("Enter the expression: ");
    gets(exp);
    for(int i=0; i<strlen(exp); i++){
        if(exp[i]=='{' || exp[i]=='[' || exp[i]=='(')
            {
                push(exp[i]);
            }
        else if (exp[i]=='}' || exp[i]==']' || exp[i]==')')
        {
            if(stack[top]=='[' && exp[i]==']')
                top--;
            if(stack[top]=='{' && exp[i]=='}')
                top--;
            if(stack[top]=='(' && exp[i]==')')
            top--;
        }
    }
        if (top==-1)
            printf("Parenthesis Balanced");
        else
            printf("Parenthesis Unbalanced");


}

void push(char a){
    if(top==-1)
    {
        top++;
        stack[top]=a;
    }
    else
        top++;
        stack[top]=a;
}













