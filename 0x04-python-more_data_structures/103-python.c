#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


/**
 * print_python_list - print list info
 * @p: pointer
 * Return: void
 **/
void print_python_list(PyObject *p)
{
	int range, putt, idx;
	const char *kind;
	PyListObject *lista = (PyListObject *)p;
	PyVarObject *vare = (PyVarObject *)p;

	range =  vare->ob_size;
	putt = lista->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", range);
	printf("[*] Allocated = %d\n", putt);

	for (idx = 0; idx < range; idx++)
	{
		kind = lista->ob_item[idx]->ob_type->tp_name;
		printf("Element %d: %s\n", idx, kind);
		if (strcmp(kind, "bytes") == 0)
			print_python_bytes(lista->ob_item[idx]);
	}
}

/**
 * print_python_bytes - print basic info about python bytes
 * @p: pointer
 * Return: void
 **/
void print_python_bytes(PyObject *p)
{
	unsigned char idx, range;
	PyBytesObject *byts = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byts->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		range = 10;
	else
		range = ((PyVarObject *)p)->ob_size + 1;

	printf(" first %d bytes: ", range);
	for (idx = 0; idx < range; idx++)
	{
		printf("%02hhx", byts->ob_sval[idx]);
		if (idx == (range - 1))
			printf("\n");
		else
			printf(" ");
	}
}
