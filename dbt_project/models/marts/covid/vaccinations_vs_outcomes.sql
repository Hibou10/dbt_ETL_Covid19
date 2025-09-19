SELECT
    country,
    cases_per_million,
    deaths_per_million,
    tests_per_thousand
FROM {{ ref('stg_covid_raw') }}
ORDER BY deaths_per_million DESC
