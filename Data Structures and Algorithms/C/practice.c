#include <stdio.h>
#define MAX_SIZE 101

//-------------------
void print_stack();
void push(int num);

int top = -1;
int A[MAX_SIZE];

int main()
{
    push(1);
    push(3);
    push(2);
    push(0);
    push(9);
    print_stack();
}

void push(int num)
{

    if (top == MAX_SIZE - 1)
    {
        printf("Stack Overflow. Can't Push element!\n");
    }
    else
    {
        top = ++top;
        A[top] = num;
    }
}

void print_stack()
{
    for (int i = top; i > -1; i--)
    {
        printf("%d\n", A[i]);
    }
}