#include "lists.h"

/**
 * is_palindrome - a function that checks if a listint_t list is a palindrome
 * or not
 * @head: address of pointer to head of list
 *
 * Description: an empty list is considered a palindrome
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *forward = NULL;
	listint_t *backward = NULL;
	int is_pal = 1;
	int len = 0, count1 = 0, count2 = 0, extra_step = 0;

	/* if list is empty: then it is palindrome */
	if (!head || !(*head))
	{
		return (is_pal);
	}

	/* calculate length of the list */
	for (forward = (*head); forward; forward = forward->next)
		len++;

	extra_step = len - 1;	/* extra step to take */
	for (forward = (*head), count1 = 0; count1 < (int)(len / 2);
			forward = forward->next, count1++, extra_step -= 2)
	{
		/* traverse to other half of the list */
		for (backward = forward, count2 = 0; count2 < extra_step;
				backward = backward->next, count2++)
			;

		if (backward->n != forward->n)
		{
			is_pal = 0;
			break;
		}
	}

	return (is_pal);
}
