#include <stdlib.h>
#include <stdio.h>

// Implement a linked list

// Declerations
void InsertNode(int x);
void PrintList();

struct Node
{
    int data;
    struct Node *next; // In C : to declare a Node pointer we need to use `struct node*`
};

struct Node *head; // A node pointer to store the Head of the linked list

int main()
{
    // Make a linkedList with only the head node
    head = NULL;
    int n, val;
    // Get values from user and Insert it in the Linked List
    printf("Enter how many numbers to be inserted:");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("Enter the %dst value : ", i + 1);
        scanf("%d", &val);
        InsertNode(val);
        PrintList();
    }
}

void InsertNode(int x)
{
    // Allocate memory for a new Node and store its pointer in temp
    struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = x;
    if (head != NULL)
    {
        temp->next = head;
    }
    head = temp;
}

void PrintList()
{
    // Print all elements in linked list
    struct Node *temp = head;
    if (temp != NULL)
    {
        printf("Elements are: ");
    }
    while (temp != NULL)
    {
        printf("%d   ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

