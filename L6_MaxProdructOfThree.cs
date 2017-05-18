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

        var topMaximum = A[A.Length - 1] * A[A.Length - 2] * A[A.Length - 3];
        var bottomMaxium = A[0] * A[1] * A[A.Length - 1];

        return Math.Max(topMaximum, bottomMaxium);
    }
}

// tests


