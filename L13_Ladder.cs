﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {

        Console.WriteLine(solution(new[] { 4, 4, 5, 5, 1 }, new[] { 3, 2, 4, 3, 1 }));
    }

    public static int[] solution(int[] A, int[] B)
    {
        var combinations = new int[A.Length];
        var fibonacci = GetFibonacciSequence(A.Max(), B.Max());

        for (var i = 0; i < A.Length; i++)
        {
            var a = fibonacci[A[i] + 1];
            var b = (1 << B[i]) - 1;

            combinations[i] = a & b;
        }

        return combinations;
    }

    private static int[] GetFibonacciSequence(int n, int modPower)
    {
        var mod = (1 << modPower) - 1;
        var fibonacci = new int[n + 2];
        fibonacci[1] = 1;

        for (var i = 2; i < fibonacci.Length; i++)
        {
            fibonacci[i] = (fibonacci[i - 2] + fibonacci[i - 1]) & mod;
        }

        return fibonacci;
    }

}




