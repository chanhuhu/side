using System;

namespace nestedLoop
{
    class Program
    {
        static void Main(string[] args)
        {
            //box(2,1);
            //triangle(5);
        }
        static void box(int h,int w) {
            for (int i = 1; i < h; i++)
            {
                for (int j = 1; j < w; j++)
                {
                    System.Console.Write('*');
                }
                System.Console.WriteLine("");
            }
        }
        static void triangle(int h) {
            for (int i = 1; i < h; i++)
            {
                for (int j = 1; j < i; j++)
                {
                    System.Console.Write('*');
                }
                System.Console.WriteLine();
            }
        }
        static void multiple(int a) {
            for (int i = 1; i <= 12; i++)
            {
                System.Console.WriteLine($"{i,2} * {a} = {i*a,2}");
            }
        }
        }
    }
}
