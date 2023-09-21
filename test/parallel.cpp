#include <iostream>
#include <thread>

void hello(int x) {
    std::cout << "Hello from thread " << std::this_thread::get_id() << ", x = " << x << std::endl;
}

int main() {
    int x = 42;
    std::thread t1(hello, 1);
    std::thread t2(hello, 1);
    t1.join();
    t2.join();
    return 0;
}
