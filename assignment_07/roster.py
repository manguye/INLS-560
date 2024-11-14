# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {'Last Name': ['Claude', 'Cadeau', 'Tyson', 'Trimble', 'Jackson', 'Hawkins', 'Lubin', 'Mayo Jr.', 'Brown', 'Davis'],
          'First Name': ['Ty', 'Elliot', 'Cade', 'Seth', 'Ian', 'Russell', 'Ven-Allen', 'Dante', 'James', 'RJ'],
          'Height': [79, 73, 79, 75, 76, 73, 80, 73, 82, 72],
          'Weight': [230, 180, 200, 195, 190, 175, 230, 175, 215, 180]
          }

data = pd.DataFrame(player)

# BMI = Weight in kg/height in meters squared
data['bmi'] = round((data['Weight']/2.205)/((data['Height']/39.37)**2), 2)

print(data)

data.to_csv('bmi.csv')