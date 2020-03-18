using System;

namespace Switch
{
    class Program
    {
        static void Main(string[] args)
        {
            testSwitch();
        }
        static void testSwitch() {
            System.Console.WriteLine("1.Kid");
            System.Console.WriteLine("2.Adult");
            System.Console.WriteLine("3.Elder");
            System.Console.WriteLine("4.Student");
            System.Console.Write("Select Customer type : ");
            int i = System.Console.Read();
            int discount = 0;
            switch (i)
            {
                case '1':
                case 'k':
                    Console.WriteLine("You're a kid.");
                    discount = 50;
                    Console.WriteLine($"Discount = {discount} %");
                    break;
                case '2':
                case 'a':
                    discount = 20;
                    Console.WriteLine("You're a adult.");
                    Console.WriteLine($"Discount = {discount} %");
                    break;
                case '3':
                case 'e':
                    discount = 30;
                    Console.WriteLine($"Discount = {discount} %");
                    Console.WriteLine("You're a elder.");
                    break;
                case '4':
                case 's':
                    discount = 40;
                    Console.WriteLine($"Discount = {discount} %");
                    Console.WriteLine("You're a student.");
                    break;
                default:
                    System.Console.WriteLine("Please select 1 to 4");
                    break;
            }
        }
    }
}
