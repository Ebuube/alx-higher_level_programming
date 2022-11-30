#include "lists.h"
#include "clist.h"
#include "cfuncs.c"

/**
 * check_cycle - checks if there is a cycle in a listint_t list
 * @list: points to a listint_t list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	clist_t *clist = 0;
	int cycle = 0;

	if (!list)
	{
		printf("ERROR: NULL passed as list\n");
		return (cycle);
	}

	for (clist = 0; list; list = list->next)
	{
		if (isin(list, clist))
		{
			cycle = 1;
			break;
		}
		if (!add_node_clist(list, &clist))
		{
			printf("ERROR: could not add node\n");
			return(cycle);
		}
	}
	free_clist(&clist);

	return (cycle);
}
