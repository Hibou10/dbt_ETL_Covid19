# Impfungen vs Outcomes Dashboard

```sql vaccinations
SELECT *
FROM vaccinations_vs_outcomes
```

<ScatterPlot 
    data={vaccinations}
    x=cases_per_million
    y=deaths_per_million
    label=country
    size: tests_per_thousand
/>