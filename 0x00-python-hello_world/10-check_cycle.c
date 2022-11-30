#include "lists.h"

/**
 * check_cycle - checks if a listint_t list has a loop
 * @list: points to a listint_t list
 *
 * Description: The function uses two pointers. One moves one step at a time
 * while the second pointer moves two nodes at a time.
 * The logic is that if there is a loop in the list, then the two pointers
 * will definitely meet at a point in the loop. Else, one of them will
 * hit the null pointer
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = 0;
	listint_t *fast = 0;
	int found_loop = 0;

	if (!list)
	{
		/* empty list */
		return (0);
	}

	for (slow = list->next, fast = list->next->next, found_loop = 0;
		slow && fast && fast->next;
		slow = slow->next, fast = fast->next->next)
	{
		if (slow == fast)
		{
			found_loop = 1;
			break;
		}
	}

	return (found_loop);
}
