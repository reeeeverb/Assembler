import System.Environment
import System.IO
import Control.Exception

main = do
    args <- getArgs
    if (length args == 1)
        then putStrLn "Correct number of args found!"
        else error "OOPS!"
    handle <- openFile (args!!0) ReadMode
    content <- hGetContents handle
    let singlelines = lines content
    print singlelines
    hClose handle

