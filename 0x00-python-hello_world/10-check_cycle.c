#include "lists.h"
/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 * Return: 0 on False and 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
