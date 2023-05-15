#include "lists.h"
#include <stdio.h>

/**
 * reverse_list - reverse linked list
 * @head: starting point of the linked list
 * Return: pointer of head to new reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *cur = head, *next;
	
	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	return (prev);
}

/**
 * is_palindrome - check if is palindrome
 * @head: starting point of the linked list
 * Return: 0 if it is not a palindrome, 1
  *		if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed, *head_cp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	reversed = reverse_list(*head);
	while (reversed != NULL && head_cp != NULL)
	{
		if (reversed->n != head_cp->n)
			return (0);
		reversed = reversed->next;
		head_cp = head_cp->next;
	}
	return (1);
}
