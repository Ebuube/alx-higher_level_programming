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
	listint_t *tmp = NULL;
	int *stack = NULL;
	int is_pal = 1;
	int len = 0, pos = 0;

	/* if list is empty: then it is palindrome */
	if (!head || !(*head))
	{
		return (is_pal);
	}

	/* calculate length of the list */
	for (tmp = (*head); tmp; tmp = tmp->next)
		len++;
	stack = malloc(len * sizeof(int));

	/* load pointers to stack */
	for (tmp = (*head), pos = len - 1; 
			tmp && pos >= 0; tmp = tmp->next, pos--)
	{
		stack[pos] = tmp->n;
	}
	/* check for palindrome */
	for (tmp = (*head), pos = 0; tmp && (pos < len / 2);
			tmp = tmp->next, pos++)
	{
		if (tmp->n != stack[pos])
		{
			is_pal = 0;
			break;
		}
	}

	/* Clean up */
	if (stack != NULL)
		free(stack);

	return (is_pal);
}
