SELECT
    country,
    cases,
    deaths,
    tests,
    population,
    todaycases,
    todaydeaths,
    ROUND(cases / NULLIF(population,0) * 1000000, 2) AS cases_per_million,
    ROUND(deaths / NULLIF(population,0) * 1000000, 2) AS deaths_per_million,
    ROUND(tests / NULLIF(population,0) * 1000, 2) AS tests_per_thousand
FROM {{ source('raw', 'covid_raw') }}
WHERE population > 0
