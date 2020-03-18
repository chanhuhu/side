using System;

namespace beta
{
    class Program
    {
        static void Main(string[] args)
        {
            double w, h;
            Console.Write("Width : " );
            w = Convert.ToDouble(Console.ReadLine());
            Console.Write("Height : ");
            h = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Recangle Area = {0}",w*h);
            Console.ReadKey();
        }
    }
}
