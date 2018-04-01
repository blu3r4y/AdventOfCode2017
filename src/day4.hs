-- Advent of Code 2017, Day 4
-- (c) blu3r4y


import           Data.List
import           Data.List.Split

part1 :: [[String]] -> Int
part1 text = length $ filter (\line -> length line == length (nub line)) text

part2 :: [[String]] -> Int
part2 text = part1 $ map (map sort) text

parser :: FilePath -> IO [[String]]
parser path = map (splitOn " ") . lines <$> readFile path

main :: IO ()
main = do
    parser "../assets/day4.txt" >>= print . part1
    putStrLn ""
    parser "../assets/day4.txt" >>= print . part2
