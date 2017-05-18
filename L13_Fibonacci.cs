using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {

        Console.WriteLine(Fibonacci(13));
    }

    public static int[] Fibonacci(int n)
    {
        var nums = new int[n];

        nums[0] = 1;
        nums[1] = 1;

        for (int i = 2; i < n; i++)
        {
            nums[i] = nums[i - 1] + nums[i - 2];
        }

        return nums;
    }

}




