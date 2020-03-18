using System;

namespace ifElse
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Console.Write("Enter your born in year : ");
            int y = int.Parse(Console.ReadLine());
            if (y >= 1965)
            {
                if (y >= 2011)
            {
            System.Console.WriteLine("You're GenAlpha");                
            }else if (y >= 1996)
            {
            System.Console.WriteLine("You're GenZ");                
            }else if (y >= 1980)
            {
            System.Console.WriteLine("You're GenY");                
            }else
            {
            System.Console.WriteLine("You're GenX");                
            }
            }
        }   
    }
}
