(define (domain waiting)
    (:requirements :adl )

    (:types
        robot - mover
        car - mover

        ;; kind of tiles
        road - tile
        park - tile
        pickup - tile
        dropoff - tile
    )

    (:constants
        Robot - robot
        Car - car
    )

    (:predicates
        ;; Example:
        ;; (Contains ?x - object ?c - container)

        (IsAt ?m - mover ?t - tile)
        (Occupied ?p - park)
        (HasLifted ?r - robot ?c - car)

        (IsToTheLeft ?a - tile ?b - tile)
        (IsToTheUp ?a - tile ?b - tile)
    )

    ;;;; Action Template - Delete and fill in own actions ;;;;

    (:action lift-car
        :parameters (?r - robot ?c - car ?t - tile)
        :precondition (and
            (IsAt ?r ?t)
            (IsAt ?c ?t)
         )
        :effect (and
            (HasLifted ?r ?c)
            (not (IsAt ?c ?t))
        )
    )

    (:action park-car-at
        :parameters (?r - robot ?c - car ?ps - park)
        :precondition (and
            (IsAt ?r ?ps)
            (HasLifted ?r ?c)
            (not (Occupied ?ps))
        )
        :effect (and
            (not (HasLifted ?r ?c))
            (Occupied ?ps)
            (IsAt ?c ?ps)
        )
    )

    (:action go-left
        :parameters (?r - robot ?f - tile ?t - tile)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheLeft ?t ?f)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )

    (:action go-right
        :parameters (?r - robot ?f - tile ?t - tile)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheLeft ?f ?t)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )

    (:action go-up
        :parameters (?r - robot ?f - tile ?t - tile)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheUp ?t ?f)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )

    (:action go-down
        :parameters (?r - robot ?f - tile ?t - tile)
        :precondition (and
            (IsAt ?r ?f)
            (IsToTheUp ?f ?t)
        )
        :effect (and
            (not (IsAt ?r ?f))
            (IsAt ?r ?t)
        )
    )
)
