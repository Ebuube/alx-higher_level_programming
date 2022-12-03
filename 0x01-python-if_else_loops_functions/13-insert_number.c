#include "lists.h"

/**
 * insert_node - inserts a number into a sorted signly linked list
 * @head: address of the pointer to the head
 * @number: the number to include in the list
 *
 * Description: the list is a sorted list
 * Return: pointer to the inserted node
 * else NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = 0, *previous = 0, *current = 0;

	if (!head)
	{
		return (NULL);
	}
	current = (*head);
	tmp = malloc(sizeof(listint_t));
	if (!tmp)
	{
		return (NULL);
	}
	tmp->n = number;	/* initializing value in node */
	for (current = previous = (*head); current; current = current->next)
	{
		if (current->n >= number)
		{
			tmp->next = current;
			if (current != (*head))
				previous->next = tmp;
			else
				(*head) = tmp;
			break;
		}
		previous = current;
	}
	if (current == (*head) && (*head) == NULL)
	{	/* empty list */
		tmp->next = NULL;
		(*head) = tmp;
	}
	if (current == NULL && previous)
	{	/* end of list */
		tmp->next = current;
		previous->next = tmp;
	}

	return (tmp);
}
