# package MathProblems;
# import java.util.Scanner;

# public class ArithmeticProblems {

# class Main {
#     public static void main(String[] args) {
#         // System.out.println("Hello, World!");
#         Scanner obj = new Scanner(System.in);
#         int num1 = obj.nextInt();
#         int num2 = obj.nextInt();

#         System.out.println("Sum: " + (num1 + num2));
#         System.out.println("Difference: " + (num1 - num2));
#         System.out.println("Product: " + (num1 * num2));
#         System.out.println("Division: " + (num1 / num2));
#         System.out.println("Remainder: " + (num1 % num2));

#        obj.close(); 
#     }
# }
# }


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number:"))

print("Sum: ",num1 + num2)
print("Subtraction: ",num1 - num2)
print("Multiplication : ",num1 * num2)
print("Division :", num1 / num2)
print("Modulus :",num1 % num2)
