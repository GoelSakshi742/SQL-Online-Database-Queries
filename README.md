# SQL Online Database Queries

A SQL analysis project examining Chicago's socioeconomic indicators, public schools, and crime data using Python and SQLite.

## 📋 Overview

This project demonstrates SQL querying and data analysis skills through exploration of three datasets from the City of Chicago's Data Portal. It analyzes relationships between crime patterns, educational institutions, and socioeconomic factors across Chicago's community areas.

## 🗂️ Datasets

1. **Chicago Census Data** - Socioeconomic indicators including per capita income, poverty levels, and hardship index
2. **Chicago Public Schools** - School performance data with safety scores and school types
3. **Chicago Crime Data** - Crime incidents with types, locations, and arrest records

## 🛠️ Technologies

- Python 3.x
- Pandas
- SQLite3
- ipython-sql
- Jupyter Notebook

## 🚀 Getting Started

### Installation

```bash
# Clone repository
git clone https://github.com/GoelSakshi742/SQL-Online-Database-Queries.git
cd SQL-Online-Database-Queries

# Install dependencies
pip install pandas ipython-sql prettytable

# Run notebook
jupyter notebook SQL_final_project.ipynb
```

## 📊 Analysis Questions

The project addresses 10 SQL problems:

1. Total crimes recorded
2. Communities with per capita income < $11,000
3. Crimes involving minors
4. Kidnapping cases involving children
5. Crime types at schools
6. Average safety scores by school type
7. Top 5 communities with highest poverty
8. Most crime-prone community area
9. Community with highest hardship index
10. Community with most crimes

## 💡 Sample Queries

**High-poverty areas:**
```sql
SELECT COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY
FROM census_data 
ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC 
LIMIT 5
```

**Crime-prone areas:**
```sql
SELECT COMMUNITY_AREA_NUMBER, COUNT(*)
FROM crime_data  
GROUP BY COMMUNITY_AREA_NUMBER
ORDER BY COUNT(*) DESC 
LIMIT 1
```

## 📈 Key Findings

- **Riverdale** has the highest hardship index and poverty rate (56.5%)
- **Austin** (Community Area 25) is most crime-prone with 43 incidents
- Four communities have per capita income below $11,000
- Schools experience multiple crime types including battery and narcotics

## 👤 Author

**Sakshi Goel** - [@GoelSakshi742](https://github.com/GoelSakshi742)

## 🙏 Acknowledgments

Based on IBM Developer Skills Network coursework by Hima Vasudevan, Rav Ahuja, and Ramesh Sannreddy.

---

*Data sourced from [City of Chicago Data Portal](https://data.cityofchicago.org/)*
