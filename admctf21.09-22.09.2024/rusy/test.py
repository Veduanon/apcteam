from datetime import datetime

# List of date pairs
date_pairs = [
    ('1984/01/21', '1984/03/26'),
    ('2015/12/29', '2016/04/07'),
    ('2005/08/02', '2005/11/19'),
    ('1982/09/05', '1982/11/11'),
    ('1980/04/06', '1980/06/29'),
    ('1998/03/16', '1998/05/25'),
    ('1993/06/26', '1993/10/27'),
    ('2021/05/01', '2021/07/08'),
    ('1984/02/18', '1984/04/10'),
    ('1984/09/16', '1985/01/10'),
    ('2001/04/04', '2001/07/14'),
    ('2022/02/13', '2022/05/19'),
    ('2021/08/03', '2021/11/11'),
    ('1986/08/26', '1986/10/14'),
    ('2012/06/06', '2012/08/15'),
    ('1989/11/07', '1990/02/17'),
    ('1996/01/15', '1996/03/24'),
    ('1990/11/25', '1991/02/15'),
    ('2017/01/14', '2017/04/25'),
    ('2009/02/25', '2009/06/15'),
    ('2003/04/14', '2003/07/22'),
    ('2006/08/21', '2006/10/29'),
    ('1990/03/31', '1990/07/04'),
    ('1984/03/15', '1984/05/06'),
    ('1987/03/10', '1987/06/18'),
    ('2012/03/10', '2012/06/04'),
    ('2004/06/28', '2004/10/07'),
    ('2014/09/08', '2014/12/27'),
    ('1999/05/28', '1999/07/22'),
    ('2021/12/29', '2022/04/25'),
    ('1982/02/22', '1982/06/16'),
    ('2000/02/13', '2000/04/22'),
    ('1995/06/24', '1995/10/27')
]

# Function to calculate days between two dates
def calculate_days_between(start_date, end_date):
    start = datetime.strptime(start_date, '%Y/%m/%d')
    end = datetime.strptime(end_date, '%Y/%m/%d')
    return (end - start).days

# Calculating intervals in days
intervals_in_days = [(pair[0], pair[1], calculate_days_between(pair[0], pair[1])) for pair in date_pairs]


print(intervals_in_days)

# import pandas as pd

# # Creating a DataFrame for better visualization
# df = pd.DataFrame(intervals_in_days, columns=["Start Date", "End Date", "Interval (Days)"])

# import ace_tools as tools; tools.display_dataframe_to_user(name="Date Intervals", dataframe=df)
