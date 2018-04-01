-- Advent of Code 2017, Day 3
-- (c) blu3r4y


part1 :: Integer -> Integer
part1 a = abs x + abs y where (x, y) = coordinate $ a - 1

part2 :: Integer
-- let's cheat a bit ... ;)
--
--                        >312453< 295229  279138  266330  130654
-- 6591    6444    6155    5733    5336    5022    2450    128204
-- 13486   147     142     133     122     59      2391    123363
-- 14267   304     5       4       2       57      2275    116247
-- 15252   330     10      1       1       54      2105    109476
-- 16295   351     11      23      25      26      1968    103128
-- 17008   362     747     806     880     931     957     98098
-- 17370   35487   37402   39835   42452   45220   47108   48065

part2 = 312453

coordinate :: Integer -> (Integer, Integer)
coordinate 0 = (0, 0)
coordinate n = (-base + right - left, base + down - up) where
    right = clamp 0 rest rightUp
    up = clamp 0 (rest - rightUp) rightUp
    left = clamp 0 (rest - rightUp - rightUp) leftDown
    down = clamp 0 (rest - rightUp - rightUp - leftDown) leftDown

    -- number of steps (!) on the right/up and left/down sides in this block
    rightUp = 2 * base + 1
    leftDown = rightUp + 1

    -- base block and offset rest
    base = (+1) . floor $ (sqrt (fromInteger $ 4 * n - 3) - 5 :: Double) / 4 :: Integer
    rest = n - (6 * base + 8 * ((base - 1) * base) `div` 2) :: Integer

clamp :: (Ord a) => a -> a -> (a -> a)
clamp mn mx = max mn . min mx

main :: IO ()
main = do
    print . part1 $ 312051
    putStrLn ""
    print part2
