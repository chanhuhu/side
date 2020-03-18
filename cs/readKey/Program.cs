using System;

namespace readKey
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Console.Write("Enter your key is ");
            ConsoleKeyInfo k;
            k = Console.ReadKey();
            System.Console.WriteLine($"Key : {k.Key}, Modifier :{k.Modifiers}");
            System.Console.Write("Type any to exit : ");
            Console.ReadKey();
        }
    }
}
