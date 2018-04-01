// Advent of Code 2017, Day 23
// (c) blu3r4y

package main

import (
	"fmt"
)

func main() {
	fmt.Println(part1())
	fmt.Println(part2())
}

func part1() int {
	mul := 0
	_, b, c, _, _, f, _, h := 0, 93, 93+17, 0, 0, 0, 0, 0

	for b != c {
		mul += (b - 2) * (b - 2)
		for d := 2; d <= b; d++ {
			for e := 2; e <= b; e++ {
				if (d * e) == b {
					f = 0
				}
			}
		}
		if f == 0 {
			h++
		}
		b += 17
	}

	return mul
}

func part2() int {
	_, b, c, _, _, f, _, h := 1, 109300, 126300+17, 0, 0, 0, 0, 0

	for b != c {
		f = 1
		factorList := factors(b, 2)
		for _, d := range factorList {
			for _, e := range factorList {
				if (d * e) == b {
					f = 0
				}
			}
		}
		if f == 0 {
			h++
		}
		b += 17
	}

	return h
}

func factors(n int, start int) []int {
	var result []int
	for i := start; i <= n/2; i++ {
		if n%i == 0 {
			result = append(result, i)
		}
	}
	return result
}
