;; Authors: Theodor Amariucai & Bora M. Alper (in no particular order)

(define (problem parking)
    (:domain finitech)
    
    (:objects
        Robot - robot
        Car1 - car
        Car2 - car
        Car3 - car
        Car4 - car
        Car5 - car
        
        R0C0 - blockedTile
        R0C1 - parkingTile
        R0C2 - roadTile
        R0C3 - parkingTile
        R1C0 - blockedTile
        R1C1 - parkingTile
        R1C2 - roadTile
        R1C3 - parkingTile
        R2C0 - hubTile
        R2C1 - roadTile
        R2C2 - roadTile
        R2C3 - parkingTile
        R3C0 - hubTile
        R3C1 - roadTile
        R3C2 - roadTile
        R3C3 - parkingTile
        R4C0 - hubTile
        R4C1 - roadTile
        R4C2 - roadTile
        R4C3 - parkingTile
        R5C0 - hubTile
        R5C1 - roadTile
        R5C2 - roadTile
        R5C3 - parkingTile
    )

    (:init
        (IsAt Robot R5C1)
        (IsCarrying Robot Car4)
        (IsAt Car1 R5C0)
        (IsAt Car2 R4C0)
        (IsAt Car3 R0C1)
        (IsAt Car5 R0C3)
        (AwaitingParking Car1)
        (AwaitingParking Car2)
        (AwaitingDelivery Car3)
        (AwaitingDelivery Car4)
        
        (IsToTheLeftOf R0C0 R0C1)
        (IsToTheLeftOf R0C1 R0C2)
        (IsToTheLeftOf R0C2 R0C3)
        (IsToTheLeftOf R1C0 R1C1)
        (IsToTheLeftOf R1C1 R1C2)
        (IsToTheLeftOf R1C2 R1C3)
        (IsToTheLeftOf R2C0 R2C1)
        (IsToTheLeftOf R2C1 R2C2)
        (IsToTheLeftOf R2C2 R2C3)
        (IsToTheLeftOf R3C0 R3C1)
        (IsToTheLeftOf R3C1 R3C2)
        (IsToTheLeftOf R3C2 R3C3)
        (IsToTheLeftOf R4C0 R4C1)
        (IsToTheLeftOf R4C1 R4C2)
        (IsToTheLeftOf R4C2 R4C3)
        (IsToTheLeftOf R5C0 R5C1)
        (IsToTheLeftOf R5C1 R5C2)
        (IsToTheLeftOf R5C2 R5C3)

        (IsAbove R0C0 R1C0)
        (IsAbove R0C1 R1C1)
        (IsAbove R0C2 R1C2)
        (IsAbove R0C3 R1C3)
        (IsAbove R1C0 R2C0)
        (IsAbove R1C1 R2C1)
        (IsAbove R1C2 R2C2)
        (IsAbove R1C3 R2C3)
        (IsAbove R2C0 R3C0)
        (IsAbove R2C1 R3C1)
        (IsAbove R2C2 R3C2)
        (IsAbove R2C3 R3C3)
        (IsAbove R3C0 R4C0)
        (IsAbove R3C1 R4C1)
        (IsAbove R3C2 R4C2)
        (IsAbove R3C3 R4C3)
        (IsAbove R4C0 R5C0)
        (IsAbove R4C1 R5C1)
        (IsAbove R4C2 R5C2)
        (IsAbove R4C3 R5C3)
    )

    (:goal (and
        (not (exists (?c - car) (or
            (AwaitingParking ?c)
            (AwaitingDelivery ?c)
        )))
    ))
)

