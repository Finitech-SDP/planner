#!/usr/bin/env bash

# docker run --rm -it -v $(pwd):/finitech:ro lapkt/lapkt-public /usr/bin/env bash -c "./siw_plus --domain /finitech/domain.pddl --problem /finitech/problem.pddl --output plan.txt && cat plan.txt"
./siw-then-bfsf --domain domain.pddl --problem problem.pddl --output plan.txt && ./validate domain.pddl problem.pddl plan.txt && cat plan.txt
