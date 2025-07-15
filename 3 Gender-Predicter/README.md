# Gender Predictor

A terminal tool that predicts the likely gender associated with a given first name using the [Genderize.io](https://genderize.io/) API.

## Features

- Predicts gender from a first name
- Shows confidence probability as a percentage
- Input validation (letters only)
- Handles invalid names and API errors gracefully
- Loop to predict multiple names in one session

## Requirements

- Python 3.x
- `requests`

```bash
pip install requests
```

## How to Run

```bash
python gender_predictor.py
```

## Example Output

```
Enter a name (or type 'exit' to quit): Hema

===================================
       GENDER PREDICTION RESULT
===================================
  Name        : Hema
  Gender      : Female
  Probability : 57.0%
===================================

Enter a name (or type 'exit' to quit): Aryan

===================================
       GENDER PREDICTION RESULT
===================================
  Name        : Aryan
  Gender      : Male
  Probability : 95.0%
===================================

Enter a name (or type 'exit' to quit): exit

Goodbye!
```
