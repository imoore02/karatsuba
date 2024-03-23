#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to add two integers using the school method
string schoolAddition(string num1, string num2, int base) {
    int carry = 0;
    string result = "";
    
    while (!num1.empty() || !num2.empty() || carry) {
        int digit1 = num1.empty() ? 0 : num1.back() - '0';
        int digit2 = num2.empty() ? 0 : num2.back() - '0';
        
        int sum = digit1 + digit2 + carry;
        carry = sum / base;
        sum %= base;
        
        result = to_string(sum) + result;
        
        if (!num1.empty()) num1.pop_back();
        if (!num2.empty()) num2.pop_back();
    }
    
    return result;
}

// Function to multiply two integers using Karatsuba algorithm
string karatsubaMultiplication(string num1, string num2, int base) {
    if (num1.length() < num2.length()) swap(num1, num2);
    
    int n = num1.length();
    
    if (n == 0) return "0";
    if (n == 1) return to_string((num1[0] - '0') * (num2[0] - '0'));
    
    int half = n / 2;
    
    string a = num1.substr(0, half);
    string b = num1.substr(half);
    string c = num2.substr(0, min<int>(num2.length(), half));
    string d = num2.substr(min<int>(num2.length(), half));
    
    string ac = karatsubaMultiplication(a, c, base);
    string bd = karatsubaMultiplication(b, d, base);
    
    string aPlusB = schoolAddition(a, b, base);
    string cPlusD = schoolAddition(c, d, base);
    string adPlusBc = schoolAddition(karatsubaMultiplication(aPlusB, cPlusD, base), schoolAddition(ac, bd, base), base);
    
    string zeros1(half, '0');
    string zeros2(n, '0');
    
    return schoolAddition(schoolAddition(ac + zeros2, adPlusBc + zeros1, base), bd, base);
}

// Function to perform integer division
string integerDivision(string num1, string num2, int base) {
    string quotient = "0";
    string remainder = num1;
    
    while (remainder.length() >= num2.length()) {
        int shift = remainder.length() - num2.length();
        string temp = num2 + string(shift, '0');
        
        if (remainder < temp) {
            temp.pop_back();
            shift--;
        }
        
        string subtracted = schoolAddition(remainder, temp, base);
        
        if (subtracted == "0") break;
        
        quotient = schoolAddition(quotient, string(shift, '1'), base);
        remainder = subtracted;
    }
    
    return quotient;
}

int main() {
    string num1, num2;
    int base;
    cin >> num1 >> num2 >> base;
    
    // School Method Addition
    string sum = schoolAddition(num1, num2, base);
    
    // Karatsuba Multiplication
    string product = karatsubaMultiplication(num1, num2, base);
    
    // Integer Division
    string division = integerDivision(num1, num2, base);
    
    cout << sum << " " << product << " " << division << endl;
    
    return 0;
}