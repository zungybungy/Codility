using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 3, 2, -6, 4, 0 }));
    }

    public static int solution(int[] A)
    {
        var maxSumEnding = 0;
        var maxSum = -int.MaxValue;

        foreach (var num in A)
        {
            maxSumEnding += num;
            maxSum = Math.Max(maxSumEnding, maxSum);

            if (maxSumEnding < 0)
            {
                maxSumEnding = 0;
            }
        }

        return maxSum;
    }

    public static int solution2(int[] A)
    {
        var maxSumEndingHere = 0;
        var maxSlice = A[0];

        foreach (var num in A)
        {
            maxSumEndingHere = Math.Max(maxSumEndingHere + num, num);
            maxSlice = Math.Max(maxSlice, maxSumEndingHere);
        }

        return maxSlice;
    }
}




