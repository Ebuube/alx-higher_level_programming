#ifndef _CLIST_H
#define _CLIST_H

#include "lists.h"
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * struct clist_s - singly linked list
 * @p: points to type listint_t
 * @next: points to the next node
 *
 * Description: singly linked list node structure for storing pointers
 * to nodes of listint_t
 */
typedef struct clist_s
{
	listint_t *p;
	struct clist_s *next;
} clist_t;

clist_t *add_node_clist(listint_t *p_node, clist_t **p_chead);
bool isin(listint_t *p_node, clist_t *p_chead);
void free_clist(clist_t **p_chead);

#endif	/* _CLIST_H */
