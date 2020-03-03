#include <stdio.h>
#include <stdlib.h>

// DEfinitions:
void InsertNode(int x);
void PrintElements();
// void InsertNodeAt(int val, int pos);
// void ReverseLinkList();
// void PrintReverse();

struct Node
{
    int data;
    struct Node *prev;
    struct Node *next;
};

struct Node *head;

int main()
{
    head = NULL;
    InsertNode(10);
    InsertNode(5);
    InsertNode(15);
    InsertNode(102);
    InsertNode(121);
    PrintElements();
}

void InsertNode(int x)
{

    struct Node *tempHead = head;
    struct Node *newNode = (struct Node *)(malloc(sizeof(struct Node)));
    newNode->data = x;

    if (tempHead == NULL)
    {
        tempHead = newNode;
        newNode->prev = NULL;
        newNode->next = NULL;
        head = tempHead;
    }
    else
    {
        while (tempHead->next != NULL)
        {
            tempHead = tempHead->next;
        }

        newNode->prev = tempHead;
        tempHead->next = newNode;
    }
    // else
    // {
    //     while (tempHead != NULL)
    //     {
    //         tempHead = tempHead->next;
    //     }
    //     tempHead->next = newNode;
    //     // tempHead = tempHead->next;
    //     newNode->prev = tempHead->next;
    //     while (tempHead->prev != NULL)
    //     {
    //         /* code */
    //         tempHead = tempHead->prev;
    //     }
    // }
    //head = tempHead;
    // tempHead = NULL;
}

void PrintElements()
{

    struct Node *temp = head;

    while (temp != NULL)
    {
        printf("%d \t", temp->data);
        temp = temp->next;
    }
    printf("\n");
}