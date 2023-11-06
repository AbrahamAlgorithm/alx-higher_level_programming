#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - check if linked list is palindrome
 * @head: the adress to the linked list
 * Return: 1 if true and 0 if not
 */
int is_palindrome(listint_t **head)
{
	int n, i, a, li;
	int *name;
	listint_t *current;
	listint_t  *new;

	current = *head;
	if (*head == NULL)
	{
		return (1);
	}
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	name = malloc(sizeof(int) * n);
	if (name == NULL)
	{
		return (0);
	}
	new = *head;
	for (i = 0; new != NULL && i < n; i++)
	{
		name[i] = new->n;
		new = new->next;
	}
	for (a = 0; a < n/2; a++)
	{
		li = n - a - 1;
		if (name[a] != name[li])
		{
			free(name);
			return (0);
		}
	}
	free(name);
	return (1);
}
