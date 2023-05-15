#include "lists.h"

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
	int nums[10000], index = 0;

	if (*head == NULL)
		return (1);

	while (head_cp != NULL)
	{
		nums[index] = head_cp->n;
		index++;
		head_cp = head_cp->next;
	}

	reversed = reverse_list(*head);
	index = 0;
	while (reversed != NULL)
	{
		if (reversed->n != nums[index])
			return (0);
		reversed = reversed->next;
		index++;
	}
	return (1);
}
