#include <stdio.h>
#include <stdlib.h>

struct Stack {
    unsigned int size;
    int top;
    char* arr;
};

struct Stack* initializeStack(int size) {
    struct Stack* s = (struct Stack*)malloc(sizeof(struct Stack));

    // Check if memory was available.
    if (!s) {
        printf("[Error] Memory allocation failed!\n");
        exit(0); // Exit the program with a failure code
    }

    s->top = -1;
    s->size = size;
    s->arr = (int*)malloc(s->size * sizeof(int));

    if (!s->arr) {
        printf("[Error] Memory allocation failed!\n");
        exit(0);
    }

    return s;
}

void push(struct Stack* s, char val) { s->arr[++(s->top)] = val; }

char pop(struct Stack* s) { return s->arr[(s->top)--]; }

int isEmpty(struct Stack* s) { return s->top == -1; }

bool isValid(char* s) {
    struct Stack* sp = initializeStack(10e4);

    for (int i = 0; s[i] != '\0'; i++) {

        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            push(sp, s[i]);

        } else {
            if (isEmpty(sp))
                return false;
            char check = pop(sp);
            if ((s[i] == ')' && check != '(') ||
                (s[i] == ']' && check != '[') ||
                (s[i] == '}' && check != '{')) {
                free(sp->arr);
                free(sp);
                return false;
            }
        }
    }

    if (!isEmpty(sp)) {
        free(sp->arr);
        free(sp);
        return false;
    }

    free(sp->arr);
    free(sp);
    return true;
}
