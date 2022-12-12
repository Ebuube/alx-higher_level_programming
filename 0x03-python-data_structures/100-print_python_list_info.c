#ifndef _MY_PY_LIST
#define _MY_PY_LIST

#include <stdio.h>

#include "Python.h"


/**
 * print_python_list_info - prints some information about a python list object
 * @p: a python list object
 *
 * Description: Print format->
 * [*] Size of the Python List = <number of current elements>
 * [*] Allocated = <number of allocated>
 * Element 0: <type name>
 * Element 1: <type name>
 * Element (n - 1): <type name>
 * ************** Separteor ****************************
 * Note that for the element types, it will be printed for only a list
 * with length n, such that n > 0
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = 0;
	char *type_name = 0;
	ssize_t count = 0;

	list = (PyListObject *)p;	/* Important for allocated and size */
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (count = 0; count < list->ob_base.ob_size; count++)
	{
		type_name = (char *)list->ob_item[count]->ob_type->tp_name;
		printf("Element %ld: %s\n", count, type_name);
	}
}

#endif	/* _MY_PY_LIST */
