-- Advent of Code 2017, Day 15
-- (c) blu3r4y


import           Data.Bits

faca = 16807 :: Word
facb = 48271 :: Word
modul = 2147483647 :: Word
mask16 = 65535 :: Word

part1 :: Word -> Word -> Int -> Int
part1 a b runs = solve a b runs 1 1

part2 :: Word -> Word -> Int -> Int
part2 a b runs = solve a b runs 4 8

solve :: Word -> Word -> Int -> Word -> Word -> Int
solve starta startb runs moda modb = numEqual a b where
    a = take runs $ generator moda starta faca
    b = take runs $ generator modb startb facb

numEqual :: Eq a => [a] -> [a] -> Int
numEqual a b = length $ filter (==True) $ zipWith (==) a b

generator :: Word -> Word -> Word -> [Word]
generator m start fac = map (.&. mask16) . filter (\a -> (a `rem` m) == 0) $ values start fac

values :: Word -> Word -> [Word]
values start fac = tail $ iterate (\val -> (val * fac) `rem` modul) start

main :: IO ()
main = do
    print $ part1 65 8921 5
    print $ part1 65 8921 (40 * 10 ^ 6)
    print $ part1 116 299 (40 * 10 ^ 6)
    putStrLn ""
    print $ part2 65 8921 1056
    print $ part2 65 8921 (5 * 10 ^ 6)
    print $ part2 116 299 (5 * 10 ^ 6)
