-- Advent of Code 2017, Day 2
-- (c) blu3r4y


import           Data.List
import           Data.List.Split
import           Data.Tuple

part1 :: [[Int]] -> Int
part1 matrix = sum [maximum row - minimum row | row <- matrix]

part2 :: [[Int]] -> Int
part2 matrix = sum $ map evenlyDivisible matrix where
    allPairs a = concatMap (\ e -> [e, swap e]) (pairs a)                   -- cartesian product without duplicates
    divModPairs a = map (uncurry divMod) $ allPairs a                       -- divmod each pair
    evenlyDivisible a = result where
        Just (result, _) = find (\(_, rest) -> rest == 0) $ divModPairs a   -- return evenly divisible tuple

pairs :: Num a => [a] -> [(a, a)]
pairs a = [(x, y) | (x:xs) <- tails a, y <- xs]

parser :: FilePath -> IO [[Int]]
parser path = map (map read . splitOn "\t") . lines <$> readFile path

main :: IO ()
main = do
    print . part1 $ [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    parser "../assets/day2_part1.txt" >>= print . part1
    putStrLn ""
    print . part2 $ [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
    parser "../assets/day2_part2.txt" >>= print . part2
