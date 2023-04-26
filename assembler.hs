import System.Environment
import Control.Exception

main = do
    args <- getArgs
    if (length args == 1)
        then putStrLn "Correct number of args found!"
        else error "OOPS!"
    content <- readFile (args!!0)
    putStr content

