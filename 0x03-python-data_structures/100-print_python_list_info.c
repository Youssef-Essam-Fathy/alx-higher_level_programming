#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: the python object
 * Return: void
 **/
void print_python_list_info(PyObject *p)
{
	int range, insert, i;
	PyObject *p2;

	range = Py_SIZE(p);
	insert = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", range);
	printf("[*] Allocated = %d\n", insert);

	for (i = 0; i < range; i++)
	{
		printf("Element %d: ", i);

		p2 = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(p2)->tp_name);
	}
}
