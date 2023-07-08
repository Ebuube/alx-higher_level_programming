#include <stdio.h>
#include "Python.h"
#include <string.h>

/* FUNCTION PROTOTYPES */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/*
 * HELP FOR COMPILATION
 * gcc -fPIC -shared libname.so ./this-file-name -I/usr/include/python3.8
 *
 * Where: libname.so specifies 'name' the name of the dynamic library
 * this-file-name: The name of this particular file
 */

/**
 * print_python_list - print basic information about Python lists
 * and Python bytes objects
 * @p: a list object
 *
 * Description: Information to be printed
 * [*] Python list info
 * [*] Size of the Python List = %ld
 * [*] Allocated = %ld
 * Element %d: tmp_name # where %d is the index of the element not value
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *mylist = NULL;
	ssize_t i = 0;

	mylist = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", mylist->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", mylist->allocated);

	/* All elements of the list */
	for (i = 0; i < mylist->ob_base.ob_size; i++)
	{
		printf("Element %ld:", i);
		printf(" %s\n", (char *)mylist->ob_item[i]->ob_type->tp_name);

		if (strcmp(mylist->ob_item[i]->ob_type->tp_name, "bytes") == 0)
		{
			print_python_bytes(mylist->ob_item[i]);
		}
	}
}


/**
 * print_python_bytes - print basic information about Python bytes
 * @p: a PyBytesObject
 *
 * Description: Information to be printed
 * [.] bytes object info
 *	size: %ld
 *	trying string: %s
 *	first n bytes: 0x0b 0x0b 0x0b 0x0b # Where n is string len, max n is 10
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	const char *SPACE = "  ";
	ssize_t i = 0;
	ssize_t size = 0;
	const ssize_t MAX = 10;	/* maximum bytes to print */

	printf("[.] bytes object info\n");

	if ((strcmp(p->ob_type->tp_name, "bytes") != 0))
	{/* Not a PyBytesObject */
		printf("%s[ERROR] Invalid Bytes Object\n", SPACE);
		return;
	}

	bytes = (PyBytesObject *)p;

	size = bytes->ob_base.ob_size;
	printf("%ssize: %ld\n", SPACE, size);
	printf("%strying string: %s\n", SPACE, bytes->ob_sval);

	printf("%sfirst %ld bytes:", SPACE, ((size > MAX) ? MAX : size + 1));
	for (i = 0; i < MAX && i < size + 1; i++)
	{
		printf(" %02x", bytes->ob_sval[i]);
	}
	printf("\n");
}
