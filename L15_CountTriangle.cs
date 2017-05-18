using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {

        Console.WriteLine(solution(new[] { 3, 2, 9, 4, 0 }));
    }

    public static int solution(int[] A)
    {
        var result = 0;

        Array.Sort(A);

        for (int x = 0; x < A.Length; x++)
        {
            var z = 0;
            for (int y = x + 1; y < A.Length; y++)
            {
                while (z < A.Length && A[x] + A[y] > A[z])
                {
                    z++;
                }

                result += z - y - 1;
            }
        }

        return result;
    }

}




