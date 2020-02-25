#!/usr/bin/env python3

import sys
import textwrap
import os
import json

from urllib.request import Request, urlopen

# Path to the PDDL4J jar, relative to the path of this script file
# (NOT THE WORKING DIRECTORY).
PDDL4J_JAR = "./pddl4j-3.8.2.jar"

def main(argv):
    print("Bora's PDDL Companion v0.3.0", end="\n\n")

    if len(argv) == 4 and argv[1] == "check":
        check(domain_path=argv[2], problem_path=argv[3])
    elif len(argv) == 4 and argv[1] == "plan":
        plan(domain_path=argv[2], problem_path=argv[3])
    else:
        print("Usage:")
        print("\tSyntax Check: {} check <DOMAIN> <PROBLEM>".format(argv[0]))
        print("\tRun Planner : {} plan  <DOMAIN> <PROBLEM>".format(argv[0]))


def check(domain_path, problem_path):
    jar_path = os.path.join(os.path.dirname(__file__), PDDL4J_JAR)

    s = 'java -javaagent:"{}" fr.uga.pddl4j.parser.Parser -o "{}" -f "{}"'.format(
            jar_path,
            domain_path,
            problem_path
    )
    os.system(s)
    print()


def plan(domain_path, problem_path):
    data = {
        "domain" : open(domain_path, 'r').read(),
        "problem": open(problem_path, 'r').read()
    }

    req = Request("http://solver.planning.domains/solve")
    req.add_header("Content-Type", "application/json")
    resp = json.loads(urlopen(req, json.dumps(data).encode("ascii")).read().decode("ascii"))

    print("Status:", resp["status"])
    print("Parsing status:", resp["result"]["parse_status"])
    print()

    prefix = "\t"

    if resp["status"] == "error":
            print("================ ERROR")
            print(textwrap.indent(resp["result"]["error"], prefix))
            print("================ OUTPUT")
            print(textwrap.indent(resp["result"]["output"], prefix))
    else:
            print("================ PLAN")
            for p in resp["result"]["plan"]:
                    print("\t%s" % (p, ))

            print()
            print("================ OUTPUT")
            print(textwrap.indent(resp["result"]["output"], prefix))


if __name__ == "__main__":
    main(sys.argv)
