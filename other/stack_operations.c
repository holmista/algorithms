# include <stdio.h>
# include <stdlib.h>

int stack[10] = {0};
int top = 0;
int bottom = 0;

void add(int value)
{
    if (top == 9) return;
    stack[top] = value;
    top++;
}

void pop()
{
    if (top == 0) return;
    stack[top] = 0;
    top--;
}

void printStack()
{
    for(int i=0; i<top;i++)
    {
        printf("%d\n", stack[i]);
    }
}

int main()
{
    add(1);
    add(2);
    add(3);
    pop();
    printStack();
    return 0;
}