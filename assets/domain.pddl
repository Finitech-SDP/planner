;; Authors: Theodor Amariucai & Bora M. Alper (in no particular order)

(define (domain finitech)
    (:requirements :adl )

    (:types
        ;; kind of tiles
        blockedTile - tile  ;; you never go there, physically always blocked
        roadTile - tile
        parkingTile - tile  ;; occupied, otherwise available
        hubTile - tile ;; for waiting dropoff or waiting pickup, available otherwise

        car - dynamic  ;; cars can only be moved around with the help of the robot
        robot - dynamic
    )

    (:constants
        Robot - robot
    )

    (:predicates
        (TemporarilyBlocked ?t - tile)

        ;; TODO: enforce that one and only one is true at a given time

        ;; The Car is waiting to be parked
        (AwaitingParking ?c - car)

        ;; Tha Car is waiting to be picked up by the owner
        (AwaitingDelivery ?c - car)

        (IsToTheLeftOf ?a - tile ?b - tile)
        (IsAbove ?a - tile ?b - tile)

        (IsAt ?m - dynamic ?t - tile)

        (IsCarrying ?r - robot ?c - car)
    )

    ;;;;;; WE ASSUME HORIZONTAL TILES!
    (:action go-left
        :parameters (?r - robot ?f - tile ?t - roadTile)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheLeftOf ?t ?f)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )

    (:action go-right
        :parameters (?r - robot ?f - tile ?t - roadTile)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheLeftOf ?f ?t)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )

    (:action go-up
        :parameters (?r - robot ?f - roadTile ?t - roadTile)
        :precondition (and
            (IsAt ?r ?f)
            (IsAbove ?t ?f)
            ;; TODO: for blocking space
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )

    (:action go-down
        :parameters (?r - robot ?f - roadTile ?t - roadTile)
        :precondition (and
            (IsAt ?r ?f)
            (IsAbove ?f ?t)
            ;; TODO: for blocking space
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )

    ;; 1) scan
    ;; 2) slide under
    ;; 3) lift
    ;; END
    (:action pickup-car-leftwards
        :parameters (?r - robot ?f - roadTile ?t - hubTile ?c - car)
        :precondition (and
            (IsAt ?r ?f)
            (IsAt ?c ?t)
            (IsToTheLeftOf ?t ?f)

            (not (exists (?c2 - car) (and (IsCarrying ?r ?c2))))

            (AwaitingParking ?c)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)

            (not (IsAt ?c ?t))
            (IsCarrying ?r ?c)
        )
    )

    (:action dropoff-car-leftwards
        :parameters (?r - robot ?f - roadTile ?t - hubTile ?c - car)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheLeftOf ?t ?f)
            (IsCarrying ?r ?c)

            (not (exists (?c2 - car) (IsAt ?c2 ?t)))

            (AwaitingDelivery ?c)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)

            (not (IsCarrying ?r ?c))
            (IsAt ?c ?t)

            (not (AwaitingDelivery ?c))
        )
    )

    (:action park-car-rightwards
        :parameters (?r - robot ?f - roadTile ?t - parkingTile ?c - car)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheLeftOf ?f ?t)
            (IsCarrying ?r ?c)

            (not (exists (?c2 - car) (IsAt ?c2 ?t)))
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)

            (not (IsCarrying ?r ?c))
            (IsAt ?c ?t)

            (not (AwaitingParking ?c))
        )
    )

    (:action park-car-leftwards
        :parameters (?r - robot ?f - roadTile ?t - parkingTile ?c - car)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheLeftOf ?t ?f)
            (IsCarrying ?r ?c)

            (not (exists (?c2 - car) (IsAt ?c2 ?t)))
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)

            (not (IsCarrying ?r ?c))
            (IsAt ?c ?t)

            (not (AwaitingParking ?c))
        )
    )

    (:action retrieve-car-rightwards
        :parameters (?r - robot ?f - roadTile ?t - parkingTile ?c - car)
        :precondition (and
            (IsAt ?r ?f)
            (IsAt ?c ?t)
            (IsToTheLeftOf ?f ?t)
            (not (exists (?c2 - car) (and
                (IsCarrying ?r ?c2)
            )))
            (AwaitingDelivery ?c)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)

            (not (IsAt ?c ?t))
            (IsCarrying ?r ?c)
        )
    )

    (:action retrieve-car-leftwards
        :parameters (?r - robot ?f - roadTile ?t - parkingTile ?c - car)
        :precondition (and
            (IsAt ?r ?f)
            (IsAt ?c ?t)
            (IsToTheLeftOf ?t ?f)
            (not (exists (?c2 - car) (and
                (IsCarrying ?r ?c2)
            )))
            (AwaitingDelivery ?c)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)

            (not (IsAt ?c ?t))
            (IsCarrying ?r ?c)
        )
    )
)
