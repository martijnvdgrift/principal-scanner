import csv
from google.cloud import resourcemanager_v3
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.api_core.exceptions import GoogleAPIError


def list_principals_for_project(client, project_id):
    principals = []
    try:

        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource=f"projects/{project_id}",
        )

        # Make the request
        response = client.get_iam_policy(request=request)

        for binding in response.bindings:
            for member in binding.members:
                principals.append({
                    'project': project_id,
                    'principal': member,
                    'role': binding.role
                })

    except GoogleAPIError as e:
        print(f"An error occurred: {e}")

    return principals


def main(project_ids, output_csv):
    client = resourcemanager_v3.ProjectsClient()
    all_principals = []

    for project_id in project_ids:
        principals = list_principals_for_project(client, project_id)
        all_principals.extend(principals)

    # Write to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['project', 'principal', 'role']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for principal in all_principals:
            writer.writerow(principal)


if __name__ == '__main__':
    project_ids = [''] #todo: add project IDs here

    # Output CSV file
    output_csv = 'google_project_principals.csv'

    main(project_ids, output_csv)
    print(f"Output saved to {output_csv}")
