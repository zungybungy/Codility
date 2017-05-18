using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {

        Console.WriteLine(solution(100));
    }

    public static int solution(int N)
    {
        var minPerimeter = 2 * (N + 1);

        int i = 1;
        while (i * i <= N)
        {
            if (N % i == 0)
            {
                minPerimeter = Math.Min(minPerimeter, 2 * (i + (N / i)));
            }
            i++;
        }

        return minPerimeter;
    }
}




