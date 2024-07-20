import pandas as pd


def filling_missing_data(df):
    df.fillna(
        {
        "Adults (ages 15+) and children (ages 0-14) newly infected with HIV":df['Adults (ages 15+) and children (ages 0-14) newly infected with HIV'].median(),
        "Adults (ages 15-49) newly infected with HIV":df['Adults (ages 15-49) newly infected with HIV'].median(),
        "Arms exports (SIPRI trend indicator values)":df['Arms exports (SIPRI trend indicator values)'].median(),
        "Automated teller machines (ATMs) (per 100,000 adults)":df['Automated teller machines (ATMs) (per 100,000 adults)'].mean(),
        "Arms imports (SIPRI trend indicator values)":df['Arms imports (SIPRI trend indicator values)'].median(),
        "Average transaction cost of sending remittances from a specific country (%)":df['Average transaction cost of sending remittances from a specific country (%)'].mean(),
        "Average transaction cost of sending remittances to a specific country (%)":df['Average transaction cost of sending remittances to a specific country (%)'].median(),
        "Bank capital to assets ratio (%)":df['Bank capital to assets ratio (%)'].median(),
        "Bank liquid reserves to bank assets ratio (%)":df['Bank liquid reserves to bank assets ratio (%)'].median(),
        "Bank nonperforming loans to total gross loans (%)":df['Bank nonperforming loans to total gross loans (%)'].median(),
        "Charges for the use of intellectual property, payments (BoP, current US$)":df['Charges for the use of intellectual property, payments (BoP, current US$)'].median(),
        "Charges for the use of intellectual property, receipts (BoP, current US$)":df['Charges for the use of intellectual property, receipts (BoP, current US$)'].median(), 
        "Commercial bank branches (per 100,000 adults)":df["Commercial bank branches (per 100,000 adults)"].median(),
        "Computer, communications and other services (% of commercial service exports)":df["Computer, communications and other services (% of commercial service exports)"].mean(),
        "Computer, communications and other services (% of commercial service imports)":df["Computer, communications and other services (% of commercial service imports)"].mean(),
        "Consumer price index (2010 = 100)":df['Consumer price index (2010 = 100)'].median(),
        "Domestic credit provided by financial sector (% of GDP)":df['Domestic credit provided by financial sector (% of GDP)'].median(),
        "Domestic credit to private sector (% of GDP)":df['Domestic credit to private sector (% of GDP)'].median(),
        "Domestic credit to private sector by banks (% of GDP)":df['Domestic credit to private sector by banks (% of GDP)'].median(),
        "Employment to population ratio, 15+, female (%) (national estimate)":df['Employment to population ratio, 15+, female (%) (national estimate)'].mean(),
        "Employment to population ratio, 15+, male (%) (national estimate)":df["Employment to population ratio, 15+, male (%) (national estimate)"].median(),
        "Employment to population ratio, 15+, total (%) (national estimate)":df["Employment to population ratio, 15+, total (%) (national estimate)"].mean(),
        "Employment to population ratio, ages 15-24, female (%) (national estimate)":df["Employment to population ratio, ages 15-24, female (%) (national estimate)"].median(),
        "Employment to population ratio, ages 15-24, male (%) (national estimate)":df["Employment to population ratio, ages 15-24, male (%) (national estimate)"].mean(),
        "Employment to population ratio, ages 15-24, total (%) (national estimate)":df["Employment to population ratio, ages 15-24, total (%) (national estimate)"].mean(),
         "Final consumption expenditure (% of GDP)":df['Final consumption expenditure (% of GDP)'].median(),
        "Final consumption expenditure (annual % growth)":df['Final consumption expenditure (annual % growth)'].median(),
        "Final consumption expenditure (constant 2010 US$)":df['Final consumption expenditure (constant 2010 US$)'].median(),
        'Final consumption expenditure (constant LCU)':df['Final consumption expenditure (constant LCU)'].median(),
        'Final consumption expenditure (current LCU)':df['Final consumption expenditure (current LCU)'].mean(),
        'Final consumption expenditure (current US$)':df['Final consumption expenditure (current US$)'].median(),
        'Fixed broadband subscriptions':df['Fixed broadband subscriptions'].median(),
        'Fixed broadband subscriptions (per 100 people)':df['Fixed broadband subscriptions (per 100 people)'].median(),
        'Fixed telephone subscriptions':df['Fixed telephone subscriptions'].median(),
        'Fixed telephone subscriptions (per 100 people)':df['Fixed telephone subscriptions (per 100 people)'].median(),
        "GDP (constant 2010 US$)":df['GDP (constant 2010 US$)'].median(),
        "GDP growth (annual %)":df['GDP growth (annual %)'].median(),
        "GDP per capita (constant 2010 US$)":df['GDP per capita (constant 2010 US$)'].median(),
        "GNI (constant 2010 US$)":df['GNI (constant 2010 US$)'].median(),
        'GNI growth (annual %)':df['GNI growth (annual %)'].mean(),
        "GNI per capita (constant 2010 US$)":df['GNI per capita (constant 2010 US$)'].median(),
        "High-technology exports (current US$)":df['High-technology exports (current US$)'].median(),
         "Individuals using the Internet (% of population)":df['Individuals using the Internet (% of population)'].mean(),
          "Military expenditure (% of GDP)":df['Military expenditure (% of GDP)'].median(),
        "Ratio of female to male labor force participation rate (%) (national estimate)":df["Ratio of female to male labor force participation rate (%) (national estimate)"].mean(),
        "Total reserves (includes gold, current US$)":df["Total reserves (includes gold, current US$)"].median()
        },inplace=True
    )
    return df
 
def main():
    df=pd.read_csv("final_demographics_data.csv")
    
    return filling_missing_data(df)
    
processed_df = main()
