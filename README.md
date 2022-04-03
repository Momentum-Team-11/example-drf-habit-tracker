# API Documentation

## View all habits for logged in user

*Authentication required*

```txt
GET api/habits/
```

## Create a new habit

*Authentication required*

```txt
POST api/habits/
```

## Get details about a habit

*Authentication required*

Includes all daily records for a habit.

```txt
GET api/habits/{habit_pk}
```

## Create a new daily record for a habit

This defaults to creating a new daily record for today.

```txt
POST api/habits/{habit_pk}
```

## Edit a daily record

```txt
PUT/PATCH api/results/{result_pk}
```

## Delete a daily record

```txt
DELETE api/results/{result_pk}
```

## Get all daily records by date

```txt
GET api/results/{year}/{month}/{day}
```

For example, get records for March 2, 2022

`GET api/results/2022/3/2`


