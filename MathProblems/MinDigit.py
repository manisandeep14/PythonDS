# import java.util.Scanner;

# class Main {
#     public static void main(String[] args) {
#         // System.out.println("Hello, World!");
#         Scanner obj = new Scanner(System.in);
#         int num = obj.nextInt();
        
#         long val = num;
#         int temp = num;
#         long res = 0;
        
#         while (num != 0) {
#             res = num % 10;
#             if (res < val) {
#                 val = res;
#             }
#             num /= 10;
#         }
        
#         System.out.println(val);
#     }
# }


num = int(input("Enter a number: "))
val = num
temp = num
res = 0

while num != 0:
  res = num % 10
  if res < val:
    val = res
  num //= 10  #floor division

print("The value is : ", val)
    

