#include "lists.h"

/**
 * check_cycle - Checks if a singly linkedlist has a cycle in it.
 *
 * @list: The list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	/* Empty list */
	if (!list)
		return (0);

	while (fast->next && fast)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (!fast)
			break;

		/* found a circle */
		if (slow == fast)
			return (1);
	}

	return (0);
}
