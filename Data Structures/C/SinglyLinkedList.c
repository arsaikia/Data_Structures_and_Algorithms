#include <stdio.h>
#include <stdlib.h>

// DEfinitions:
void InsertNode(int x);
void PrintElements();
void InsertNodeAt(int val, int pos);
void ReverseLinkList();
void PrintReverse();

// Create a Node Struct:
//      This is a single Node for the Linked List that has a Data part and a Node pointer to point to the next node
struct Node
{
    int data;
    struct Node *next;
};

// Create a pointer to store the first location of LL: THE HEAD
struct Node *head = NULL; // Curently points to nowhere

// The main function; Program Executes from here
int main()
{

    // Promp user for input
    int selection, count, val;

    while (1)
    {
        printf("\nEnter what to do ?\n\t"
               "1. Insert a node at end of list\n\t"
               "2. Insert at selected position\n\t"
               "3. Reverse Linked List\n\t"
               "4. Print All Elements\n\t"
               "5. Print All Elements in Reverse\n\t"
               "6. Exit\n\t");
        scanf("%d", &selection);

        switch (selection)
        {
        case 1:
            printf("Enter number of values you want to store : ");
            scanf("%d", &count);

            for (int i = 0; i < count; i++)
            {
                printf("\nEnter value %d  : ", i + 1);
                scanf("%d", &val);
                InsertNode(val);
            }
            PrintElements();
            continue;
        case 2:
            InsertNodeAt(100, 2);
            PrintElements();
            continue;
        case 3:
            ReverseLinkList();
            continue;
        case 4:
            PrintElements();
            continue;
        case 5:
            PrintReverse(head);
            continue;
        default:
            return 1;
        };
    }
}

void InsertNode(int x)
{

    // A new memory allocation for a node stored in tempNode pointer
    struct Node *tempNode = (struct Node *)(malloc(sizeof(struct Node)));

    tempNode->data = x;
    if (head != NULL)
    {
        //tempNode->next = head;
        //head->next = tempNode;
        struct Node *t1 = head;
        while (t1->next != NULL)
        {
            t1 = t1->next;
        }
        t1->next = tempNode;
    }
    else
    {
        head = tempNode;
    }
}

void InsertNodeAt(int val, int pos)
{

    struct Node *temp1 = (struct Node *)(malloc(sizeof(struct Node)));

    temp1->data = val;

    if (head == NULL)
    {
        head = temp1;
    }
    else
    {
        struct Node *temp2 = head;
        int index = 1;

        while ((index < pos - 1) && (temp2->next != NULL))
        {
            index += 1;
            temp2 = temp2->next;
        }

        temp1->next = temp2->next;
        temp2->next = temp1;
    }
}

void ReverseLinkList()
{

    struct Node *current, *prev, *next;
    current = head;
    prev = NULL;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    head = prev;
    PrintElements();
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

void PrintReverse(struct Node *temp)
{
    struct Node *tempHead = temp;

    if (tempHead == NULL)
    {
        return;
    }

    PrintReverse(tempHead->next);

    printf("%d\t", tempHead->data);
}