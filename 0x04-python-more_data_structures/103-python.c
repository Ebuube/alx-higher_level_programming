#ifndef _MY_PY_INFO
#define _MY_PY_INFO


#include <stdio.h>
#include <string.h>

#include "Python.h"


/**
 * print_python_bytes - A function that prints some information
 * about a PyBytesObject
 * @p: a PyObject
 *
 * Description: Print format ->
 *
 * *********************** Separtor *****************************************
 * [.] bytes object info
 *   size: 5
 *   trying string: <the object displayed as string>
 *   first <x> bytes: <the first x bytes in hex format, separated by space>
 * *********************** Separtor *****************************************
 *
 * Where x is the number of bytes in the string and the max val of x is 10
 *
 * Note Note Note Note Note
 * If the object p is not a PyBytesObject, print this error message
 * Print format ->
 *
 * *********************** Separtor *****************************************
 * [.] bytes object info
 *   [ERROR] Invalid Bytes Object
 * *********************** Separtor *****************************************
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *string = 0;
	const Py_ssize_t _MAX_ = 10;
	Py_ssize_t len = 0;
	Py_ssize_t count = 0;

	printf("[.] bytes object info\n");	/* for all objects */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = ((PyBytesObject *)p)->ob_base.ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size = %ld\n", len);
	printf("  trying string: %s\n", string);

	len = (len < _MAX_) ? len + 1 : _MAX_;
	printf("  first %ld bytes:", len);
	for (count = 0; count < len; count++)
		printf(" %02x", string[count]);
}


/**
 * print_python_list - prints some information about a python list object
 * @p: a python list object
 *
 * Description: Print format->
 *
 * *********************** Separtor *****************************************
 * [*] Size of the Python List = <number of current elements>
 * [*] Allocated = <number of allocated>
 * Element 0: <type name>
 * Element 1: <type name>
 * Element (n - 1): <type name>
 * *********************** Separtor *****************************************
 *
 * Note Note that for the element types, it will be printed for only a list
 * with length n, such that n > 0
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = 0;
	char *type_name = 0;
	ssize_t count = 0;

	if (!p)
	{
		return;
	}
	list = (PyListObject *)p;	/* Important for allocated and size */
	printf("[*] Python List info\n");	/* for all PyListObject's */
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (count = 0; count < list->ob_base.ob_size; count++)
	{
		type_name = (char *)list->ob_item[count]->ob_type->tp_name;
		printf("Element %ld: %s\n", count, type_name);
		if (PyBytes_Check(list->ob_item[count]))
			print_python_bytes(list->ob_item[count]);
	}
}

#endif	/* _MY_PY_INFO */
