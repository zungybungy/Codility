using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 0, 1, 1, 1, 0, 0, 1 }));
    }

    public static int solution(int[] A)
    {
        if (A.Length == 0)
        {
            return 0;
        }

        Array.Sort(A);
        //this probally not optimum at all - try to do with set
        int distinctCount = 1;
        for (int i = 1; i < A.Length; i++)
        {
            if (A[i] != A[i - 1])
            {
                distinctCount++;
            }
        }

        return distinctCount;
    }
}

// tests


