# from hijri_converter import convert

# # Convert the Gregorian date to Hijri
# ramadan_start_hijri = convert.Gregorian(2024, 4, 9).to_hijri()

# # Get the string representation of the Hijri date
# hijri_string = f"{ramadan_start_hijri.year}-{ramadan_start_hijri.month_name()}-{ramadan_start_hijri.day:02}"

# print("Ramadan in 2024 will start on:", hijri_string)
from hijri_converter import convert

# Convert the Hijri date to Julian
ramadan_start_julian = convert.Hijri(1445, 9, 1).to_julian()

print("Ramadan in 2024 will start on:", ramadan_start_julian)
