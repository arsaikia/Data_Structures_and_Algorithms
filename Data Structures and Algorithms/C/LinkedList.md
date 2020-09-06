#include <stdlib.h>
#include <stdio.h>
// Implementation of Linked-List(Singly linked)
// A linked list contains nodes. Each node cotains a data section and a pointer to the next node
// We only keep the address of the first node(Head Node)

// This is the node to store data and stre pointer to next node
struct Node
{
    int data;
    struct Node *next;
};

// We need to store the head node location : Pinter to the head Node(say head)
// To create a Node pointer variable we have to use `struct Node*`
struct Node *head;  // Global Variable named head which is of pointer type `struct node*`
void Insert(int x); // Function o insert a new node and data x at the end of the linked-list
void Print();       // Prints all the data in the linked-list

int main()
{
    // make an empty linked-list by making the variable head as null ( Head stores the firt pointer locaion of the linked list)
    head = NULL;
    // Prompt user for numbers to be inserted in the ll
    printf("How many numbers ?\n");
    int n, x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("Enter the Number : ");
        scanf("%d", &x);

        Insert(x);
        Print();
    }
}

void Insert(int x)
{
    struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = x;
    if (head != NULL)
    {
        temp->next = head;
    }
    head = temp;
}

void Print()
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d \t", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
