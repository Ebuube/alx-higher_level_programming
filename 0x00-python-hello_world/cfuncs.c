#include "clist.h"

/**
 * add_node_clist - adds a node to a clist_t
 * @p_node: listint_t pointer to store in new node
 * @p_chead: address of pointer to head of a clist_t list
 *
 * Return: pointer to newly added node
 * or NULL if function fails
 */
clist_t *add_node_clist(listint_t *p_node, clist_t **p_chead)
{
	clist_t *tmp = 0;

	if (!p_chead || !p_node)
	{
		return (NULL);
	}
	tmp = malloc(sizeof(clist_t));
	if (!tmp)
	{
		return (NULL);
	}
	/* assigning value */
	tmp->p = p_node;

	if (!(*p_chead))
	{
		/* for an empty list */
		tmp->next = NULL;
		(*p_chead) = tmp;
	}
	else
	{
		/* for a non empty list */
		tmp->next = (*p_chead);
		(*p_chead) = tmp;
	}

	return (tmp);
}

/**
 * isin - searches for the value of p_node in a clist_t list
 * @p_node: points to a listint_t node
 * @p_chead: points to head of a clist_t list
 *
 * Return: True if found else False
 */
bool isin(listint_t *p_node, clist_t *p_chead)
{
	clist_t *tmp = NULL;
	bool found = false;

	if (!p_node)
	{
		printf("ERROR: NULL passed to be searched\n");
		return (found);
	}
	for (tmp = p_chead, found = false; tmp; tmp = tmp->next)
	{
		found = (tmp->p == p_node) ? true : false;
		if (found)
		{
			break;
		}
	}

	return (found);
}


/**
 * free_clist - frees a clist_t type and sets its head to NULL
 * @p_chead: address of pointer to head of a clist_t list
 *
 * Return: nothing
 */
void free_clist(clist_t **p_chead)
{
	clist_t *tmp = NULL;

	if (!p_chead)
	{
		return;
	}

	for (tmp = (*p_chead); tmp;)
	{
		tmp = (*p_chead)->next;
		free(*p_chead);
		(*p_chead) = tmp;
	}
	(*p_chead) = NULL;
}
