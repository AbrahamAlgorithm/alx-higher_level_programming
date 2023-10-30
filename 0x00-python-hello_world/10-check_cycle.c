#include "lists.h"
/**
 * check_cycle - check if linked list is cyclic
 * @list: the linked list
 * Return: 0 on False and 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (current->next != NULL)
	{
		current = current->next;
	}
	else
	{
		return (0);
	}
	while (current != list)
	{
		if (current->next == NULL)
		{
			return (0);
		}
		current = current->next;
	}
	return (1);
}
