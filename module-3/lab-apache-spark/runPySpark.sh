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
checkCommand "brew"
checkCommand "jq" "install with: brew install jq"
checkCommand "spark-shell" "install with: brew install apache-spark"
checkCommand "jupyter"


INSTALLED_SPARK_VERSION=$(brew info --json=v1  apache-spark | jq -r ".[0].installed[0].version")
echo "Using installed spark: $INSTALLED_SPARK_VERSION"
export SPARK_HOME=/usr/local/Cellar/apache-spark/$INSTALLED_SPARK_VERSION/libexec
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
export PYSPARK_PYTHON=python3
pyspark &
sleep 5
open "http://localhost:4040"
wait %1