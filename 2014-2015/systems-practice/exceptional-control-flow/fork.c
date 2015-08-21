#include <iostream>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <errno.h>
using namespace std;

static const size_t kNumChildren = 5;
static size_t numDone = 0;
// To execute C++, please define "int main()"
static void reapChild(int sig){
  pid_t pid;
  while(true) {
    pid = waitpid(-1, NULL, WNOHANG);
    if (pid<=0) break;
    numDone++;
  }
}
int main(int argc, char *argv[]) {
  printf("Let children play\n");
  signal(SIGCHLD, reapChild);
  for (size_t kid = 1; kid <= 5; kid++) {
    pid_t pid = fork();
    if (pid == 0) {
      sleep(3);
      printf("Kid #%zu is done playing\n", kid);
      return 0;
    }
  }
}