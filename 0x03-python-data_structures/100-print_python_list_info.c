#include <stdio.h>
#include "Python.h"


/**
 * print_python_list_info - print basic information of a python list
 * @l: a list object
 * Description: Information to be printed
 * [*] Size of the Python List = %ld
 * [*] Allocated = %ld
 * Element %d: tp_name	# where %d is the index of the element not vaue
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *l)
{
	PyListObject *mylist;
	int i;

	mylist = (PyListObject *)l;

	printf("[*] Size of the Python List = %ld\n", mylist->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", mylist->allocated);

	/* All elements of the list */
	for (i = 0; i < mylist->ob_base.ob_size; i++)
	{
		printf("Element %d:", i);
		printf(" %s\n", (char *)mylist->ob_item[i]->ob_type->tp_name);
	}
}
