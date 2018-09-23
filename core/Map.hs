module Map
  ( module Map
    ) where

import System.Random

type Coordinate = Int
type Name = String
type Id = Int
type Map = ([Object], [Entity])

data Entity = Entity
            { getName :: Name
            , getId :: Id
            , getEX :: Coordinate
            , getEY :: Coordinate
            , getProperties :: [Property]
            } deriving (Eq)
instance Show Entity where
  --   Umnikos - X=293 Y=-392 (8)
  show (Entity name id x y _) = name ++ " - X=" ++ show x ++ " Y=" ++ show y ++ " (" ++ show id ++ ")"

data Property = Health Int
              | Hunger Int
              | Thirst Int
              deriving (Eq, Show)

data Object = Object
            { getOX :: Coordinate
            , getOY :: Coordinate
            , getClass :: Class
            } deriving (Eq, Show)

data Class = Wood
           | Stone
           deriving (Eq, Show)

walkRandomly :: Entity -> IO Entity
walkRandomly (Entity nm id x y ps) = do
  gen <- newStdGen
  let (i,_) = randomR (0, 7) gen :: (Int, StdGen)
      (dx,dy) = [(1,1),(1,0),(1,-1)
                ,(0,1),      (0,-1)
                ,(-1,1),(-1,0),(-1,-1)] !! i
  return $ Entity nm id (x+dx) (y+dy) ps

