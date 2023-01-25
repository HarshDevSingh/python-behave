import subprocess


class Runner:

    @staticmethod
    def run_docker_system_prune():
        response = subprocess.run("yes | docker system prune", shell=True)
        assert response.returncode == 0, "run docker system prune execution failed"

    @staticmethod
    def run_docker_compose_build():
        response = subprocess.run("docker compose build", shell=True)
        assert response.returncode == 0, "run_docker_compose_build execution failed"

    @staticmethod
    def run_docker_compose_up():
        response = subprocess.run("docker compose up -d", shell=True)
        assert response.returncode == 0, "run_docker_compose_up execution failed"

    @staticmethod
    def run_db_docker_compose_build():
        response = subprocess.run("docker compose -f docker-compose-db.yml build", shell=True)
        assert response.returncode == 0, "run_db_docker_compose_build execution failed"

    @staticmethod
    def run_db_docker_compose_up():
        response = subprocess.run("docker compose -f docker-compose-db.yml up -d", shell=True)
        assert response.returncode == 0, "run_db_docker_compose_up execution failed"

    @staticmethod
    def run_docker_compose_down():
        response = subprocess.run("docker compose down", shell=True)
        assert response.returncode == 0, "run_docker_compose_up execution failed"

    @staticmethod
    def run_behave_test_local_command():
        response = subprocess.run("behave --no-capture", shell=True)
        assert response.returncode == 0, "run_docker_compose_build execution failed"

    @staticmethod
    def run_behave_test_docker_command():
        response = subprocess.run("docker compose run --rm python behave --no-capture", shell=True)
        assert response.returncode == 0, "run_behave_docker_command execution failed"

