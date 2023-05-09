#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *head_cp = *head,
	*prev;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (head == NULL || *head == NULL)
	{
		*head = new;
		return (new);
	}
	
	while (head_cp != NULL)
	{
		if (head_cp->n > number)
		{
			prev->next = new;
			new->next = head_cp;
			break;
		}
		prev = head_cp;
		head_cp = head_cp->next;
	}
	return (new);
}
