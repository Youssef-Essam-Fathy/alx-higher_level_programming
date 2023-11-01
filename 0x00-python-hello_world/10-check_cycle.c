#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return:  0 if there is no cycle, 1 if there is a cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *down = list, *higher = list;

	while (higher && higher->next)
	{
		down = down->next;
		higher = higher->next->next;
		if (down == higher)
			return (1);
	}
	return (0);
}
