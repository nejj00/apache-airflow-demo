# Apache Demo Project

## WSL Configuration

If using Windows as OS, WSL needs to be installed, because Airflow has a better support for Mac and Unix:

### WSL installation

[Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)

[Get started using Visual Studio Code with Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

### Git on WSL

Git:

```bash
sudo apt install git-all
```

GitHub CLI:

[Installing gh on Linux and BSD](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)

Setting email and user:

```bash
git config --global user.email "email"
config --global user.name "username"
```

### Apache Airflow installation 

1. Update the WSL package manager:

```bash
   sudo apt update && sudo apt upgrade -y
```

2. Install Python and required tools:

```bash
   sudo apt install -y python3 python3-pip python3-venv
```

3. Create a virtual environment for Airflow:

```bash
   python3 -m venv airflow-venv
   source airflow-venv/bin/activate
```

4. Install Apache Airflow using pip:

```bash
   pip install apache-airflow
```

Optionally, if you need specific extras like celery, postgres, or mysql:

```bash
   pip install "apache-airflow[celery,postgres]"
```

5. Initialize the Airflow database:

```bash
   airflow db init
```

6. Create an admin user:

```bash
   airflow users create \
       --username admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email <admin@example.com>
```

7. Start the Airflow webserver and scheduler:

```bash
   airflow webserver -p 8080
   airflow scheduler
```