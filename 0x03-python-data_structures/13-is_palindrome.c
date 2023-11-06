#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 **/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	else
		return (show_it_is_palind(head, *head));
}

/**
 * show_it_is_palind - a funtion shows weather there is a palindrome
 * @head: head of linked list
 * @tail: tail of linked list
 * Return: integer value
 **/
int show_it_is_palind(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	if (show_it_is_palind(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
