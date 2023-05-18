#include "lists.h"
#include <stdio.h>


/**
 * print_dlistint - prints all elements of the list
 * @h: starting point of the list
 * Return: number of nodes in the list
 */

size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *cp = (dlistint_t *)h;
	size_t nodes = 0;

	while (cp)
	{
		printf("%d\n", cp->n);
		cp = cp->next;
		nodes++;
	}
	return (nodes);
}
