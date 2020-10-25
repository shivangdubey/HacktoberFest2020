#include <stdio.h>

typedef struct
{   int row;
    int col;
} Order;

typedef struct
{   int row_i;
    int col_i;
    int val;
} Tuple;

void inputMatrix(int arr[][5], Order *order)
{   int *curr_elem_addr = 0;

    printf("Start entering: \n");
    for (int i = 0; i < order->row; i++)
    {   for (int j = 0; j < order->col; j++)
        {      scanf("%d", &arr[i][j]);       }
    }
}

int convertToTuple(int arr[][5], Order *order, Tuple *tuple)
{   int tuple_index = 0;
    int curr_elem = 0;

    for (int i = 0; i < 10; i++)
        tuple[i].val = 0;

    for (int i = 0; i < order->row; i++)
    {   for (int j = 0; j < order->col; j++)
        {
            if (arr[i][j] != 0)
            {
                tuple[tuple_index].row_i = i;
                tuple[tuple_index].col_i = j;
                tuple[tuple_index++].val = arr[i][j];
            }
        }
    }
    return tuple_index;
}

void printTuple(Tuple *tuple, int tuple_sz)
{   printf("R C Value\n");
    for (int i = 0; i < tuple_sz; i++)
    {   printf("%d %d %d\n",tuple[i].row_i,tuple[i].col_i,tuple[i].val);    }
    printf("\n");
}

int main()
{   int a[5][5], b[5][5];
    Order mat_order;
    Tuple tuple_a[10], tuple_b[10];
    int tuple_size_a, tuple_size_b;

    printf("Enter the no:of rows in the matrix: ");
    scanf("%d", &mat_order.row);
    printf("Enter the no:of cols in the matrix: ");
    scanf("%d", &mat_order.col);

    printf("Enter the first matrix: \n");
    inputMatrix(a, &mat_order);

    printf("Enter the second matrix: \n");
    inputMatrix(b, &mat_order);

    tuple_size_a = convertToTuple(a, &mat_order, tuple_a);
    tuple_size_b = convertToTuple(b, &mat_order, tuple_b);

    printf("Tuple form of the two matrices are: \n");
    printTuple(tuple_a, tuple_size_a);
    printTuple(tuple_b, tuple_size_b);

    return 0;
}
