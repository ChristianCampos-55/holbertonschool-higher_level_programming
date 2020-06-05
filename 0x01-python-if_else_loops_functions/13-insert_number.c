#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a node in a sorted linked list
 * @head: pointer to adress of head of list
 * Return: adress of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (!(*head) || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next)
	{
		if ((current->next)->n >= number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	new->next = NULL;
	return (new);
}
