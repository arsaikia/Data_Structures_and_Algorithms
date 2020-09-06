#include <stdio.h>
#define MAX_SIZE 101

int A[MAX_SIZE];
int top = -1;

void push(int x);
void pop();
void print();

int main()
{
    pop();
    push(1);
    push(3);
    pop();
    push(10);

    return 1;
}

void push(int x)
{
    if (top == MAX_SIZE - 1)
    {
        printf("\nError: Stack Overflow !");
    }
    A[++top] = x;
    print();
}

void pop()
{
    if (top == -1)
    {
        printf("\nError: Empty Stack !");
    }
    else
    {
        top -= 1;
    }
    print();
}

void print()
{
    int i;
    printf("\nStack :\t");
    for (i = 0; i <= top; i++)
    {
        printf("  %d  ", A[i]);
    }
}