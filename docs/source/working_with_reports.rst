Working with Reports
--------------------
When a scan job completes, it provides information that can then be viewed as a report. Data from a single scan job can be viewed in a report, but you can also merge the results of multiple scan jobs and then create a report from the merged results.

Viewing the Scan Report
^^^^^^^^^^^^^^^^^^^^^^^
When the scan job completes, you have the capability to produce a report for that scan job. You can request a report with all the details, or facts, of the scan, or request a report with a summary. The summary report process runs steps to merge the facts found during the inspection of the various hosts that are contacted during the scan. When possible, the report process also runs steps to deduplicate redundant systems. For both types of reports, you can produce the report in JavaScript Object Notation (JSON) format or comma-separated values (CSV) format.

To generate a summary report, enter the ``report summary`` command and specify the identifier for the scan job and the format for the output file.

For example, if you want to create the report summary for a scan with the scan job identifier of ``1`` and you want to generate that report in CSV format in the ``~/scan_result.csv`` file, you would enter the following command::

  # qpc report summary --scan-job 1 --csv --output-file=~/scan_result.csv

However, if you want to create the detailed report, you would use the ``report detail`` command.  This command takes the same options as the ``report summary`` command. The output is not deduplicated and merged, so it contains all facts from each source. For example, to create the detailed report for a scan with the scan job identifier ``1``, with CSV output in the ``~/scan_result.csv`` file, you would enter the following command::

  # qpc report detail --scan-job 1 --csv --output-file=~/scan_result.csv

Merging Scan Results
^^^^^^^^^^^^^^^^^^^^
You can combine results from two or more scan jobs, reports, or JSON details report files and use that merged data to create a single report. You can start this process by using the ``qpc report merge`` command.

For example, if you want to merge the results from the scan jobs with identifiers of ``11``, ``15``, and ``22``, you would enter the following command::

  # qpc report merge --job-ids 11 15 22

If you want to merge the results from reports with identifiers of ``1``, ``2``, and ``3``, you would enter the following command::

  # qpc report merge --report-ids 1 2 3

Additionally, if you would like to create a merged report from JSON details report files, you would enter the following command::

  # qpc report merge --json-files /path/to/file1.JSON /path/to/file2.JSON

The output of the above commands provides a report identifier that can be used to access the merged data. You can use this identifier and the ``qpc report`` command with the ``detail`` or ``summary`` subcommands to generate a report from the merged results.
