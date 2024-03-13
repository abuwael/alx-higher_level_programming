#include "lists.h"

/**
 * check_cycle - Checks if a singl linke lists gain a cycl.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp, *head;

	if (list == NULL || list->next == NULL)
		return (0);

	temp = list->next;
	head = list->next->next;

	while (temp && head && head->next)
	{
		if (temp == head)
			return (1);

		temp = temp->next;
		head = head->next->next;
	}

	return (0);
}
