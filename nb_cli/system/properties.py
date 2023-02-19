"""System properties"""
import platform


def SystemProperties():
    # Get system info
    system_info = platform.uname()

    # Create a table
    table_data = [
        ["System Name", system_info.system],
        ["Node Name", system_info.node],
        ["Release", system_info.release],
        ["Version", system_info.version],
        ["Machine", system_info.machine],
        ["Processor", system_info.processor],
    ]

    # Output the table
    print("System Properties:")
    for row in table_data:
        print(f"{row[0]:20} : {row[1]}")
