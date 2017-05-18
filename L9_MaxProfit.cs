using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(new[] { 23171, 21011, 21366, 21013, 21367 }));
    }

    public static int solution(int[] A)
    {
        if (A.Length < 1)
        {
            return 0;
        }

        var maxProfit = 0;
        var minPrice = A[0];

        foreach (var price in A)
        {
            maxProfit = Math.Max(maxProfit, price - minPrice);
            minPrice = Math.Min(minPrice, price);
        }

        return maxProfit;
    }
}




