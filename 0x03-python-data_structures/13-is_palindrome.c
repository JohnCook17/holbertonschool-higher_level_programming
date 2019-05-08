#include "lists.h"

void rev(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *cur = *head;
	listint_t *next;

	while(cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*head = prev;
}
int comp(listint_t *head, listint_t *half)
{
	listint_t *temp1 = head;
	listint_t *temp2 = half;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *half, *prev = *head;
	listint_t *mid = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = slow;
			slow = slow->next;
		}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	half = slow;
	prev->next = NULL;
	rev(&half);
	res = comp(*head, half);
	rev(&half);
	if (mid != NULL)
	{
		prev = mid;
		mid->next = half;
	}
	else
		prev->next = half;
	}
	return (res);
}
