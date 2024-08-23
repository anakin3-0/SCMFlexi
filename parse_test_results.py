import xml.etree.ElementTree as ET
import csv
import sys

def parse_test_results(xml_file, csv_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Open CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Test Case', 'Status', 'Time (s)'])

        # Iterate through each test case in the XML
        for testcase in root.iter('testcase'):
            name = testcase.get('name')
            time = testcase.get('time')
            status = 'Passed'

            # Check for failure or error
            if testcase.find('failure') is not None:
                status = 'Failed'
            elif testcase.find('error') is not None:
                status = 'Error'

            # Write the test case result to the CSV file
            writer.writerow([name, status, time])

if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: python parse_test_results.py <input_xml_file> <output_csv_file>")
        sys.exit(1)

    xml_file = sys.argv[1]
    csv_file = sys.argv[2]

    # Parse the test results and write to CSV
    parse_test_results(xml_file, csv_file)

