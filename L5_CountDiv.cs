using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Console.WriteLine(solution(6, 100, 2));
    }

    static public int solution(int A, int B,int K)
    {
        int num = 0;
        num = B / K - A / K + ((A % K) == 0 ? 1 : 0);
        return num;
    }
}

// tests


