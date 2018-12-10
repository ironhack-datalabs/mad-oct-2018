#! /bin/bash
function checkCommand {
    CMD=$1
    HELP_INSTALL=$2
    if ! [ -x "$(command -v $CMD)" ]; then
        echo "Error: $CMD is not installed." >&2
        if [ -n "$HELP_INSTALL" ]; then 
            echo $HELP_INSTALL 
        fi
        exit 1
    fi
}

# Check installed packages first
checkCommand "git"
checkCommand "spark-shell"
checkCommand "jupyter"

# Platform dependent checks and SPARK_HOME EXPORT
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    export SPARK_HOME=/home/$(whoami)/spark
elif [[ "$OSTYPE" == "darwin"* ]]; then
    checkCommand "brew"
    INSTALLED_SPARK_VERSION=$(brew info --json=v1  apache-spark | jq -r ".[0].installed[0].version")
    echo "Using installed spark: $INSTALLED_SPARK_VERSION"
    export SPARK_HOME=/usr/local/Cellar/apache-spark/$INSTALLED_SPARK_VERSION/libexec
else
    echo "NOT SUPPORTED OS"
    exit 1;
fi

# Configure pyspark
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
export PYSPARK_PYTHON=python3
pyspark &
sleep 5
open "http://localhost:4040"
wait %1