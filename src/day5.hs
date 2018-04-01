-- Advent of Code 2017, Day 5
-- (c) blu3r4y


import           Control.Monad.Extra
import           Control.Monad.ST
import           Data.Array.Base

type OffsetFunc = (Int -> Int)

part1 :: [Int] -> Int
part1 = jumpCount (+ 1)

part2 :: [Int] -> Int
part2 = jumpCount (\a -> if a >= 3 then a - 1 else a + 1)

jumpCount :: OffsetFunc -> [Int] -> Int
jumpCount f list = runST (do
    let upper = length list - 1
    arr <- newListArray (0, upper) list :: ST s (STUArray s Int Int)        -- mutable array for jumps
    (+ 1) . length <$> iterateMaybeM (jump f upper arr) 0)                  -- repeated jump function application

jump :: OffsetFunc -> Int -> STUArray s Int Int -> Int -> ST s (Maybe Int)
jump f size arr pos = do
    offset <- unsafeRead arr pos
    unsafeWrite arr pos $ f offset
    let
        newPos = pos + offset
        result = if newPos >= 0 && newPos <= size then Just newPos else Nothing
    return result

parser :: FilePath -> IO [Int]
parser path = map read . lines <$> readFile path

main :: IO ()
main = do
        print $ part1 [0, 3, 0, 1, -3]
        parser "../assets/day5.txt" >>= print . part1
        putStrLn ""
        print $ part2 [0, 3, 0, 1, -3]
        parser "../assets/day5.txt" >>= print . part2
