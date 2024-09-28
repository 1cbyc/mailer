#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    while (1) {
        system("git add .");

        system("git commit -m 'doing the v2 revamp of the mailer anyone can actually use'");

        system("git push");

        sleep(8);
    }

    return 0;
}
