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
listint_t *reverse_list(listint_t *start)
{
	listint_t *prev = NULL;
	listint_t *curr = start;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a @listint_t list is a palindrome
 *
 * @head: A reference to the pointer to the first node in the list
 *
 * Return: 1 if it a palindome 0 otherwise
 */
int is_palindrome(listint_t **head) {
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half = NULL;
    listint_t *mid_node = NULL, *temp_head, *reversed_second_half;
    int is_pal = 1;

    /* Empty list or single element is a palindrome */
    if (!*head || !(*head)->next)
        return 1;

    /* Finding the middle and end of the first half of the list */
    while (fast && fast->next) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    /* Handling odd number of elements */
    if (fast) {
        mid_node = slow;
        slow = slow->next;
    }

    /* Reversing the second half of the list */
    second_half = reverse_list(slow);

    /* Comparing the first and second halves of the list */
    temp_head = *head;
    while (second_half) {
        if (temp_head->n != second_half->n) {
            is_pal = 0; /* Not a palindrome */
            break;
        }
        temp_head = temp_head->next;
        second_half = second_half->next;
    }

    /* Restoring the original list by reversing the second half again */
    reversed_second_half = reverse_list(second_half);

    /* Reconnecting the first and second halves */
    if (mid_node) {
        prev_slow->next = mid_node;
        mid_node->next = reversed_second_half;
    } else {
        prev_slow->next = reversed_second_half;
    }

    return is_pal;
}
