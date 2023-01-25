from utilities.commons.runner_commands import Runner
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run_env",required=True, \
                        help="anyone choice from local,local_to_docker, \
                        docker is expected(basically, where you want to run tests)")
    args = parser.parse_args()
    os.environ["RUN_ENV"] = args.run_env

    if os.environ["RUN_ENV"] not in ["local","local_to_docker","docker","db_docker"]:
        raise ValueError("Invalid run env was passed, Please choose from [local,local_to_docker,docker]")
    else:
        if os.environ["RUN_ENV"] in ["local_to_docker"]:
            Runner.run_docker_compose_build()
            Runner.run_docker_compose_up()
            Runner.run_behave_test_local_command()
        elif os.environ["RUN_ENV"] in ["docker"]:
            Runner.run_docker_compose_build()
            Runner.run_docker_compose_up()
            Runner.run_behave_test_docker_command()
        elif os.environ["RUN_ENV"] in ["db_docker"]:
            Runner.run_db_docker_compose_build()
            Runner.run_db_docker_compose_up()
        else:
            Runner.run_behave_test_local_command()

    if os.environ["RUN_ENV"] in ["local_to_docker","docker"]:
        Runner.run_docker_compose_down()
        Runner.run_docker_system_prune()



