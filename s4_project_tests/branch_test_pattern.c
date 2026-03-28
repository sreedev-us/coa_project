#include <stdio.h>

int main() {
    long long sum = 0;
    int iterations = 100000; // 100k loops

    for (int i = 0; i < iterations; i++) {
        // A repeating, predictable pattern: True 3 times, False 1 time
        if (i % 4 != 0) { 
            sum += i;
        } else {
            sum -= i;
        }
    }

    printf("Final sum: %lld\n", sum);
    return 0;
}
