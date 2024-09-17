Inside this project, there are two files that loop to a set of Google Cloud projects and return a list of principals, both on a project-level scope, and a dataset-level.
Be aware that you need to have at least roles/viewer permissions on the projects you'd like to target.


To use these scripts, follow the following steps:
1. Please populate the `project_ids` field in both python files with a list of Google Cloud projects you want to scan.
2. Install the Google Cloud CLI SDK on your device.
3. Authenticate to the SDK with `gcloud auth application-default login`.
4. Activate a VirtualEnv and install the dependencies. 
5. Run the Python scripts.
6. In your current directory, there are now two files created that you can import in BigQuery for evaluation.

