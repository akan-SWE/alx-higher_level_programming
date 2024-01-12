#include <stdio.h>
#include <time.h>
#include <Python.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p)
{
	PyListObject *list_obj;
	Py_ssize_t i;

    if (p->ob_type != &PyList_Type) {
        printf(" [ERROR]: Invalid List Object\n");
        return;
    }

	list_obj = (PyListObject *)p;
	Py_ssize_t size = list_obj->ob_base.ob_size;
	Py_ssize_t allocated = list_obj->allocated;

	/* List information */
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = list_obj->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;
	char *bytes_as_str;

	printf("[.] bytes object info\n");
	size = bytes->ob_base.ob_size;

	printf(" size : %ld\n", size);

	bytes_as_str = bytes->ob_sval;
	printf(" trying string: %s\n", bytes_as_str);
	printf(" first %ld bytes:", (size + 1) < 10 ? size + 1: 10);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02x", bytes_as_str[i] & 0xFF);
	putchar('\n');
}

void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;

	printf("[.] float bytes info\n");

	if (PyFloat_Check(p))
		printf(" value: %g\n", float_obj->ob_fval);
	else
		printf(" [ERROR] Invalid Float Object\n");
}
