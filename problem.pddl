(define (problem waiting-XX) ;; Replace XX with task number
    (:domain waiting)
    (:objects
        ;; Machine Generated Map Below
        ;; Do NOT edit manually, use map-editor instead
        R0C0 - dropoff
        R0C1 - road
        R0C2 - road
        R0C3 - road
        R0C4 - road
        R0C5 - road
        R0C6 - road
        R0C7 - road
        R0C8 - road
        R0C9 - road
        R1C0 - road
        R1C1 - park
        R1C2 - park
        R1C3 - park
        R1C4 - park
        R1C5 - park
        R1C6 - road
        R1C7 - park
        R1C8 - park
        R1C9 - road
        R2C0 - road
        R2C1 - road
        R2C2 - road
        R2C3 - road
        R2C4 - road
        R2C5 - road
        R2C6 - road
        R2C7 - park
        R2C8 - park
        R2C9 - road
        R3C0 - road
        R3C1 - park
        R3C2 - park
        R3C3 - park
        R3C4 - park
        R3C5 - park
        R3C6 - road
        R3C7 - park
        R3C8 - park
        R3C9 - road
        R4C0 - pickup
        R4C1 - road
        R4C2 - road
        R4C3 - road
        R4C4 - road
        R4C5 - road
        R4C6 - road
        R4C7 - road
        R4C8 - road
        R4C9 - road
    )

    (:init
        (IsAt Car R0C0)
        (IsAt Robot R4C9)

        ;; Machine Generated Map Below
        ;; Do NOT edit manually, use map-editor instead.
        (IsToTheLeft R0C0 R0C1)
        (IsToTheLeft R0C1 R0C2)
        (IsToTheLeft R0C2 R0C3)
        (IsToTheLeft R0C3 R0C4)
        (IsToTheLeft R0C4 R0C5)
        (IsToTheLeft R0C5 R0C6)
        (IsToTheLeft R0C6 R0C7)
        (IsToTheLeft R0C7 R0C8)
        (IsToTheLeft R0C8 R0C9)
        (IsToTheUp R0C0 R1C0)
        (IsToTheUp R0C1 R1C1)
        (IsToTheLeft R1C0 R1C1)
        (IsToTheUp R0C2 R1C2)
        (IsToTheLeft R1C1 R1C2)
        (IsToTheUp R0C3 R1C3)
        (IsToTheLeft R1C2 R1C3)
        (IsToTheUp R0C4 R1C4)
        (IsToTheLeft R1C3 R1C4)
        (IsToTheUp R0C5 R1C5)
        (IsToTheLeft R1C4 R1C5)
        (IsToTheUp R0C6 R1C6)
        (IsToTheLeft R1C5 R1C6)
        (IsToTheUp R0C7 R1C7)
        (IsToTheLeft R1C6 R1C7)
        (IsToTheUp R0C8 R1C8)
        (IsToTheLeft R1C7 R1C8)
        (IsToTheUp R0C9 R1C9)
        (IsToTheLeft R1C8 R1C9)
        (IsToTheUp R1C0 R2C0)
        (IsToTheUp R1C1 R2C1)
        (IsToTheLeft R2C0 R2C1)
        (IsToTheUp R1C2 R2C2)
        (IsToTheLeft R2C1 R2C2)
        (IsToTheUp R1C3 R2C3)
        (IsToTheLeft R2C2 R2C3)
        (IsToTheUp R1C4 R2C4)
        (IsToTheLeft R2C3 R2C4)
        (IsToTheUp R1C5 R2C5)
        (IsToTheLeft R2C4 R2C5)
        (IsToTheUp R1C6 R2C6)
        (IsToTheLeft R2C5 R2C6)
        (IsToTheUp R1C7 R2C7)
        (IsToTheLeft R2C6 R2C7)
        (IsToTheUp R1C8 R2C8)
        (IsToTheLeft R2C7 R2C8)
        (IsToTheUp R1C9 R2C9)
        (IsToTheLeft R2C8 R2C9)
        (IsToTheUp R2C0 R3C0)
        (IsToTheUp R2C1 R3C1)
        (IsToTheLeft R3C0 R3C1)
        (IsToTheUp R2C2 R3C2)
        (IsToTheLeft R3C1 R3C2)
        (IsToTheUp R2C3 R3C3)
        (IsToTheLeft R3C2 R3C3)
        (IsToTheUp R2C4 R3C4)
        (IsToTheLeft R3C3 R3C4)
        (IsToTheUp R2C5 R3C5)
        (IsToTheLeft R3C4 R3C5)
        (IsToTheUp R2C6 R3C6)
        (IsToTheLeft R3C5 R3C6)
        (IsToTheUp R2C7 R3C7)
        (IsToTheLeft R3C6 R3C7)
        (IsToTheUp R2C8 R3C8)
        (IsToTheLeft R3C7 R3C8)
        (IsToTheUp R2C9 R3C9)
        (IsToTheLeft R3C8 R3C9)
        (IsToTheUp R3C0 R4C0)
        (IsToTheUp R3C1 R4C1)
        (IsToTheLeft R4C0 R4C1)
        (IsToTheUp R3C2 R4C2)
        (IsToTheLeft R4C1 R4C2)
        (IsToTheUp R3C3 R4C3)
        (IsToTheLeft R4C2 R4C3)
        (IsToTheUp R3C4 R4C4)
        (IsToTheLeft R4C3 R4C4)
        (IsToTheUp R3C5 R4C5)
        (IsToTheLeft R4C4 R4C5)
        (IsToTheUp R3C6 R4C6)
        (IsToTheLeft R4C5 R4C6)
        (IsToTheUp R3C7 R4C7)
        (IsToTheLeft R4C6 R4C7)
        (IsToTheUp R3C8 R4C8)
        (IsToTheLeft R4C7 R4C8)
        (IsToTheUp R3C9 R4C9)
        (IsToTheLeft R4C8 R4C9)
    )

    (:goal (and
        (exists (?ps - park) (and
            (IsAt Car ?ps)
        ))
    ))
)
