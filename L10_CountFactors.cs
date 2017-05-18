using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {

        Console.WriteLine(solution(100));
    }

    public static int solution(int N)
    {
        var result = 0;

        int i = 1;
        while (i * i < N)
        {
            if (N % i == 0)
            {
                result += 2;
            }
            i++;
        }
        if (i * i == N)
        {
            result++;
        }

        return result;
    }

}




