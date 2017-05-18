using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 3, 2, 4, 1 }));
    }

    public static int solution(int[] A)
    {
        const int maxLength = 100000;
        const int isPermutation = 1;
        const int isNotPermutation = 0;
        int length = A.Length;

        int[] countingArray = new int[maxLength]; // initialized to 0 by default

        for (int i = 0; i < length; i++)
        {
            if (A[i] > maxLength)
            {
                return isNotPermutation;
            }
            else
            {
                countingArray[A[i] - 1] = 1;
            }
        }

        for (int i = 0; i < length; i++)
        {
            if (countingArray[i] == 0)
            {
                return isNotPermutation;
            }
        }

        return isPermutation;
    }
}

// tests


