using System;

namespace gamma
{
    class Program
    {
        static void Main(string[] args)
        {
            // System.Console.Write("Please Input number : ");
            // int a = Convert.ToInt32(Console.ReadLine());
            // System.Console.WriteLine(a);
            System.Console.Write("Width :");
            double w = Convert.ToDouble(Console.ReadLine());
            System.Console.Write("Height :");
            double h = Convert.ToDouble(Console.ReadLine());
            System.Console.WriteLine("Recangle area = " + Recangle(w,h));
            System.Console.WriteLine("Square area = " + Square(5));
        }
        static double Recangle(double w, double h) {
            return w*h;
        }
        static double Square(double side) {
            return Recangle(side, side);
        }
    }
}
