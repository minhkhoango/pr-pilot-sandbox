# Dummy data for testing, if needed.
# report = {
#     "item_count": 120,
#     "items": {
#         "laptop": 1200.00,
#         "mouse": 25.50,
#         "keyboard": 75.00
#     }
# }

def process_inventory_report(report_data: dict[str, int | dict[str, int]], department: str) -> str:
    """
    Processes a dictionary of inventory data and generates a department summary.
    """
    # PROBLEM 1: THE SILENT BUG
    total_items = report_data.get('item_cont', 0) 
    
    # PROBLEM 2: INEFFICIENT & UNREADABLE
    most_expensive_item = ""
    max_price = -1
    if 'items' in report_data and report_data['items']:
        for item, price in report_data['items'].items():
            if price > max_price:
                max_price = price
                most_expensive_item = item

    summary = f"Inventory Report for {department.upper()}:\n"
    summary += f"Total items: {total_items}\n"
    if most_expensive_item:
        summary += f"Most expensive item: {most_expensive_item} at ${max_price:.2f}\n"

    # PROBLEM 3: REPEATING YOURSELF (DRY VIOLATION)
    if total_items == 0:
        status_message = f"Department '{department}' is out of stock."
        summary += f"Status: CRITICAL - {status_message}"
        print(f"LOG: {status_message}") # Pretend this is a log call
    elif total_items < 50:
        status_message = f"Department '{department}' has low stock."
        summary += f"Status: WARNING - {status_message}"
        print(f"LOG: {status_message}") # Pretend this is a log call
    else:
        status_message = f"Department '{department}' has sufficient stock."
        summary += f"Status: OK - {status_message}"
        print(f"LOG: {status_message}") # Pretend this is a log call
        
    return summary

# print(process_inventory_report(report, "Electronics"))
