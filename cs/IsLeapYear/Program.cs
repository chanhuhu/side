using System;

namespace IsLeapYear
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Is Leap Year = "+IsLeap(2020));
            PrintList();
        }
        static bool IsLeap(int y) {
            return y % 4 == 0;
        }
        static void PrintList() {
            for (int i = 1; i <= 50; i++) {
                if (i % 5 == 1 && i != 1)
                {
                    System.Console.WriteLine();
                }
                System.Console.Write($"{i,5}");
            }
        }
    }
}
