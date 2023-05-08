#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the linked list to check
 * Return: 0 no; 1 yes
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tail = list;

	while (tail != NULL && head != NULL && head->next != NULL)
	{
		tail = tail->next;
		head = head->next->next;
		if (tail == head)
			return (1);
	}
	return (0);
}
