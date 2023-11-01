#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *okda = *head, *gded = malloc(sizeof(listint_t));

	if (!gded)
		return (NULL);

	gded->n = number;
	gded->next = NULL;

	if (!okda || gded->n < okda->n)
	{
		gded->next = okda;
		return (*head = gded);
	}

	while (okda)
	{
		if (!okda->next || gded->n < okda->next->n)
		{
			gded->next = okda->next;
			okda->next = gded;
			return (okda);
		}
		okda = okda->next;
	}
	return (NULL);
}
