#include "lists.h"
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked
 * list.
 * @head: head
 * @number: number to be inserted
 * Return: address of the new node or NULL of it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t newNode = (listint_s)malloc(sizeof(listint_s));
	newNode->data = newData;
	newNode->next = NULL;

	if (*head == NULL || newData < (*head)->data)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		listint_t current = *head;
		while (current->next != NULL && current->next->data < newData)
		{
			current = current->next;
		}
		newNode->next = current->next;
		current->next = newNode;
	}
i}
