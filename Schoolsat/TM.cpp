#include <iostream>
#include <vector>

int main() {
    std::vector<double> variable1 = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::vector<double> variable2 = {2.0, 4.0, 6.0, 8.0, 10.0};

    double timeInterval = 1.0;  // seconds

    std::vector<double> rates;
    for (size_t i = 0; i < variable1.size() - 1; ++i) {
        double rate = (variable2[i + 1] - variable2[i]) / (variable1[i + 1] - variable1[i]) / timeInterval;
        rates.push_back(rate);
    }

    // Print the rates
    std::cout << "Rates between variable2 and variable1 per second:" << std::endl;
    for (size_t i = 0; i < rates.size(); ++i) {
        std::cout << "Interval " << i + 1 << ": " << rates[i] << " units/second" << std::endl;
    }

    return 0;
}
