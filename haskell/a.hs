main :: IO ()
main = do
    name <- getLine
    putStrLn ("Hi, " ++ name ++ ".")
    print(map abs [-1,-2])
    
p :: Double -> Double -> Double
p x y = (*) (exp (-y)) ((**) y x) / (product [1..x])

-- p' = \ xs -> y -> (+) p (x:xs) 15 y 

-- p'
--     = \ n ->
--         case n of
--              -> p n 15  
--             otherwise = p (n) 15 + p (n-1) 15

p' []     acc = acc
p' (x:xs) acc = p x 15 + p' xs acc

p'' = p 0 15 + p 1 15 + p 2 15 + p 3 15 + p 4 15 + p 5 15 + p 6 15 + p 7 15 + p 8 15 + p 9 15

b = \ x -> \ y -> x

halve xs = splitAt (length xs `div` 2) xs

halve' xs = splitAt (div (length xs) 2) xs

halve'' xs = (take n xs, drop n xs)
    where n = length xs `div` 2

safetail
    = \ xs -> 
        case xs of
            [] -> []
            (_ : xs) -> xs

safetail' xs
    | null xs = []
    | otherwise = tail xs

safetail'' xs = if null xs then [] else tail xs

isOdd
    = \ x ->
        if ((mod x 2) == 0) then False else True

-- isEven
--     = \ x ->
--         not isOdd x

-- isEven :: Int -> Bool
-- isEven x = not isOdd x