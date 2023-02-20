"""System information."""
import platform

from rich.table import Table


def system_info() -> str:
    """Get system information."""
    sys_info = platform.uname()

    # Create a table
    table_data = [
        ["System Name", sys_info.system],
        ["Node Name", sys_info.node],
        ["Release", sys_info.release],
        ["Version", sys_info.version],
        ["Machine", sys_info.machine],
        ["Processor", sys_info.processor],
    ]

    table = Table("Property", "Value", title="System Information")

    for row in table_data:
        table.add_row(*row)

    return table
