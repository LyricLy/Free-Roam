module Map 
  ( module Map
  ) where

import System.Random

type Speed = Float
type Coordinate = Float
type Name = String
type Id = Int

-- type Map = ([Entity], Biomes)
data Entity = Entity
            { getName :: Name
            , getId :: Id
            , getX :: Coordinate
            , getY :: Coordinate
            , getProperties :: [Property]
            } deriving (Eq)
instance Show Entity where
  --        Dagger of death - X=2.23606797749979 Y=-3.128423821201 (18398122)
  show (Entity name id x y _) = name ++ " - X=" ++ show x ++ " Y=" ++ show y ++ " (" ++ show id ++ ")"
data Property = Health Int
              | Hunger Int
              | Thirst Int
              deriving (Eq, Show)

moveEntity :: Speed -> Entity -> IO Entity
moveEntity speed (Entity nm id x y ps) = do
  gen <- newStdGen
  let (dx, newgen) = randomR (speed, -speed) gen
      (by, _) = random newgen :: (Bool,StdGen)
      dy = sqrt (speed^2 - dx^2) * if by then 1 else -1
  return $ Entity nm id (x+dx) (y+dy) ps
