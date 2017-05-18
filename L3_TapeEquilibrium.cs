using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 3, 1, 2, 4, 3 }));
    }

    public static int solution(int[] A)
    {
        int length = A.Length;
        const int maxLenght = 100000;
        int[] partialSums = new int[maxLenght];

        // calculate partial sums
        for (int i = 0; i < length; i++)
        {
            partialSums[i] = i > 0 ? A[i] + partialSums[i - 1] : A[i];
        }

        int minimalValue = int.MaxValue;

        // get minimal value
        for (int i = 0; i < length - 1; i++)
        {
            int difference = Math.Abs(partialSums[i] - (partialSums[length - 1] - partialSums[i]));

            minimalValue = difference < minimalValue ? difference : minimalValue;
        }

        return minimalValue;
    }
}

// tests


