#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *tail;

	if (head == NULL || *head == NULL || new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	tail = (*head)->next;
	if (tail == NULL)
		tail = *head;
	while (tail->next)
		tail = tail->next;
	tail->next = new;
	return (new);
}
