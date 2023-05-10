#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *head_cp = *head,
	*prev = NULL;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	
	while (head_cp != NULL)
	{
		if (head_cp->n > number)
		{
			if (prev == NULL)
			{
				new->next = *head;
				*head = new;
				break;
			}
			else if (head_cp->next != NULL)
			{
				prev->next = new;
				new->next = head_cp;
				break;
			} else if (head_cp->next == NULL)
			{
				head_cp->next = new;
				break;
			}
		} else if (head_cp->next == NULL)
		{
			head_cp->next = new;
			break;
		}
		prev = head_cp;
		head_cp = head_cp->next;
	}
	return (new);
}
