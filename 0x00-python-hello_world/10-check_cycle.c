#include "lists.h"
/**
 * check_cycle - checks if the list has a cycle in it
 * @list: the linked list to check
 *
 * Return: 0 if no cycle 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = fast = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
