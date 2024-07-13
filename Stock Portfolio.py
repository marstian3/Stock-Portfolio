import matplotlib.pyplot as plt
import pandas as pd
import os

def load_portfolio():
    # Placeholder for loading portfolio data, could be from a file or database
    return {}

def save_portfolio_to_excel(portfolio):
    # Convert portfolio data to a DataFrame
    df = pd.DataFrame(list(portfolio.items()), columns=['Stock', 'Invested Amount'])
    
    # Get the current working directory
    cwd = os.getcwd()
    
    # Define the Excel file path
    excel_file = os.path.join(cwd, 'portfolio.xlsx')
    
    # Save DataFrame to Excel
    df.to_excel(excel_file, index=False)
    print(f"Portfolio data saved to {excel_file}")

def create_portfolio_pie_chart():
    portfolio = load_portfolio()
    total_investment = sum(portfolio.values())
    
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").strip()
        if stock_name.lower() == 'done':
            break
        try:
            invested_amount = float(input(f"Enter amount invested in {stock_name}: $"))
            if invested_amount <= 0:
                print("Investment amount must be greater than zero. Try again.")
                continue
            portfolio[stock_name] = portfolio.get(stock_name, 0) + invested_amount
            total_investment += invested_amount
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue
    
    if total_investment == 0:
        print("Portfolio is empty. Exiting.")
        return
    
    # Save portfolio data to Excel
    save_portfolio_to_excel(portfolio)
    
    # Calculate percentages and prepare data for the pie chart
    labels = []
    sizes = []
    other_percentage = 0.0
    
    for stock_name, invested_amount in portfolio.items():
        percentage = (invested_amount / total_investment) * 100
        if percentage >= 5:
            labels.append(stock_name)
            sizes.append(percentage)
        else:
            other_percentage += percentage
    
    # Add 'Other' category if applicable
    if other_percentage > 0:
        labels.append('Other')
        sizes.append(other_percentage)
    
    # Plotting the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Stock Portfolio Allocation')
    plt.show()

# Run the function
create_portfolio_pie_chart() 