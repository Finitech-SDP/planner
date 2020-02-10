#!/usr/bin/env bash

docker run -it -v $(pwd):/finitech:ro lapkt/lapkt-public /usr/bin/env bash -c "./siw_plus --domain /finitech/domain.pddl --problem /finitech/problem.pddl --output plan.txt && cat plan.txt"
