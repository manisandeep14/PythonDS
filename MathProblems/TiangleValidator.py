# package MathProblems;
# import java.util.Scanner;

# public class TiangleValidator {

# class Main {
#     public static void main(String[] args) {
#         // System.out.println("Hello, World!");
#         Scanner obj = new Scanner(System.in);
        
#         int num1 = obj.nextInt();
#         int num2 = obj.nextInt();
#         int num3 = obj.nextInt();

#         if (num1 + num2 > num3) {
#             if (num1 + num3 > num2) {
#                 if (num2 + num3 > num1) {
#                     System.out.println("Yes");
#                 }
#             }
#         } else {
#             System.out.println("No");
#         }
#        obj.close(); 
#     }
# }
# }

num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))
num3 = int(input("Enter Third Number:"))

if num1 + num2  > num3 :
  if num1 + num3 > num2 :
    if num2 + num3 > num1 :
      print("Yes, itz a valid Triangle")
else:
  print("No, itz not a valid Triangle")    
