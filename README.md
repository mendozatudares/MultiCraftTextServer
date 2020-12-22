# MultiCraftTextServer
Serverless function deployed to Azure, tasked with parsing natural language commands received from MultiCraft clients

## Development Setup
These are instructions for setting up MultiCraftTextServer on your system for development. Note that the instructions below have been run in Bash on Debian 10 (buster).
The TextServer has been set up to deploy to Microsoft Azure Functions. Please see these guides for using either [VS Code](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python#configure-your-environment) or the [Command Line](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser#configure-your-local-environment) for configuring your environment.

Setup a new python virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
Use the Azure Functions Core Tools for initiating the function using `func init`. Be sure to choose python for the worker runtime.

See the [MultiCraftServer repo](https://github.com/mendozatudares/MultiCraftServer/) for information about setting up a Minecraft server with MultiCraft running on it.

## Startup
The TextServer may run locally using `func start` in the MultiCraftTextServer directory or by pressing `F5` in VS Code. The endpoint that the function will be running at should be of the form `https://localhost:XXXX/httptrigger1`.
```
source .venv/bin/activate
func start
```
You can then test the function by accessing the endpoint using your browser or a [MultiCraftClient](https://github.com/mendozatudares/MultiCraftClient/releases/). Be sure to have a Minecraft server with MultiCraft to ensure commands go through.
