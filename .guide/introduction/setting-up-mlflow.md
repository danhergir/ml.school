# Setting Up MLflow

[MLflow](https://mlflow.org/) is a platform-agnostic AI/ML lifecycle management tool that will help us track experiments and share and deploy models. 

The different workflows we'll run as part of the project will connect to an MLflow server to store all of the data they generate and track and version the models. 

To run an MLflow server locally, open a terminal window and run the following command:

```shell
just mlflow
```

This command will start an MLflow server bound to `0.0.0.0` and listening on port `5001`. We'll need to keep this server running while we work on the project.

This command starts MLflow in development mode on port `5001`, binding it to `0.0.0.0` and allowing browser requests from forwarded ports and workspace previews. The project uses `5001` by default because `5000` is commonly occupied by macOS and editor helper processes, which can cause confusing `403` responses from the wrong service.

If you're running the repository directly on your machine, open [`http://127.0.0.1:5001`](http://127.0.0.1:5001) in a browser. If you're running inside a container or cloud workspace, open the forwarded preview URL for port `5001` instead.

For more information on how to run the MLflow server, check [Common ways to set up MLflow](https://mlflow.org/docs/latest/tracking.html#common-setups). You can also run the following command to get more information:

```shell
mlflow server --help
```
