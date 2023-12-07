#include "lists.h"


/**
 * reverse_values - Initializes an array to the data in @listint_t
 * and reverses the array
 *
 * @head: A pointer to the first node in @listint_t
 * @size: Number of nodes in @listint_t
 *
 * Return: An array of integers
 */
int *reverse_values(listint_t *head, int size)
{
	int i, j, *numbers = malloc(sizeof(int) * size);

	if (!numbers)
		return (NULL);

	/* initialize array */
	for (i = 0; i < size; i++)
	{
		numbers[i] = head->n;
		head = head->next;
	}
	/* reverse array */
	for (i = 0, j = --size; i < j; i++, j--)
	{
		/* Swap */
		int temp = numbers[i];

		numbers[i] = numbers[j];
		numbers[j] = temp;
	}

	return (numbers);
}

/**
 * is_palindrome - Checks if a @listint_t list is a palindrome
 *
 * @head: A reference to the pointer to the first node in the list
 *
 * Return: 1 if it a palindome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int arraySize = 0, i, *numbers = NULL;
	listint_t *temp = NULL;

	/* get number of nodes */
	temp = *head;
	while (temp)
	{
		arraySize++;
		temp = temp->next;
	}
	/* initialize and reverse array */
	if (arraySize)
	{
		numbers = reverse_values(*head, arraySize);
		if (!numbers)
			return (0);
	}
	i = 0;
	temp = *head;
	while (temp) /* compare */
	{
		/* Not equal to it revered values form not a palindrome */
		if (numbers[i] != temp->n)
			return (0);

		i++;
		temp = temp->next;
	}

	free(numbers);
	return (1);
}
