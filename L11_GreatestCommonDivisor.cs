using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {

        Console.WriteLine(GcdSubstract(10,30));
    }

    public static int GcdSubstract(int a, int b)
    {
        if (a == b)
        {
            return a;
        }

        return a > b ?
            GcdSubstract(a - b, b) :
            GcdSubstract(a, b - a);
    }

    public static int GcdModulo(int a, int b)
    {
        if (a % b == 0)
        {
            return b;
        }

        return GcdModulo(b, a % b);
    }

    public static int GcdBinary(int a, int b, int res)
    {
        if (a == b)
        {
            return a * res;
        }

        if (a % 2 == 0 && b % 2 == 0)
        {
            return GcdBinary(a / 2, b / 2, 2 * res);
        }

        if (a % 2 == 0)
        {
            return GcdBinary(a / 2, b, res);
        }

        if (b % 2 == 0)
        {
            return GcdBinary(a, b / 2, res);
        }

        return a > b ?
            GcdBinary(a - b, b, res) :
            GcdBinary(a, b - a, res);
    }

}




