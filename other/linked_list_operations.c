# include <stdio.h>
# include <stdlib.h>

typedef struct {
    int val;
    void *next;
} Node;

Node *head = NULL;

void addToFront(int val)
{
    Node *node = malloc(sizeof(Node));
    node->val = val;
    if(head == NULL)
    {
        node->next = NULL;
        head = node;
    }
    else
    {
        node->next = head;
        head = node;
    }
}

void addToBack(int val)
{
    Node *node = malloc(sizeof(Node));
    node->val = val;
    if(head == NULL)
    {
        node->next = NULL;
        head = node;
    }
    else
    {
        Node *current = head;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = node;
    }
}

void removeFirst()
{
    if(head != NULL)
    {
        Node *firstNode = head;
        Node *next = head->next;
        free(firstNode);
        head = next;
    }
}

void removeNodeByValue(int val)
{
    if(head != NULL)
    {
        if(head->val == val)
        {
            removeFirst();
            return;
        }
        Node *next = head->next;
        Node *current = head;
        while (next != NULL)
        {
            if (next->val == val)
            {
                current->next = next->next;
                free(next);
                return;
            }
            current = next;
            next = current->next;
        }
    }
}

void insertAt(int position, int val)
{
    if (head == NULL)
    {
        Node *node = malloc(sizeof(Node));
        node->val = val;
        return;
    }
    int currentIdx = 0;
    Node *currentNode = head;
    while (currentIdx <= position && currentNode != NULL)
    {
        if (currentIdx+1 == position)
        {
            Node *node = malloc(sizeof(Node));
            node->val = val;
            Node *next = currentNode->next;
            node->next = next;
            currentNode->next = node;
            return;
        }
        currentIdx+=1;
        Node *next = currentNode->next;
        currentNode = next;
    }
}

void traveseLinkedList(Node *node)
{
    Node *current = node;
    while (current != NULL)
    {
        printf("%d\n", current->val);
        current = current->next;
    }
}

int main()
{
    Node *node1 = malloc(sizeof(Node));
    node1->val = 1;
    Node *node2 = malloc(sizeof(Node));
    node2->val = 2;
    Node *node3 = malloc(sizeof(Node));
    node3->val = 3;
    node1->next = node2;
    node2->next = node3;
    head = node1;
    addToBack(4);
    addToFront(0);
    removeNodeByValue(2);
    insertAt(9, 8);
    traveseLinkedList(head);
    return 0;
}