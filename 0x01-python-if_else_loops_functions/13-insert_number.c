#include "lists.h"


/**
 * insert_node - Inserts a node into a sorted singly linked list
 *
 * @head: A reference to the first node in the list
 * @number: The number to insert in the new node
 *
 * Return: The address of the newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *prev = NULL, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);

	newNode->n = number;
	/* First element in the list */
	if (!*head)
	{
		*head = newNode;
		return (newNode);
	}
	if (number < current->n)
	{
		newNode->next = current;
		*head = newNode;
		return (newNode);
	}

	/* Get position to insert when number is less than the element*/
	while (number > current->n)
	{
		prev = current;
		current = current->next;

		/* reaches last node in the list */
		if (!current)
			break;
	}
	/* Insert at the position */
	newNode->next = prev->next;
	prev->next = newNode;

	return (newNode);
}
