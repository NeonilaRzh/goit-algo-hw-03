from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        difference = (input_date - current_date).days
        return difference
    
        """question
        return (datetime.today().date() - datetime.strptime(date, "%Y-%m-%d").date()).days 
        чи можна використати такий запис, чи вже гірше читається?
        """
       
    except ValueError:
        return f"Please enter date in format 'yyyy-mm-dd'"