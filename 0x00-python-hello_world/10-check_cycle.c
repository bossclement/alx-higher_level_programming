#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list - the linked list to check
 * Return: 0 no; 1 yes
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tail = list->next;

	if (list == NULL)
		return (0);
	while (tail)
	{
		if (tail == head)
			return (1);
		tail = tail->next;
	}
	return (0);
}
