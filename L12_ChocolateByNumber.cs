using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {

        Console.WriteLine(solution(13, 2));
    }

    public static int solution(int N, int M)
    {
        var chocolates = new int[N];
        var countEaten = 0;

        var i = 0;
        while (chocolates[i] == 0)
        {
            chocolates[i] = 1;
            countEaten++;
            i = (i + M) % N;
        }

        return countEaten;
    }

    public static int solution2(int N, int M)
    {
        // Calculate the GCD
        var a = N;
        var b = M;
        int gcd;

        while (a % b != 0)
        {
            gcd = b;
            b = a % b;
            a = gcd;
        }
        gcd = b;

        return N / gcd;
    }

}




