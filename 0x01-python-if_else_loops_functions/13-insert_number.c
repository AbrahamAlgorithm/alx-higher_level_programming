#include "lists.h"
/**
 * insert_node - insert node in a sorted linked list
 * @head: the head of the linked list
 * @number: the int value to insert
 * Return: the new linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t **new;
	listint_t *keep;

	keep = malloc(sizeof(listint_t));
	new = malloc(sizeof(listint_t));
	if (keep == NULL || new == NULL)
	{
		return (NULL);
	}
	keep->n = number;
	keep->next = NULL;
	if (*head == NULL)
	{
		*head = keep;
	}
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
			{
				*new = current->next;
				keep->next = current->next;
				(*new)->next = keep;
				return (*head);
			}
			current = current->next;
		}
		current->next = keep;
		return (*head);
	}
	return (NULL);
}
