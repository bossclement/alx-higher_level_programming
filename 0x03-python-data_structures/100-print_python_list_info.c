#include <Python.h>

/**
 * print_python_list_info - prints info of a python list.
 * @p: the python list object.
 */
void print_python_list_info(PyObject *p)
{
	int sz, space, i;
	PyObject *obj;

	sz = Py_SIZE(p);
	space = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", space);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
