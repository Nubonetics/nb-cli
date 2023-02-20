"""System properties."""
import platform

from rich.table import Table


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

    table = Table("Property", "Value", title="System Properties")

    for row in table_data:
        table.add_row(*row)

    return table
