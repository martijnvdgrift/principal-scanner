import csv
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError


def list_principals_for_project(project_id):
    client = bigquery.Client(project=project_id)
    principals = []

    try:
        datasets = client.list_datasets()
        for dataset in datasets:
            dataset_id = f"{project_id}.{dataset.dataset_id}"
            dataset_info = client.get_dataset(dataset_id)
            for entry in dataset_info.access_entries:
                principals.append({
                    'project': project_id,
                    'principal': entry.entity_id,
                    'dataset': dataset_info.dataset_id,
                    'role': entry.role
                })

    except GoogleAPIError as e:
        print(f"An error occurred: {e}")

    return principals


def main(project_ids, output_csv):
    all_principals = []

    for project_id in project_ids:
        principals = list_principals_for_project(project_id)
        all_principals.extend(principals)

    # Write to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['project', 'principal', 'dataset', 'role']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for principal in all_principals:
            writer.writerow(principal)


if __name__ == '__main__':
    project_ids = [''] #todo: add project IDs here

    # Output CSV file
    output_csv = 'bigquery_dataset_principals.csv'

    main(project_ids, output_csv)
    print(f"Output saved to {output_csv}")
