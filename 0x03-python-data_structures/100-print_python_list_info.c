#include <Python.h>

/**
 * print_python_list_info - Function to print Python list's info
 * @p: Element of type PyObject
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj = NULL;
	Py_ssize_t a = 0, s = 0;

	if (p == NULL || !PyList_Check(p))
		return;
	s = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", s);
	printf("[*] Allocated = %zu\n", ((PyListObject *) p)->allocated);
	for (; a < s; a++)
	{
		obj = PyList_GetItem(p, a);
		printf("Element %zu: %s\n", a, Py_TYPE(obj)->tp_name);
	}
}
