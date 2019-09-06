// gcc bof2.c -o bof2 -no-pie
#include <stdio.h>
#include <unistd.h>

int getflag() {
    printf("\nHINT: you shoudn't jump straight to getflag\n");
    printf("but instead somewhere in the middle\n\n");

    printf("This is due to the stack alignment shifting (the value of rbp now has a '8' in the units place, which system() does not like)");
    system("cat flag");
}

int main() {
    long fib[8] = {0, 1, 1, 2, 3, 5, 8, 13};
    int idx;
    char buf[0x20];

    puts("im the bof fib printer!");
    puts("gimme index of the number you want me to print:");
    scanf("%d", &idx);
    printf("%zu\n", fib[idx]);

    read(0, buf, 0x100);
    printf("hey i printed the fib, %s, what do ya want!", buf);
}
