from planner import Planner
from planner.kinds import Car, Robot


def main():
    p = Planner()

    plan = p.plan(
        None,
        cars=[Car(0, 3, Car.CarStatus.AWAITING_PARKING)],
        robot=Robot(2, 0)
    )
    print("PLAN")
    for step in plan:
        print(f"\t{step}")


if __name__ == "__main__":
    main()
