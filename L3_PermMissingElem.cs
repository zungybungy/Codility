using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 2, 3, 1, 5 }));
    }

    public static int solution(int[] A)
    {
        // calculate prefix sum
        long arraySum = 0;
        foreach (int i in A) // A.Sum() breaks as it uses Int32
        {
            arraySum += i;
        }

        // calculate theorical sum
        long n = A.Length + 1;
        long theoricalSum = (n * (n + 1)) / 2; // notice long as return type to avoid overflow

        // return difference
        return (int)(theoricalSum - arraySum);
    }
}

// tests


