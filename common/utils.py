from pathlib import Path


def read_docker_secrets_file(secret: str, path: str = "/run/secrets") -> str | None:
    """
    Read the specified secrets file

    :params secrete: Name of secrete file
    :params path: Path to secret file if not in the standard location
    """
    try:
        file_path = Path(path).joinpath(secret)
        with open(file_path) as f:
            return f.readline()
    except FileNotFoundError:
        return None
