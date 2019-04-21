def factorialn(num):
  if num == 0:
      return 1;
  return num*factorialn(num-1);

def main():

 print("Hello World!")
 num=input("Enter the value of no")
 num = int(num)
 ans = factorialn(num);
 print("value of ans {}" .format(ans))

main();

