using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 0, 1, 1, 1, 7, 8, 1 }));
    }

    public static int solution(int[] A)
    {
        Array.Sort(A);

        for (int i = 2; i < A.Length; i++)
        {
            long sum = (long)A[i - 1] + (long)A[i - 2];
            if (sum > A[i])
            {
                return 1;
            }
        }

        return 0;
    }
}

// tests


