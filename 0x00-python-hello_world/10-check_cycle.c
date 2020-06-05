#include"lists.h"

/**
 * check_cycle - function that finds if a linked list is looped
 * @list: pointer to head of list
 * Return: 0 if looped, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *check_one = list, *check_two = list;

	while (check_one && check_two && check_two->next && list)
	{
		check_one = check_one->next;
		check_two = check_two->next->next;

		if (check_one == check_two)
			return (1);
	}

	return (0);
}
