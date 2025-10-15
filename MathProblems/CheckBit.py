# import java.util.Scanner;

# class Main {
#     public static void main(String[] args) {
#         // System.out.println("Hello, World!");
#         Scanner obj = new Scanner(System.in);
        
#         int lights = obj.nextInt();
#         int pos = obj.nextInt();
        
#         if (((lights >> pos) % 2 == 1)) {
#             System.out.println("true");
#         } else {
#             System.out.println("false");
#         }
#     }
# }

# Bitwise Operators

# & -> and
# | -> or
# ^ -> xor
# << -> left shift
# >> -> right shift

x = 6
y = 12
z = 0

print("AND ->", x & y)
print("OR->", x | y)
print("XOR->", x ^ y)
print("Left Shift->",x << 1 )
print("Right Shift->",x >> 1)


lights = int(input("Enter No.of Lights: "))
pos = int(input("Enter no.of pos: "))

if (lights >> pos) % 2 == 1:
  print("true")
else:
  print("false")

