"""System properties."""
import platform


def system_properties() -> str:
    """System properties."""
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

    # Return the table
    output_table="System Properties:\n"
    for row in table_data:
        output_table+=f"{row[0]:20} : {row[1]}\n"
    return output_table
