qsort lst
      | lst == [] = []
      | otherwise = (qsort less_eq) ++ [pivot] ++ (qsort greater)
      where
        pivot = head lst
        rest_lst = tail lst
        less_eq = [a | a <- rest_lst, a <= pivot]
        greater = [a | a <- rest_lst, a > pivot]


merge :: [Int] -> [Int] -> [Int]
merge [] lis2 = lis2
merge lis1 [] = lis1
merge (lis1:rest1) (lis2:rest2) =
  if lis1 < lis2
    then lis1 : merge rest1 (lis2:rest2)
    else lis2 : merge (lis1: rest1) rest2


splitList :: [Int] -> ([Int], [Int])
splitList xs = (take half xs, drop half xs)
  where
    half = length xs `div` 2


mergesort :: [Int] -> [Int]
mergesort [] = []
mergesort [x] = [x]
mergesort l =
  let (x,y) = splitList l
  in merge (mergesort x) (mergesort y)

