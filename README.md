
# Karatsuba Multiplication

This repository contains an implementation of the **Karatsuba multiplication algorithm**, an efficient divide-and-conquer approach for multiplying large numbers. Unlike traditional multiplication methods, Karatsuba reduces the number of required multiplications, significantly improving performance for large inputs.  

## Features  
- Supports multiplication of **large numbers** in **any numerical base**.  
- Implements the **divide-and-conquer Karatsuba algorithm** for enhanced efficiency.  

## How It Works  
The Karatsuba algorithm improves multiplication efficiency using the formula:  

<img width="385" alt="Screen Shot 2025-03-03 at 10 48 58 pm" src="https://github.com/user-attachments/assets/9777d84c-b76f-4585-82ee-614304345164" />


where:  
- **X and Y** are the two numbers being multiplied,  
- **A, B, C, D** are split parts of the numbers,  
- **m** is the half-length of the numbers.  


