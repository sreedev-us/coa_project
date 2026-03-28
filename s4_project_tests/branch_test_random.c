#include <stdio.h>
#include <stdlib.h>

int main() {
    long long sum = 0;
    int iterations = 10000; // 10 million loops

    // Seed the random number generator
    srand(42); 

    for (int i = 0; i < iterations; i++) {
        // Generate a random number
        int val = rand() % 100; 

        // Unpredictable branch
        if (val < 50) { 
            sum += val;
        } else {
            sum -= val;
        }
    }

    printf("Final sum: %lld\n", sum);
    return 0;
}
