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

    const int maxSize = 1000000000;
    public static int solution(int[] A)
    {
        int total = 0;
        int preSum = 0;

        foreach (int car in A)
        {
            if (car == 0)
            {
                preSum++;
            }
            else
            {
                total += preSum;
            }

            if (total > maxSize)
            {
                return -1;
            }
        }

        return total;
    }
}

// tests


